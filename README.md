# BRUNNER_SIDESTICK
UDP–MAVLink bridge to connect Brunner CLS2Sim output with the MARSH simulator
# Brunner–MARSH Interface

This repository contains Python scripts to interface the **Brunner CLS2Sim / Sim2** application
with the **MARSH** simulation environment at Politecnico di Milano.

## Structure

| Script | Description |
|---------|--------------|
| `brunner_sniff.py` | Listens to UDP packets from CLS2Sim and logs raw data to identify packet structure |
| `brunner_controls_debug.py` | Generates simulated joystick data (no hardware required) and sends MANUAL_CONTROL messages |
| `brunner_to_marsh.py` | Final interface: receives UDP data from Brunner and sends MAVLink MANUAL_CONTROL to MARSH |

## Requirements
- Python ≥ 3.10  
- Install dependencies with:

```bash
pip install -r requirements.txt
