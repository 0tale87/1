#!/usr/bin/python
# -*- coding: utf-8; -*-

import subprocess
import RPi.GPIO as GPIO
import time
PIN=21

GPIO.setmode(GPIO.BCM)

GPIO.setup(PIN,GPIO.IN)

while True:
    pirValue = GPIO.input(PIN)
    if( pirValue == True):
        subprocess.call('tvservice -o')
        time.sleep(10)
        subprocess.call('tvservice -p')
        subprocess.call('fbset -depth 8')
        subprocess.call('fbset -depth 32')
        subprocess.call('xrefresh -d :0.0')
    time.sleep(0.1)
