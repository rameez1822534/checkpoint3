import matplotlib.pyplot as plt
import numpy as np

def create_weight(n):
    return np.random.randint(55, 116, n)

def create_height(n):
    return np.random.uniform(1.45, 2.10, n)

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def create_physique(n):
    weights = create_weight(n)
    heights = create_height(n)
    bmis = calculate_bmi(weights, heights)
    return (weights, heights, bmis)

n = 100
physique_data = create_physique(n)
weights, heights, bmis = physique_data

# Create a scatterplot
plt.figure(figsize=(8, 6))
plt.scatter(heights, weights, c=['red' if bmi > 25 else 'green' for bmi in bmis], marker='o', alpha=0.7)

# Highlight overweight and underweight individuals
plt.scatter([], [], color='red', label='Overweight (BMI > 25)')
plt.scatter([], [], color='green', label='Underweight (BMI < 18.5)')
plt.legend()

plt.grid(True)
plt.show()
