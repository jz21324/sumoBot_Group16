import machine
from machine import Pin, PWM
import time

pwm_rate = 2000
ain1_ph = Pin(12, Pin.OUT)  # Initialize GP12 as an OUTPUT
ain2_en = PWM(Pin(13), freq=pwm_rate, duty_u16=0)

bin1_ph = Pin(14, Pin.OUT)  # Initialize GP12 as an OUTPUT
bin2_en = PWM(Pin(15), freq=pwm_rate, duty_u16=0)

pwm = min(max(int(2**16 * abs(1)), 0), 65535)

inputA = Pin(4, Pin.IN, Pin.PULL_UP)
inputB = Pin(5, Pin.IN, Pin.PULL_UP)
inputC = Pin(6, Pin.IN, Pin.PULL_UP)
inputD = Pin(7, Pin.IN, Pin.PULL_UP)

def read_rf():
    if inputA.value() == 1:
        print("Motor A ON") # Print to REPL
        ain1_ph.low()
        ain2_en.duty_u16(pwm)
    else:
        print("Motor OFF") # Print to REPL
        ain1_ph.low()
        ain2_en.duty_u16(0)

if __name__ == "__main__":
    time.sleep(0.5)

    while True:
        read_rf()
        time.sleep(0.01)