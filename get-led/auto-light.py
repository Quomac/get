import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

led = 26
ls = 13 

gpio.setup(led, gpio.OUT)
gpio.setup(ls, gpio.IN)

while True:
    if gpio.input(ls) == 1:
        state = 1
    else:
        state = 0
    gpio.output(led, state)
    time.sleep(0.2)