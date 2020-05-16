#Created by Vishnu N M on 10th April 2020
#LEDs on Raspberry pi is initially blink mode. When any keyboard key is held down, LEDs stays on ON mode (HIGH). When key released, goes back to blink mode.
import RPi.GPIO as GPIO 
import time
import keyboard
import os
import pynput
from pynput import keyboard
from termcolor import colored, cprint

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) 
cprint('\nBLINK MODE', 'red', attrs=['blink'])
print "Hold any key to Start. Esc to exit"
while True:
   GPIO.output(8, GPIO.HIGH)
   sleep(1)
   GPIO.output(8, GPIO.LOW)
   sleep(1)
   def on_press(key):
        cprint('\nHIGH MODE', 'green')
	   GPIO.output(8, GPIO.HIGH)

   def on_release(key):
     cprint('\nBLINK MODE', 'red', attrs=['blink'])
        GPIO.output(8, GPIO.HIGH)
        sleep(1)
        GPIO.output(8, GPIO.LOW)
        sleep(1)
     if key == keyboard.Key.esc:
       return False

   with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
      listener.join()
