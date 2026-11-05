import i2c_adc as ac
import time
import matplotlib.pyplot as plt
import RPi.GPIO as gpio

mxv = 5.150

r2r = ac.MCP3021(mxv)

time_null = time.time()

time_measure = 0.001

x = []
y = []

sampl_per = []

#print(r2r.get_sc_voltage())

gpio.setmode(gpio.BCM)
gpio.setup(14, gpio.OUT, initial = 0)

gpio.output(14, 0)

while True:
    if r2r.get_voltage()<0.1:
        break
    print("lol", r2r.get_voltage())

gpio.output(14, 1)
time_null_def = time.time()

while (r2r.get_voltage()<3):
    x0 = time.time()-time_null_def
    x.append(x0)
    y0 = r2r.get_voltage()
    y.append(y0)
    #time.sleep(time_measure)
    print(y0)
    #sampl_per.append(time.time()-x0)

gpio.output(14, 0)


while (r2r.get_voltage()>0.5):
    x0 = time.time()-time_null_def
    x.append(x0)
    y0 = r2r.get_voltage()
    y.append(y0)
    #time.sleep(time_measure)
    print(y0)
    #sampl_per.append(time.time()-x0)

plt.figure(figsize=(10,6))

plt.ticklabel_format(style='sci', axis='both', scilimits=(0,0), useMathText = True)

plt.minorticks_on()
plt.grid(visible = True, which = 'major', linestyle='-', linewidth = 1.5, color='0.7')
plt.grid(visible = True, which = 'minor', linestyle='--', linewidth = 1, color='0.8')

plt.xlabel(r"$T, seconds$")
plt.ylabel(r"$U, Volts$")

plt.plot(x, y, label = 'grpah', marker = '', linestyle='-', color = '#ab34cf', linewidth = 1)
plt.show()
