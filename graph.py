import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 50)

def f(x):
    return x**2

#y = np.linspace(0, 1, 10)

vec = np.vectorize(f)
y = vec(x)

plt.plot(x, y)
plt.show()
