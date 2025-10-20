import machine
from machine import Pin
from ir_rx.nec import NEC_8
from ir_rx.print_error import print_error

def ir_callback(data, addr, _):
    print(f"Received NEC command! Data: 0x{data:02X}, Address: 0x{addr:02X}")

ir_pin = Pin(14, Pin.IN, Pin.PULL_UP)

ir_receiver = NEC_8(ir_pin, callback=ir_callback)

ir_receiver.error_function(print_error)

while True:
    pass  # GPIO14 for IR receiver