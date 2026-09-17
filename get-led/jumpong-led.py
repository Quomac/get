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
    if cur >= 8:
        cur = 0
        state = not state
    gpio.output(leds[cur], state)
    cur+=1
    time.sleep(1)