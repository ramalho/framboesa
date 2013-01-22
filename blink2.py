#!/usr/bin/env python
# coding: utf-8

import RPi.GPIO as GPIO
from time import sleep

def blink(pin, repetitions=1):
    for i in xrange(repetitions):
        GPIO.output(pin,GPIO.HIGH)
        sleep(.5)
        GPIO.output(pin,GPIO.LOW)
        sleep(.5)

def on_off(pin, time=.1):
        GPIO.output(pin,GPIO.HIGH)
        sleep(time)
        GPIO.output(pin,GPIO.LOW)

# use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)

pins = [11, 12, 13, 15, 16, 18, 22, 7]

# set up GPIO output channel
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

for pin in pins:
    on_off(pin, .2)

GPIO.cleanup()
