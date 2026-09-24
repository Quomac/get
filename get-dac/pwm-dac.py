import RPi.GPIO as gpio

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.pin = gpio_pin
        self.freq = pwm_frequency
        self.range = dynamic_range
        self.pwm = gpio.PWM(self.pin, 200)
        self.verbose = verbose
        self.duty = 0
        self.pwm.start(self.duty)

        gpio.setmode(gpio.BCM)
        gpio.setup(self.pin, gpio.OUT, initial = 0)
        
    def deinit(self):
        gpio.output(self.pin, 0)
        gpio.cleanup()

    def set_pwm(self, duty):
            self.pwm.ChangeDutyCycle(duty)
    
    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.range:.2f} В)")
            print("Устанавлниваем 0.0 В")
            self.set_pwm(0)
        else:
            self.set_pwm(int(voltage / self.range * self.freq))

        

if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 500, 3.290, True)
        
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()