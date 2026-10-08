import RPi.GPIO as gpio
import time


class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01, verbose = False):
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
            if gpio.input(self.comp_gpio) == 1:
                return gpio.input(self.comp_gpio)
        return 255
    def get_sc_voltage(self):
        return (self.sequential_counting_adc()/255)*self.dynamic_range
    
if __name__ == "__main__":
    try:
        adc = R2R_ADC(3.28)
        
        while True:
            try:
                voltage = adc.get_sc_voltage()
                print(f"Измеренное напряжение: {voltage:.3f} В")
                time.sleep(0.5)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        adc.deinit()
        
