import RPi.GPIO as gpio

class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        
        gpio.setmode(gpio.BCM)
        gpio.setup(self.gpio_bits, gpio.OUT, initial = 0)
    
    def deinit(self):
        gpio.output(self.gpio_bits, 0)
        gpio.cleanup()
    
    def set_number(self, number):
        #print([int(element) for element in bin(number)[2:].zfill(8)], number)
        gpio.output(self.gpio_bits, [int(element) for element in bin(number)[2:].zfill(8)])

    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.dynamic_range:.2f} В)")
            print("Устанавлниваем 0.0 В")
            self.set_number(0)
        else:
            self.set_number(int(voltage / self.dynamic_range * 255))
        #print(111)




if __name__ == "__main__":
    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)
        
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()