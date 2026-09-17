import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

led = 26
bt = 13

leds = [24, 22, 23, 27, 17, 25, 12, 16]

gpio.setup(bt, gpio.IN)
gpio.setup(leds, gpio.OUT)
gpio.output(leds, 0)

cur = 0
state = 0
while True:
    for led in leds:
        gpio.output(led, 1)
        time.sleep(0.05)
        gpio.output(led, 0)

    for led in reversed(leds):
        gpio.output(led, 1)
        time.sleep(0.05)
        gpio.output(led, 0)