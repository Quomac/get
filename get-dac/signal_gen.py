import numpy as np
import time

def get_sin_wave_amplitude(freq, time):
    return (np.sin(freq*2*np.pi*time)+1)/2

def triangle(ln, time):
    if (time/ln<0.5):
        return (time/ln)*2
    else:
        return 2*(1-time/ln)

def get_tr_wave_amplitude(period, time):
    return triangle(period, time%(period))

def wait_for_sampling_period(sampling_frequency):
    return time.sleep(1/sampling_frequency)
