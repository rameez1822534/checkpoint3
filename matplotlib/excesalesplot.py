import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Specify the full path to the CSV file
csv_file_path = 'C:\\module visualization\\matplotlib\\forsaljning.csv'

# Read the CSV file into a DataFrame (must be located in the correct folder)
df = pd.read_csv(csv_file_path) #header = 0 uses the first row as column names

plt.figure(figsize=(6, 4)) 

x_values = df['Manad']
y_2019 = df['2019']
y_2020 = df['2020']
y_2021 = df['2021']

highest_value = max(y_2019)
lowest_value = min(y_2019)

# Create a list of colors for each data point in y_2019
colors = ['green' if value == highest_value else 'red' if value == lowest_value else 'black' for value in y_2019]

# Plot the 2019 data with conditional coloring
for i in range(len(x_values)):
    plt.bar(x_values[i], y_2019[i], label='2019', color=colors[i], alpha=0.7)
    
plt.plot(x_values, y_2020, label='2020', alpha=0.7)
plt.plot(x_values, y_2021, label='2021', alpha=0.7)
plt.legend(['2019', '2020', '2021'])
plt.show()
