from machine import Pin
import time
from ir_tx.nec import NEC

# -------------------------------------------------------------------
# IR TRANSMITTER SETUP
# -------------------------------------------------------------------

tx_pin = Pin(17, Pin.OUT, value=0)   # IR LED output pin
device_addr = 0x01                   # Your IR device address
transmitter = NEC(tx_pin)

# Commands
CMD_UP    = 0x01
CMD_DOWN  = 0x02
CMD_LEFT  = 0x03
CMD_RIGHT = 0x04
CMD_STOP  = 0x05

# Optional Pico on-board LED (if supported)
try:
    led = Pin("LED", Pin.OUT)
except:
    led = Pin(25, Pin.OUT)   # Use GP25 instead

# -------------------------------------------------------------------
# SEND A COMMAND
# -------------------------------------------------------------------
def send_ir(cmd):
    """Send a single NEC IR command."""
    transmitter.transmit(device_addr, cmd)
    print("IR SENT:", hex(cmd))
    led.toggle()
    time.sleep(0.05)

# -------------------------------------------------------------------
# FUNCTION USED BY CONTROLLER PROGRAM
# -------------------------------------------------------------------
def transmutation(command=CMD_STOP):
    send_ir(command)


# -------------------------------------------------------------------
# DEBUG MODE: ONLY RUNS IF FILE RUN DIRECTLY
# -------------------------------------------------------------------
if __name__ == "__main__":
    print("Transmitter test. Sending all commands every 1 second.")
    while True:
        for cmd in [CMD_UP, CMD_DOWN, CMD_LEFT, CMD_RIGHT, CMD_STOP]:
            send_ir(cmd)
            time.sleep(1)
