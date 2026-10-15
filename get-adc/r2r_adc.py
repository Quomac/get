import RPi.GPIO as gpio
import time


class R2R_ADC:
    def __init__(self, dynamic_range, compare_time, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time
        
        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        gpio.setmode(gpio.BCM)
        gpio.setup(self.bits_gpio, gpio.OUT, initial = 0)
        gpio.setup(self.comp_gpio, gpio.IN)

    def deinit(self):
        gpio.output(self.bits_gpio, 0)
        gpio.cleanup()

    def number_to_dac(self, number):
        gpio.output(self.bits_gpio, [int(element) for element in bin(number)[2:].zfill(8)])

    def sequential_counting_adc(self):
        for x in range(256):
            self.number_to_dac(x)
            time.sleep(self.compare_time)
            #print(x)
            if gpio.input(self.comp_gpio) == 1:
                return x
        return 255
    
    def successive_approximation_adc(self):
        s = bin(0)[2:].zfill(8)
        for x in range(0, 8):
            self.number_to_dac(int(s[:x] + '1' + s[(x+1):], 2))
            time.sleep(self.compare_time)
            if gpio.input(self.comp_gpio) == 1:
                s = s[:x] + '0' + s[(x+1):]
            else:
                s = s[:x] + '1' + s[(x+1):]
            #print(s)
        return int(s, 2)

    def get_sc_voltage(self):
        #print(0, self.sequential_counting_adc())
        return (self.sequential_counting_adc()/255)*self.dynamic_range
    
    def get_sa_voltage(self):
        #print(0, self.sequential_counting_adc())
        return (self.successive_approximation_adc()/255)*self.dynamic_range
    
        
