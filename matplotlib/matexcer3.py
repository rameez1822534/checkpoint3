import matplotlib.pyplot as plt 
import numpy as np

# x1 = 1 
# y1 = 1
# x2 = 3
# y2 = 5
# x3 = 2
# y3 = -2
# x4 = 1
# y4 = 5
# x5 = 5
# y5 = 3

x = np.array([0, 1, 2, -0.5, 2.5, 0])
y = np.array ([0, 1,0, 0.6, 0.6, 0])
plt.plot(x,y ,color='red')
plt.plot(x , y , marker= 'o', color='k', linestyle='None')
plt.title("Twisted little star with markers")

plt.show()