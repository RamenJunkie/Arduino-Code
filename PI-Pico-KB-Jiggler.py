import time
import random
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

time.sleep(1)
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

total_runs = 0
running = True

# Map characters to keycodes
keyOptions = {
    "w": Keycode.W,
    "a": Keycode.A,
    "s": Keycode.S,
    "d": Keycode.D,
    " ": Keycode.SPACE
}

while running:
    led.value = True
    
    # Choose a random key
    nextKey = random.choice(list(keyOptions.keys()))
    keycode = keyOptions[nextKey]
    
    # Hold the key for 2-4 seconds (random)
    hold_duration = random.uniform(2.0, 4.0)
    
    # Press and hold the key
    keyboard.press(keycode)
    time.sleep(hold_duration)
    keyboard.release(keycode)
    
    led.value = False
    time.sleep(0.1)
    
    # Wait before next key press
    nextSleep = random.randint(20, 40)
    time.sleep(nextSleep)
    
    total_runs = total_runs + 1
    if total_runs > 480:
        running = False
