import machine
from machine import Pin, PWM
from ir_rx.nec import NEC_8
from ir_rx.print_error import print_error
from time import sleep
import rf_reciever

switch = Pin(22, Pin.IN, Pin.PULL_UP)

def ir_callback(data, addr, _):
    print(f"Received NEC command! Data: 0x{data:02X}, Address: 0x{addr:02X}")
    rf_reciever.led1.value(1)
    rf_reciever.led2.value(1)
    rf_reciever.led3.value(1)
    rf_reciever.led4.value(1)

ir_pin = Pin(19, Pin.IN, Pin.PULL_UP)


ir_receiver = NEC_8(ir_pin, callback=ir_callback)

ir_receiver.error_function(print_error)

while True:
    if switch.value() == 0:
        print("IR Receiver Disabled")
        ir_receiver.callback = None
        rf_reciever.read_rf()
    else:
        print("IR Receiver Enabled")
        ir_receiver.callback = ir_callback
        sleep(0.1)
        