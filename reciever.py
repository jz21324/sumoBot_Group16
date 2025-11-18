from machine import Pin, PWM
from ir_rx.nec import NEC_8
from ir_rx.print_error import print_error
import time

# =================================
# MOTOR CONTROLLER CLASS
# =================================
class Motor:
    def __init__(self, ph_pin, en_pin, freq=2000):
        self.ph = Pin(ph_pin, Pin.OUT)
        self.en = PWM(Pin(en_pin), freq=freq, duty_u16=0)
        self.stop()

    def forward(self, power=1.0):
        duty = int(65535 * max(min(power, 1.0), 0))
        self.ph.low()
        self.en.duty_u16(duty)
        print("[MOTOR] Forward:", duty)

    def reverse(self, power=1.0):
        duty = int(65535 * max(min(power, 1.0), 0))
        self.ph.high()
        self.en.duty_u16(duty)
        print("[MOTOR] Reverse:", duty)

    def stop(self):
        self.en.duty_u16(0)
        print("[MOTOR] Stop")

# =================================
# SETUP MOTORS
# =================================
left_motor = Motor(12, 13)
right_motor = Motor(14, 15)

# =================================
# IR COMMANDS (MATCH TRANSMITTER)
# =================================
CMD_UP     = 0x01
CMD_DOWN   = 0x02
CMD_LEFT   = 0x03
CMD_RIGHT  = 0x04
CMD_STOP   = 0x05

# =================================
# IR CALLBACK
# =================================
def ir_callback(cmd, addr, _):
    print("Received:", hex(cmd))

    if cmd == CMD_UP:
        left_motor.forward()
        right_motor.forward()

    elif cmd == CMD_DOWN:
        left_motor.reverse()
        right_motor.reverse()

    elif cmd == CMD_LEFT:
        left_motor.stop()
        right_motor.forward()

    elif cmd == CMD_RIGHT:
        left_motor.forward()
        right_motor.stop()

    elif cmd == CMD_STOP:
        left_motor.stop()
        right_motor.stop()

# =================================
# IR RECEIVER INITIALIZE
# =================================
ir_pin = Pin(19, Pin.IN, Pin.PULL_UP)
ir = NEC_8(ir_pin, callback=ir_callback)
ir.error_function(print_error)

print("IR Motor Receiver Ready")

while True:
    time.sleep(0.1)
