import matplotlib.pyplot as plt 
import numpy as np


def x2(x):
    return x**2

x = np.linspace(-10, 10, 100)
y = x2(x)
plt.plot(x,y)

plt.show()
