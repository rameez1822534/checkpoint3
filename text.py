import matplotlib.pyplot as plt
import pandas as pd

# Load the data from the CSV file
df = pd.read_csv("forsaljning.csv")

# Create subplots for each year
fig, axes = plt.subplots(3, 1, figsize=(8, 12), sharex=True)

# Year 2019
axes[0].plot(df['Manad'], df['2019'], label='2019', color='blue', alpha=0.7)
axes[0].set_ylabel('Sales')
axes[0].legend()

# Year 2020
axes[1].plot(df['Manad'], df['2020'], label='2020', color='red', alpha=0.7)
axes[1].set_ylabel('Sales')
axes[1].legend()

# Year 2021
axes[2].plot(df['Manad'], df['2021'], label='2021', color='green', alpha=0.7)
axes[2].set_xlabel('Month')
axes[2].set_ylabel('Sales')
axes[2].legend()

plt.tight_layout()
plt.show()
