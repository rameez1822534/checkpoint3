import matplotlib.pyplot as plt

#Data for the bar chart

fruits = ['Bananas' , 'Oranges' , 'Lemons', 'Apples']

number_of_fruits =[15, 24 , 10 , 30]

#Create a bar chart 
bars  = plt.bar(fruits, number_of_fruits, color=['gold', 'orange', 'yellow', 'red' ])

# Add labels and a title
plt.xlabel ('Fruits')
plt.ylabel('Number of fruits')
plt.title ('Fruit consumption')

# plt.show()

colors = ['blue', 'green', 'red', 'purple']

# Create pie chart

plt.pie(number_of_fruits, labels=fruits, colors=colors, autopct='%1.2f%%', startangle=140)
plt.show()