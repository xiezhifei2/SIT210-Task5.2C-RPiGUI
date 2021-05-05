from Tkinter import *
import Tkinter as tk
import tkFont
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)
##hardware
led_red = LED(14)
led_blue = LED(15)
led_green = LED(18)

##event function
def Red_ledToggle():
    if led_red.is_lit:
        led_red.off()
        RedButton["text"] = "Turn Red on"
    else:
        led_red.on()
        RedButton["text"] = "Turn Red off"

def Blue_ledToggle():
    if led_blue.is_lit:
        led_blue.off()
        BlueButton["text"] = "Turn Blue on"
    else:
        led_blue.on()
        BlueButton["text"] = "Turn Blue off"

def Green_ledToggle():
    if led_green.is_lit:
        led_green.off()
        GreenButton["text"] = "Turn Green on"
    else:
        led_green.on()
        GreenButton["text"] = "Turn Green off"
        

        
def close():
    RPi.GPIO.cleanup()
    win.destroy()
    
##GUI definition
win = tk.Tk()
win.title("LED Toggler")
myFont = tkFont.Font(family = 'Helvetica',size = 12, weight = "bold")

##WIDGETS
RedButton = Button(win, text = "Turn Red on", font = myFont, command = Red_ledToggle, bg = 'bisque2',height = 1, width = 24)
RedButton.grid(row = 0, column=1)

BlueButton = Button(win, text = "Turn Bluee on", font = myFont, command = Blue_ledToggle, bg = 'bisque2',height = 1, width = 24)
BlueButton.grid(row = 1, column=1)

GreenButton = Button(win, text = "Turn Green on", font = myFont, command = Green_ledToggle, bg = 'bisque2',height = 1, width = 24)
GreenButton.grid(row = 2, column=1)

exitButton = Button(win, text = "Exit", font = myFont, command = close, bg = 'red',height = 1, width = 6)
exitButton.grid(row = 3, column=1)

win.protocol("WM_DELETE_WINDOW",close)#exit cleanly

win.mainloop()#keep loopping


