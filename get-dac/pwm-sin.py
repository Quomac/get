import pwm_dac as pwm
import signal_gen as sg
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000



if __name__ == "__main__":
    try:
        dac = pwm.PWM_DAC(12, 500, 3.290, True)
        
        while True:
            try:
                voltage = amplitude*sg.get_sin_wave_amplitude(signal_frequency, time.time())
                dac.set_voltage(voltage)
                sg.wait_for_sampling_period(sampling_frequency)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")
    finally:
        dac.deinit()