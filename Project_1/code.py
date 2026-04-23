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

