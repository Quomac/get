import r2r_adc as ac
import time
import matplotlib.pyplot as plt

mxv = 3.28

r2r = ac.R2R_ADC(mxv, 0.0001)

time_null = time.time()

time_measure = 0.001

x = []
y = []

sampl_per = []

#print(r2r.get_sc_voltage())


def plot_voltage_vs_time(time_dur):
    time_null_def = time.time()
    while (time.time()-time_null_def < time_dur):
        x0 = time.time()-time_null_def
        x.append(x0)
        y0 = r2r.get_sc_voltage()
        y.append(y0)
        #time.sleep(time_measure)
        print(y0)
        sampl_per.append(time.time()-x0)

plot_voltage_vs_time(3)
plt.figure(figsize=(10,6))
plt.hist(sampl_per)
plt.figure(figsize=(10,6))

plt.plot(x, y)
plt.show()
