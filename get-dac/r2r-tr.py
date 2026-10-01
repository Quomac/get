import r2r_dac as r2r
import signal_gen as sg
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000



if __name__ == "__main__":
    try:
        dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.2, True)
        
        while True:
            try:
                voltage = sg.get_tr_wave_amplitude(signal_frequency, time.time())*amplitude
                dac.set_voltage(voltage)
                sg.wait_for_sampling_period(sampling_frequency)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()