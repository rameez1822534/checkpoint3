import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = x 
y4 = x**2

plt.figure(figsize=(6, 4))  # 6 inches wide and 4 inches high

# Subplots
plt.subplot(2, 2, 1)
plt.plot(x, y1, color='blue')
plt.title('Sine Curve')

plt.subplot(2, 2, 2)
plt.plot(x, y2, color='red')
plt.title('Cosine Curve')

plt.subplot(2, 2, 3)
plt.plot(x, y3, color='purple')
plt.title('Linear Function')

plt.subplot(2, 2, 4)
plt.plot(x, y4, color='green')
plt.title('Quadratic Function')

# Adjust spacing between subplots
plt.tight_layout()

# Add a common title for the entire figure
plt.suptitle('Subplots with Titles', fontsize=16)

# Adjust subplots to 80% of the height from the bottom
plt.subplots_adjust(top=0.8, left=0.2)

plt.show()
