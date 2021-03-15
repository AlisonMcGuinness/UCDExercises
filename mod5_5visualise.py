# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt
import pandas as pd
# file = "C:\\Users\\Admin\\Documents\\UCD_Data\\avocado.csv"
# file = "C:\\Users\\Admin\\PycharmProjects\\UCDExercises\\avocados.csv"


file="data\\avoplotto.pkl"
#avocados = pd.read_csv(file, sep=',')
import pickle
# Open pickle file and load data: d
with open(file, 'rb') as file:
    avocados = pickle.load(file)

print('')
print('BAR GRAPH FROM PANDAS DATASET')
'''
Bar plots are great for revealing relationships between categorical (size) and numeric (number sold) variables, 
but you'll often have to manipulate your data first in order to get the numbers you need for plotting.
'''
# Look at the first few rows of data
print(avocados.head())

# Get the total number of avocados sold of each size
nb_sold_by_size = avocados.groupby("size")['nb_sold'].sum()
print(nb_sold_by_size)
# Create a bar plot of the number of avocados sold by size
print('use .plot method with kind = \'bar\'')
nb_sold_by_size.plot(kind="bar")
# Show the plot
plt.show()

print('')
print('LINE ')
'''
Line plots are designed to visualize the relationship between two numeric variables, 
where each data values is connected to the next one. 
They are especially useful for visualizing the change in a number over time since each time point 
is naturally connected to the next time point. 
In this exercise, you'll visualize the change in avocado sales over three years.
'''
print('.plot with kind = line')
# Get the total number of avocados sold on each date
nb_sold_by_date = avocados.groupby("date")['nb_sold'].sum()
# Create a line plot of the number of avocados sold by date
nb_sold_by_date.plot(kind="line")

# Show the plot
plt.show()
print(' Line plots are great for visualizing something over time')


# Scatter plot of nb_sold vs avg_price with title
print('')
print('SCATTER')
avocados.plot(kind="scatter", x="nb_sold", y="avg_price", title="Number of avocados sold vs. average price")

# Show the plot
plt.show()

print(' scatter to see if 2 measure are corelated - when num sold is higher then prices are lower')

print('2 HISTS')
'''
doc for hist https://www.geeksforgeeks.org/matplotlib-pyplot-hist-in-python/

The alpha property specifies the transparency of the plot. 
0.0 is transparent and 1.0 is opaque. When alpha is set to be 0.5 for both
'''
# Histogram of conventional avg_price
avocados[avocados['type'] == 'conventional']['avg_price'].hist(bins=20, alpha=0.5)

# Histogram of organic avg_price
avocados[avocados['type'] == 'organic']['avg_price'].hist(bins=20, alpha=0.5)

# Add a legend
plt.legend(["Conventional","organic"] )
plt.legend()
# Show the plot
plt.show()