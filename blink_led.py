from machine import Pin
from utime import sleep

led1 = Pin(14, Pin.OUT)
led2 = Pin(15, Pin.OUT)
led3 = Pin(16, Pin.OUT)

print("LED starts flashing...")
while True:
    try:
        led1.toggle()
        led2.toggle()
        led3.toggle()
        sleep(1)
    except KeyboardInterrupt:
        break

led1.off()
led2.off()
led3.off()
print("Finished.")