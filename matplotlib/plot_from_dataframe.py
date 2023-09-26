import pandas as pd
import matplotlib.pyplot as plt
import os

# Specify the full path to the CSV file
csv_file_path = 'C:\\module visualization\\matplotlib\\forsaljning.csv'

# Read the CSV file into a DataFrame (must be located in the correct folder)
df = pd.read_csv(csv_file_path) #header = 0 uses the first row as column names

# Display the DataFrame
plt.subplot(2, 2, 1)
plt.plot(df['Manad'],df['2019'],color='red')
plt.title('Försäljning 2019')

plt.subplot(2, 2, 2)
plt.plot(df['Manad'],df['2020'],color='green')
plt.title('Försäljning 2020')

plt.subplot(2, 2, 3)
plt.plot(df['Manad'],df['2021'],color='k') 
plt.title('Försäljning 2021')

plt.subplot(2, 2, 4)
plt.plot(df['Manad'],df['2019'],color='red')
plt.plot(df['Manad'],df['2020'],color='green')
plt.plot(df['Manad'],df['2021'],color='k') 
plt.title('Försäljning 2019, 2020, 2021')

plt.tight_layout()

plt.show()

# We could use months instead of df['Manad']
# months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','okt','nov','dec']


# - bars
plt.bar(df['Manad'],df['2019'],color='k')
plt.bar(df['Manad'][7],df['2019'][7],color='green')
plt.bar(df['Manad'][9],df['2019'][9],color='red')
plt.xlabel("månader")
plt.ylabel("Försäljning i kronor (kr)")
plt.title("Försäljning 2019")


plt.show()


# Show how we can stack bar charts by using bottom=:

plt.bar(df['Manad'],df['2019'],color='gold', label='2019')
plt.bar(df['Manad'],df['2020'],color='silver', bottom = df['2019'], label='2020') # bottom is on top of 2019
plt.bar(df['Manad'],df['2021'],color='brown', bottom = df['2019'] + df['2020'] , label='2021') # bottom is on top of 2019+2020
plt.legend(loc = 'upper right')


plt.show()