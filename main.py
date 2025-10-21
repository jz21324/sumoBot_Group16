import machine
from machine import Pin, PWM
from ir_rx.nec import NEC_8
from ir_rx.print_error import print_error
from time import sleep

def ir_callback(data, addr, _):
    print(f"Received NEC command! Data: 0x{data:02X}, Address: 0x{addr:02X}")
    led1.toggle()
    led2.toggle()
    led3.toggle()

ir_pin = Pin(19, Pin.IN, Pin.PULL_UP)
led1 = Pin(16, Pin.OUT)
led2 = Pin(17, Pin.OUT)
led3 = Pin(20, Pin.OUT)

ir_receiver = NEC_8(ir_pin, callback=ir_callback)

pwm = PWM(Pin(18)) # Set the pin for the PWM object
pwm.freq(10)

ir_receiver.error_function(print_error)

while True:
    for duty in range(32768):
        pwm.duty_u16(duty)
        sleep(0.0001)
    for duty in range(32768, 0, -1):
        pwm.duty_u16(duty)
        sleep(0.0001)  # GPIO14 for IR receiver