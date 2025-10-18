#!/usr/bin/env python3
"""
Brunner UDP Sniffer
Use this script to monitor raw UDP packets from CLS2Sim or Sim2.
"""

import socket
import datetime

UDP_IP = "0.0.0.0"       # ascolta su tutte le interfacce locali
UDP_PORT = 23234         # cambia con la porta configurata in CLS2Sim
SAVE_TO_FILE = True
LOGFILE = "brunner_packets.log"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Listening on {UDP_IP}:{UDP_PORT}")
print("Press Ctrl+C to stop.\n")

try:
    with open(LOGFILE, "w") if SAVE_TO_FILE else open("/dev/null", "w") as f:
        while True:
            data, addr = sock.recvfrom(2048)
            hex_str = data.hex(" ")
            line = f"{datetime.datetime.now().strftime('%H:%M:%S')} | From {addr} | {hex_str}"
            print(line)
            f.write(line + "\n")
except KeyboardInterrupt:
    print("\nStopped.")
