import machine
from machine import Pin, PWM
from ir_rx.nec import NEC_8
from ir_rx.print_error import print_error
from time import sleep

def ir_callback(data, addr, _):
    print(f"Received NEC command! Data: 0x{data:02X}, Address: 0x{addr:02X}")

ir_pin = Pin(14, Pin.IN, Pin.PULL_UP)

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