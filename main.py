import machine
from machine import Pin, PWM
import time

pwm_rate = 20
ain1_ph = Pin(12, Pin.OUT)  # Initialize GP12 as an OUTPUT
ain2_en = PWM(Pin(13), freq=pwm_rate, duty_u16=0)

bin1_ph = Pin(14, Pin.OUT)  # Initialize GP12 as an OUTPUT
bin2_en = PWM(Pin(15), freq=pwm_rate, duty_u16=0)

pwm = min(max(int(2**16 * abs(1)), 0), 65535)

input1 = Pin(4, Pin.IN, Pin.PULL_UP)
input2 = Pin(5, Pin.IN, Pin.PULL_UP)
input3 = Pin(6, Pin.IN, Pin.PULL_UP)
input4 = Pin(7, Pin.IN, Pin.PULL_UP)

on = False

def read_rf():
    global on 

    if input2.value() == 1 and not on:
        ain1_ph.low()
        ain2_en.duty_u16(pwm)
        bin1_ph.high()
        bin2_en.duty_u16(pwm)
        print("Input 1 activated")
        on = True
        # time.sleep(0.1)

    if input1.value() == 1 and on:
        ain1_ph.low()
        ain2_en.duty_u16(0)
        bin1_ph.high()
        bin2_en.duty_u16(0)
        print("Input 2 activated")
        on = False
        # time.sleep(0.1)

if __name__ == "__main__":
    while True:
        read_rf()