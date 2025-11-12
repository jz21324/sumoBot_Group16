import machine
import time
from machine import Pin, PWM
from ir_rx.nec import NEC_8
from ir_rx.print_error import print_error
from time import sleep

time.sleep(0.5)

def ir_callback(data, addr, _):
    print(f"Received NEC command! Data: 0x{data:02X}, Address: 0x{addr:02X}")
    ain1_ph.low()
    bin1_ph.low()
    ain2_en.duty_u16(65535)
    bin2_en.duty_u16(65535)

    time.sleep(2)

    ain2_en.duty_u16(0)
    bin2_en.duty_u16(0)

pwm_rate = 2000
ain1_ph = Pin(12, Pin.OUT)  # Initialize GP12 as an OUTPUT
ain2_en = PWM(Pin(13), freq=pwm_rate, duty_u16=0)

bin1_ph = Pin(14, Pin.OUT)  # Initialize GP12 as an OUTPUT
bin2_en = PWM(Pin(15), freq=pwm_rate, duty_u16=0)

ir_pin = Pin(18, Pin.IN, Pin.PULL_UP)

ir_receiver = NEC_8(ir_pin, callback=ir_callback)

pwm1 = Pin(17) # Set the pin for the PWM object

ir_receiver.error_function(print_error)

while True: 
    time.sleep(0.1)
    