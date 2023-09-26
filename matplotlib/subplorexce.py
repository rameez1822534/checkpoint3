import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Specify the full path to the CSV file
csv_file_path = 'C:\\module visualization\\matplotlib\\forsaljning.csv'

# Read the CSV file into a DataFrame (must be located in the correct folder)
df = pd.read_csv(csv_file_path) #header = 0 uses the first row as column names

plt.figure(figsize=(12, 6))  # Set the figure size

# Manad = list(calendar.month_abbr)[1:]
# Create subplots for each year
plt.subplot(131)  # 1 row, 3 columns, subplot 1
plt.bar(df['Manad'], df['2019'], label='2019', color='blue')
plt.title('Year 2019')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.legend()

plt.subplot(132)  # 1 row, 3 columns, subplot 2
plt.plot(df['Manad'], df['2020'], label='2020', color='red')
plt.title('Year 2020')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.legend()

plt.subplot(133)  # 1 row, 3 columns, subplot 3
plt.plot(df['Manad'], df['2021'], label='2021', color='black')
plt.title('Year 2021')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.legend()

plt.tight_layout()  # Adjust spacing between subplots
plt.show()