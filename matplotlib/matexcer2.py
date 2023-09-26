import matplotlib.pyplot as plt 
import numpy as np


# # add title , lables and legend
x = np.linspace(-10, 10, 100) # creates 100 values , evenly spread from 0 to 10
y = np.sin(x)  


plt.plot(x,y)
plt.show()