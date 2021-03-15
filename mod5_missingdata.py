
'''
Missing values are everywhere, and you don't want them interfering with your work.
Some functions ignore missing data by default, but that's not always the behavior you might want.
Some functions can't handle missing values at all,
so these values need to be taken care of before you can use them.
If you don't know where your missing values are, or if they exist,
you could make mistakes in your analysis.

In this exercise, you'll determine if there are missing values in the dataset, and if so, how many.


DO NOT HAVE RIGHT DATA FOR THIS!!

the pickle file will work on the other mod5 exercises instead of the one I made up

the one I made up (from kaggle) is atually the right format for these ones. need to swap around.
'''

import pandas as pd
import matplotlib.pyplot as plt

file = "data\\avocados.csv"
avocados = pd.read_csv(file, sep=',')
# use 2015 as 2016 doesn't have any missing values!
avocados_2016 = avocados[avocados["year"] == 2015]

print('')
print('INSPECT /count missing values in each column')
# Check individual values for missing values
print(avocados_2016.isna())
# Check each column for missing values
print('ANY coluns have null?')
print(avocados_2016.isna().any())
print('TOTAL null values is ')
print(avocados_2016.isna().sum())

# Bar plot of missing values by variable
avocados_2016.isna().sum().plot(kind="bar")
# Show plot
plt.show()

print('')
print('REMOVE missing values')

'''

In this exercise, you'll remove missing values by removing all rows that contain missing values.
Removing observations with missing values is a quick and dirty way to deal with missing data, 
but this can introduce bias to your data if the values are not missing at random.
'''

# Remove all rows that have any missing values
avocados_complete = avocados_2016.dropna()
# Check if any columns contain missing values - these will all be false
print(avocados_complete.isna().any())


print('')
print('OPTION 2 - FILL MISSING VALUES WITH SOMETHING APPROPRIATE')
# From previous step
cols_with_missing = ["small_sold", "large_sold", "xl_sold"]
avocados_2016[cols_with_missing].hist()
plt.show()

# Fill in missing values with 0
avocados_filled = avocados_2016.fillna(0)

# Create histograms of the filled columns
avocados_filled[cols_with_missing].hist()
# Show the plot  distribution changes shape after filling in null values. ????
plt.show()