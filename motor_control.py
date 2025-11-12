import machine
import time
from machine import Pin, PWM

time.sleep(0.5)

pwm_rate = 2000
ain1_ph = Pin(12, Pin.OUT)  # Initialize GP12 as an OUTPUT
ain2_en = PWM(Pin(13), freq=pwm_rate, duty_u16=0)

bin1_ph = Pin(14, Pin.OUT)  # Initialize GP12 as an OUTPUT
bin2_en = PWM(Pin(15), freq=pwm_rate, duty_u16=0)

pwm = min(max(int(2**16 * abs(1)), 0), 65535)

while True:
    print("Motor ON") # Print to REPL
    ain1_ph.low()
    ain2_en.duty_u16(pwm)
    bin1_ph.low()
    bin2_en.duty_u16(pwm)
    time.sleep(2)
    print("Motor OFF") # Print to REPL
    ain1_ph.low()
    ain2_en.duty_u16(0)
    bin1_ph.low()
    bin2_en.duty_u16(0)
    time.sleep(2)