import ir_tx
import time
import machine
from ir_tx.nec import NEC
from machine import Pin
from utime import sleep
tx_pin = Pin(17 ,Pin.OUT,value=0)
device_addr = 0x01
transmitter = NEC(tx_pin)
commands = [0x01,0x02,0x03,0x04]
pin = Pin("LED", Pin.OUT)
if __name__ == "__main__":
 while True:
    
    for command in commands:
        
        transmitter.transmit(device_addr,command)
        print("COMMANDS",hex(command),"TRANSMITTED.")
        pin.toggle()
        time.sleep(1)

def transmutation():
    transmitter.transmit(device_addr,commands[0])
    print("COMMANDS",hex(commands[0]),"TRANSMITTED.")
    pin.toggle()
    time.sleep(0.1)