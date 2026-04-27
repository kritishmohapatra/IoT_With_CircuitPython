import board
import digitalio
import time

btn=digitalio.DigitalInOut(board.GP14)
btn.direction=digitalio.Direction.INPUT
btn.pull=digitalio.Pull.UP

led=digitalio.DigitalInOut(board.GP15)
led.direction=digitalio.Direction.OUTPUT

led_state=False
while True:
    if not btn.value:
        led_state=not led_state
        led.value=led_state
        
    while not btn.value:
        time.sleep(0.01)
    time.sleep(0.001)
    
