#  Day 1: The Heartbeat (Onboard LED)

Welcome to the first project of my **CircuitPython on Pico 2 W** series.  
This project focuses on setting up the development environment and verifying the core functionality of the RP2350 microcontroller.

---

##  Project Overview

This is the "Hello World" of embedded systems.  
The goal is to ensure that:

- CircuitPython firmware is correctly flashed  
- The onboard filesystem is accessible  
- GPIO control is working properly  

---

##  Hardware Components

- **Board:** Raspberry Pi Pico 2 W  
- **Onboard LED:** Connected to `board.LED` (Internal)

---

##  Filesystem Architecture

CircuitPython uses a unique and beginner-friendly workflow:

- **`code.py`**  
  The main script that runs automatically on boot.

- **`CIRCUITPY` Drive**  
  The board appears as a USB mass storage device.  
  You can directly copy files to it — "Save-to-Run" workflow.

---

##  Code (`code.py`)

```python
import board
import digitalio
import time

led=digitalio.DigitalInOut(board.LED)
led.direction=digitalio.Direction.OUTPUT

print("Project 01: led blinking")

while True:
    led.value=True
    print("LED ON")
    time.sleep(0.5)
    led.value=False
    print("LED OFF")
    time.sleep(0.5)
```

##  Key Learnings

### Digital Output Logic
GPIO pins must be explicitly configured as output using `Direction.OUTPUT`.

### Boolean Control
CircuitPython uses `True` (HIGH) and `False` (LOW), making the code intuitive.

### Auto-Reload Feature
CircuitPython automatically reloads code when files are saved, enabling rapid prototyping.

---

##  How to Run

1. Connect your Raspberry Pi Pico 2 W to your computer  
2. Ensure the `CIRCUITPY` drive appears  
3. Copy the `code.py` file to the root directory  
4. Open a Serial Monitor (Thonny / Mu Editor)  
5. Observe LED blinking and debug messages  

---

## 👨‍💻 Author

**Kritish Mohapatra**  

Part of the **IoT with CircuitPython Series**