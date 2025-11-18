from machine import I2C, Pin
import time
from seesaw import Seesaw
from transmitter import transmutation   # your IR send function

# -------------------------------------------------------------------
# I2C + SEESAW INITIALIZATION
# -------------------------------------------------------------------

i2c = I2C(1, scl=Pin(3), sda=Pin(2), freq=100000)

print("I2C scan:", i2c.scan())
# Should show: [8, 80]  ---> 0x08 and 0x50
# We use 0x50 for the Seesaw
seesaw_dev = Seesaw(i2c, addr=0x50)

# -------------------------------------------------------------------
# GAMEPAD CONSTANTS
# -------------------------------------------------------------------

BUTTON_A = 5
BUTTON_B = 1
BUTTON_X = 6
BUTTON_Y = 2
BUTTON_START = 16
BUTTON_SELECT = 0

JOYSTICK_X_PIN = 14
JOYSTICK_Y_PIN = 15

BUTTONS_MASK = (
    (1 << BUTTON_X)
    | (1 << BUTTON_Y)
    | (1 << BUTTON_A)
    | (1 << BUTTON_B)
    | (1 << BUTTON_SELECT)
    | (1 << BUTTON_START)
)

LED_1_PIN = 12
LED_2_PIN = 13
LED_3_PIN = 15
LED_4_PIN = 14

joystick_center_x = 511
joystick_center_y = 497
joystick_threshold = 50

# Track last button state to detect new presses
last_buttons = 0


# -------------------------------------------------------------------
# SETUP
# -------------------------------------------------------------------
def setup():
    seesaw_dev.pin_mode_bulk(BUTTONS_MASK, seesaw_dev.INPUT_PULLUP)
    print("Buttons configured.")


# -------------------------------------------------------------------
# READ BUTTONS
# -------------------------------------------------------------------
def read_buttons():
    return seesaw_dev.digital_read_bulk(BUTTONS_MASK)


# -------------------------------------------------------------------
# PROCESS BUTTONS
# -------------------------------------------------------------------
def handle_buttons(current_buttons):
    global last_buttons

    # Detect new presses
    changed = current_buttons & ~last_buttons

    if changed & (1 << BUTTON_A):
        print("A pressed → SEND IR")
        transmutation()    # your IR send
    if changed & (1 << BUTTON_B):
        print("B pressed → SEND IR")
        transmutation()
    if changed & (1 << BUTTON_X):
        print("X pressed → SEND IR")
        transmutation()
    if changed & (1 << BUTTON_Y):
        print("Y pressed → SEND IR")
        transmutation()

    last_buttons = current_buttons


# -------------------------------------------------------------------
# READ JOYSTICK
# -------------------------------------------------------------------
def read_joystick():
    x = seesaw_dev.analog_read(JOYSTICK_X_PIN)
    y = seesaw_dev.analog_read(JOYSTICK_Y_PIN)
    return x, y


# -------------------------------------------------------------------
# PROCESS JOYSTICK MOVEMENT
# -------------------------------------------------------------------
def handle_joystick(x, y):
    if abs(x - joystick_center_x) < joystick_threshold and \
       abs(y - joystick_center_y) < joystick_threshold:
        return  # dead zone — don't send anything

    if y < joystick_center_y - joystick_threshold:
        print("Joystick UP → SEND IR")
        transmutation()

    elif y > joystick_center_y + joystick_threshold:
        print("Joystick DOWN → SEND IR")
        transmutation()

    elif x < joystick_center_x - joystick_threshold:
        print("Joystick LEFT → SEND IR")
        transmutation()

    elif x > joystick_center_x + joystick_threshold:
        print("Joystick RIGHT → SEND IR")
        transmutation()


# -------------------------------------------------------------------
# MAIN LOOP
# -------------------------------------------------------------------
def main():
    setup()
    last_x, last_y = read_joystick()

    while True:
        # BUTTON HANDLING
        current_buttons = read_buttons()
        handle_buttons(current_buttons)

        # JOYSTICK HANDLING
        x, y = read_joystick()
        if abs(x - last_x) > joystick_threshold or abs(y - last_y) > joystick_threshold:
            handle_joystick(x, y)
            last_x, last_y = x, y

        time.sleep(0.05)


# -------------------------------------------------------------------
# RUN
# -------------------------------------------------------------------
if __name__ == "__main__":
    main()
