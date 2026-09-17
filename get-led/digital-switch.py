import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

led = 26

bt = 6

state = 0

gpio.setup(bt, gpio.IN)
gpio.setup(led, gpio.OUT)

while True:
    if gpio.input(bt) == 1:
        state = not state
        gpio.output(led, state)
        time.sleep(0.2)