import numpy as np
import time

def get_sin_wave_amplitude(freq, time):
    return (np.sin(freq*2*np.pi*time)+1)/2

def wait_for_sampling_period(sampling_frequency):
    return time.sleep(1/sampling_frequency)
