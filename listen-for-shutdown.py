#!/usr/bin/env python

import RPi.GPIO as GPIO
import subprocess
import time

def Shutdown(channel):
    start_time = time.time()
    while GPIO.input(channel) == 0:
        pass
    press_time = time.time()-start_time

    if press_time > 3:
        print("Shutting Down")
        subprocess.call(['shutdown', '-h', 'now'],shell=False)
    else:
        print("Ignoring System shutdown button, not long enough signal")

GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(3, GPIO.FALLING, callback=Shutdown, bouncetime=500)

while 1:
    time.sleep(1)
