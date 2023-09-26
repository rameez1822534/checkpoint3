import pandas as pd
import matplotlib.pyplot as plt

# Specify the full path to the CSV file
csv_file_path = 'C:\\module visualization\\matplotlib\\London 2012 Olympic alternative medal rankings - ALL.csv'

# Read the CSV file into a DataFrame (must be located in the correct folder)
df = pd.read_csv(csv_file_path) #header = 0 uses the first row as column names

df['Total Medals'] = df['Gold'] + df['Silver'] + df['Bronze']  # Calculate total medals
df = df.sort_values(by='Total Medals', ascending=False)  # Sort by total medals
top_10_df = df.head(10) 

plt.figure(figsize=(12, 6))

x_values = top_10_df['Country name']  # Use 'Country' column as x-axis labels
y_gold = top_10_df['Gold']
y_silver = top_10_df['Silver']
y_bronze = top_10_df['Bronze']

plt.barh(x_values, y_gold, color='gold', label='Gold')
plt.barh(x_values, y_silver, color='silver', label='Silver', left=y_gold)
plt.barh(x_values, y_bronze, color='#cd7f32', label='Bronze', left=y_gold + y_silver)

plt.xlabel('Number of Medals')
plt.ylabel('Countries')
plt.title('Medals by Country')
plt.legend()
plt.tight_layout()
plt.show()
