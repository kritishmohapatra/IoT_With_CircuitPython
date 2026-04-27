import board
import pwmio
import time

led_pwm=pwmio.PWMOut(board.GP15, frequency=500, duty_cycle=0)

while True:
    for i in range(0, 65535, 500):
        led_pwm.duty_cycle=i
        time.sleep(0.01)
    for i in range(65535, 0, -500):
        led_pwm.duty_cycle=i
        time.sleep(0.01)
