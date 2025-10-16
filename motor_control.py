import machine
import time
from machine import Pin, PWM

time.sleep(0.5)

pwm_rate = 2000
ain1_ph = Pin(12, Pin.OUT)  # Initialize GP12 as an OUTPUT
ain2_en = PWM(Pin(13), freq=pwm_rate, duty_u16=0)
led = Pin(18, Pin.OUT)

pwm = min(max(int(2**16 * abs(1)), 0), 65535)

while True:
    print("Motor ON") # Print to REPL
    ain1_ph.low()
    ain2_en.duty_u16(pwm)
    led.high()
    time.sleep(2)
    print("Motor OFF") # Print to REPL
    ain1_ph.low()
    ain2_en.duty_u16(0)
    led.low()
    time.sleep(2)