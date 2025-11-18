import machine
from machine import Pin, PWM
import time

pwm_rate = 2000
ain1_ph = Pin(12, Pin.OUT)
ain2_en = PWM(Pin(13), freq=pwm_rate, duty_u16=0)
bin1_ph = Pin(14, Pin.OUT)
bin2_en = PWM(Pin(15), freq=pwm_rate, duty_u16=0)

pwm = min(max(int(2**16 * abs(1)), 0), 65535)

input1 = Pin(4, Pin.IN, Pin.PULL_UP)
input2 = Pin(5, Pin.IN, Pin.PULL_UP)
input3 = Pin(6, Pin.IN, Pin.PULL_UP)
input4 = Pin(7, Pin.IN, Pin.PULL_UP)

prev = 0  # start high because PULL_UP means idle = 1

def read_rf():
    global prev
    curr = input1.value()

    # detect button press (falling edge: 0 -> 1)
    if prev == 0 and curr == 1:
        ain1_ph.low()
        ain2_en.duty_u16(pwm)
        bin1_ph.low()
        bin2_en.duty_u16(pwm)
        print("Button pressed → Motors ON")

    # detect button release (rising edge: 1 -> 0)
    if prev == 1 and curr == 0:
        ain1_ph.low()
        ain2_en.duty_u16(0)
        bin1_ph.low()
        bin2_en.duty_u16(0)
        print("Button released → Motors OFF")

    prev = curr
    time.sleep(0.03)  # small debounce (20ms)

if __name__ == "__main__":
    while True:
        read_rf()
