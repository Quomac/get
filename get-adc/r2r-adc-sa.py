import RPi.GPIO as gpio
import time
import r2r_adc as r2r

if __name__ == "__main__":
    try:
        adc = r2r.R2R_ADC(3.28)
        
        while True:
            try:
                voltage = adc.get_sa_voltage()
                print(f"Измеренное напряжение: {voltage:.3f} В")
                time.sleep(0.5)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        adc.deinit()
        
