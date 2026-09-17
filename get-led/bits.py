import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

led = 26
up = 9
down = 10

leds = [24, 22, 23, 27, 17, 25, 12, 16]

gpio.setup(up, gpio.IN)
gpio.setup(down, gpio.IN)
gpio.setup(leds, gpio.OUT)
gpio.output(leds, 0)

s = ""

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

cur = 0
state = 0
while True:
    if gpio.input(up) == 1:
        cur+=1
    elif gpio.input(down) == 1:
        cur-=1
    if cur<0:
        cur = 255
    elif cur > 255:
        cur = 0
    gpio.output(leds, dec2bin(cur)) 
    time.sleep(0.1)
    