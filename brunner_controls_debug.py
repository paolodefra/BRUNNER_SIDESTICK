#!/usr/bin/env python3
"""
Offline MARSH test node (no hardware required)
Simulates Brunner joystick data and sends MANUAL_CONTROL via MAVLink
"""

import math
import time
from pymavlink import mavutil
from pymavlink.dialects.v20 import common as mavlink

MARSH_IP = "127.0.0.1"
MARSH_PORT = 24400
RATE_HZ = 50.0

mav_conn = mavutil.mavlink_connection(f"udpout:{MARSH_IP}:{MARSH_PORT}")
mav = mavlink.MAVLink(mav_conn)
mav.srcSystem = 1
mav.srcComponent = mavlink.MAV_COMP_ID_USER1

print(f"Sending simulated MANUAL_CONTROL to {MARSH_IP}:{MARSH_PORT}")
print("Press Ctrl+C to stop.\n")

interval = 1.0 / RATE_HZ
t0 = time.time()

try:
    while True:
        t = time.time() - t0
        x = int(1000 * math.sin(2 * math.pi * t / 4))   # roll
        y = int(1000 * math.cos(2 * math.pi * t / 4))   # pitch
        z = int(500 + 500 * math.sin(2 * math.pi * t / 6))  # collective
        r = int(300 * math.sin(2 * math.pi * t / 2))   # yaw
        buttons = 0

        mav.manual_control_send(
            target=mav.srcSystem,
            x=x, y=y, z=z, r=r, buttons=buttons
        )

        print(f"Sent: roll={x:5d}, pitch={y:5d}, coll={z:4d}, yaw={r:5d}")
        time.sleep(interval)

except KeyboardInterrupt:
    print("\nStopped by user.")
