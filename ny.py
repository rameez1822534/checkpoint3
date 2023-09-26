import matplotlib.pyplot as plt 
import numpy as np

#fig = plt.figure() # empty figure 

#plt.show() # you have to show your plot

# x1 = 1 
# y1 = 1
# x2 = 5
# y2 = 5
# x3 = 3
# y3 = -2

# x_values = np.array([x1 , x2, x3])
# y_values = np.array([y1 , y2, y3])

# plt.plot(x_values , y_values, marker = "$❤️$")
# plt.show()

# add title , lables and legend
x = np.linspace(0, 10 , 100) # creates 100 values , evenly spread from 0 to 10
y1 = np.sin(x)  
y2 = np.cos(x)

plt.figure(figsize=(8,6)) # inches . 1 inch about spread from 0 to 10 

plt.plot(x, y1, label = 'Sine' , color='red', linestyle = '-', marker = 's')
plt.plot(x, y2, label = 'Cosine' , color='green', linestyle = '--', marker = 'o')

#add a legend
plt.legend(loc = 'upper right')

# add a title and labels for the x and y axis 
plt.title('Sine and Cosine Curves', fontsize = 24)
plt.xlabel('X-axis', fontsize = 20)
plt.ylabel('Y-axis', fontsize = 20)


# Add add grid(show grid)
plt.grid(True)

plt.show()