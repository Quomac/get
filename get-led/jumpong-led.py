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

while True:
    cur+=1
    if cur >= 7:
        cur = 0
    gpio.output(leds[cur], 1)
    time.sleep(1)