#!/usr/bin/env python3
"""
Brunner to MARSH bridge
Reads UDP packets from CLS2Sim and sends MANUAL_CONTROL via MAVLink.
"""

import socket
import struct
import time
from pymavlink import mavutil
from pymavlink.dialects.v20 import common as mavlink

# === CONFIG ===
BRUNNER_PORT = 23234
MARSH_IP = "127.0.0.1"
MARSH_PORT = 24400
# ===============

# UDP listener
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", BRUNNER_PORT))
sock.settimeout(0.1)

# MAVLink setup
conn = mavutil.mavlink_connection(f"udpout:{MARSH_IP}:{MARSH_PORT}")
mav = mavlink.MAVLink(conn)
mav.srcSystem = 1
mav.srcComponent = mavlink.MAV_COMP_ID_USER1

print(f"Listening Brunner UDP on port {BRUNNER_PORT}")
print(f"Sending MANUAL_CONTROL to MARSH at {MARSH_IP}:{MARSH_PORT}")
print("Press Ctrl+C to stop.\n")

def parse_brunner_packet(data):
    """
    Placeholder parser.
    Replace this with actual unpacking once packet format is known.
    """
    # Example: suppose packet has 4 float32 values [roll, pitch, yaw, thrust]
    if len(data) >= 16:
        roll, pitch, yaw, thrust = struct.unpack("<ffff", data[:16])
        return roll, pitch, yaw, thrust
    else:
        # fallback if unknown format
        return 0.0, 0.0, 0.0, 0.5

try:
    while True:
        try:
            data, addr = sock.recvfrom(2048)
            roll, pitch, yaw, thrust = parse_brunner_packet(data)

            # Scale to MAVLink MANUAL_CONTROL range
            x = int(max(-1.0, min(1.0, roll)) * 1000)
            y = int(max(-1.0, min(1.0, pitch)) * 1000)
            r = int(max(-1.0, min(1.0, yaw)) * 1000)
            z = int((max(0.0, min(1.0, thrust))) * 1000)

            mav.manual_control_send(target=mav.srcSystem, x=x, y=y, z=z, r=r, buttons=0)
            print(f"→ Sent to MARSH | Roll:{x:5d} Pitch:{y:5d} Yaw:{r:5d} Thr:{z:4d}")

        except socket.timeout:
            pass

        time.sleep(0.02)

except KeyboardInterrupt:
    print("\nStopped by user.")
