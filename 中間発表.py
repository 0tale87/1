#!/usr/bin/python
# -*- coding: utf-8; -*-

import RPi.GPIO as GPIO
import time
PIN=21

GPIO.setmode(GPIO.BCM)

GPIO.setup(PIN,GPIO.IN)

while True:
    pirValue = GPIO.input(PIN)
    if( pirValue == True):
        print "PIR = ON"

    time.sleep(0.1)
