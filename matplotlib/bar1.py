import matplotlib.pyplot as plt 
import numpy as np


# Create a scatter plot of random data points 

x = np.random.rand(50)
y = np.random.rand(50)
plt.style.use('Solarize_Light2')
plt.scatter(x, y)

plt.annotate("jag", xy=(0.5,0.5), xytext=(0.6,0.6), arrowprops=dict(arrowstyle = '<->', color='red'))
ax = plt.gca() # get current Axis
ax.spines['top'].set_visible(False) # hide the top spine
ax.spines['bottom'].set_visible(False) # hide the bottom spine
ax.spines['left'].set_visible(False) # hide the left spine
ax.spines['right'].set_visible(False) # hide the right spine
plt.show()
