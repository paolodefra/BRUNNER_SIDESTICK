# BRUNNER_SIDESTICK
UDP–MAVLink bridge to connect Brunner CLS2Sim output with the MARSH simulator

Python tools to interface the **Brunner CLS2Sim / Sim2** active control hardware  
with the **MARSH** simulation environment developed at Politecnico di Milano’s  
Rotorcraft–Pilot Coupling (RPC) laboratory.

## 🚁 Overview

This repository provides a modular set of scripts to capture, analyze and forward
joystick data from the Brunner control system to the MARSH simulator using the
MAVLink `MANUAL_CONTROL` message.  

It enables **pilot-in-the-loop testing** with real inceptor hardware, supporting
research on biodynamic feedback, control-system stability, and Rotorcraft–Pilot Coupling (RPC)
phenomena.

---

## 📡 System Architecture

      ┌──────────────────────┐
      │   Brunner CLS2Sim    │
      │ (or Sim2 application)│
      └──────────┬───────────┘
                 │ UDP packets
                 ▼
      ┌──────────────────────┐
      │   brunner_sniff.py   │
      │ (packet monitor/log) │
      └──────────┬───────────┘
                 │ parsed data
                 ▼
      ┌──────────────────────┐
      │  brunner_to_marsh.py │
      │ (UDP → MAVLink bridge│
      └──────────┬───────────┘
                 │ MANUAL_CONTROL msgs
                 ▼
      ┌──────────────────────┐
      │        MARSH         │
      │ (Simulator environment)
      └──────────────────────┘


The same architecture can run **without hardware** using  
`brunner_controls_debug.py`, which generates artificial joystick data
to verify communication with MARSH.

---

## 🧩 Repository Structure

| File | Description |
|------|--------------|
| `scripts/brunner_sniff.py` | Listens to UDP packets from CLS2Sim / Sim2 and saves them to a log file for analysis. |
| `scripts/brunner_controls_debug.py` | Simulates joystick inputs and sends `MANUAL_CONTROL` messages to MARSH (offline testing). |
| `scripts/brunner_to_marsh.py` | Receives real UDP data from Brunner, parses it, and forwards it to MARSH via MAVLink. |


---






