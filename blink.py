#!/usr/bin/env python
# coding: utf-8

import RPi.GPIO as GPIO
import time

def blink(pin, times=1):
    for i in xrange(times):
        GPIO.output(pin,GPIO.HIGH)
        time.sleep(.5)
        GPIO.output(pin,GPIO.LOW)
        time.sleep(.5)

# use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)

# set up GPIO output channel
pin = 12
GPIO.setup(pin, GPIO.OUT)

# blink 6 times
blink(pin, 6)

GPIO.cleanup()
