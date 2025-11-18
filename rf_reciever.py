import machine
from machine import Pin, PWM
import time

led1 = Pin(14, Pin.OUT)
led2 = Pin(15, Pin.OUT)
led3 = Pin(16, Pin.OUT)
led4 = Pin(17, Pin.OUT)

input1 = Pin(0, Pin.IN, Pin.PULL_UP)
input2 = Pin(1, Pin.IN, Pin.PULL_UP)
input3 = Pin(2, Pin.IN, Pin.PULL_UP)
input4 = Pin(3, Pin.IN, Pin.PULL_UP)

def read_rf():
    if input1.value() == 1:
        led1.value(1)
        print("Input 1 activated")
        time.sleep(0.2)
    else:
        led1.value(0)
    if input2.value() == 1:
        led2.value(1)
        print("Input 2 activated")
        time.sleep(0.2)
    else:
        led2.value(0)
    if input3.value() == 1:
        led3.value(1)
        print("Input 3 activated")
        time.sleep(0.2)
    else:
        led3.value(0)
    if input4.value() == 1:
        led4.value(1)
        print("Input 4 activated")
        time.sleep(0.2)
    else:
        led4.value(0)

if __name__ == "__main__":
    read_rf()