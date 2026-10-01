import sinus_mp as mcp
import signal_gen as sg
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000



if __name__ == "__main__":
    try:
        dac = mcp.MCP4725(5)
        
        while True:
            try:
                voltage = sg.get_sin_wave_amplitude(signal_frequency, time.time())
                dac.set_voltage(voltage)
                sg.wait_for_sampling_period(sampling_frequency)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()