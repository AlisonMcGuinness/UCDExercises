import pandas as pd
import numpy as np


file = "stores.tsv"
file = "C:\\Users\\Admin\\Documents\\UCD_Data\\stores.tsv"
sales = pd.read_csv(file, sep='\t', comment='#', na_values=['Nothing'])
# Print the first element of data
'''
Note problems with KeyErrors - it looked like columns were all correct but
there must have been spaces in the column namess. I had to edit tsv file and make
sure only tabs between the data this fixed it.
'''
# Print the info about the sales DataFrame
print('explore dataframe')
print(sales.info())
print(sales.head())

print('')
print('use summary methods')

# Print the mean of weekly_sales
print('the mean is %s' % str(sales['weekly_sales'].mean()))

# Print the median of weekly_sales
print(' the median is %s' % str(sales['weekly_sales'].median()))
print('also mode, min, max, var, std, sum and others')
'''
The mean weekly sales amount is almost double the median weekly sales amount! 
This can tell you that there are a few very high sales weeks that are making 
the mean so much higher than the median.
'''
'''
Summary statistics can also be calculated on date columns 
that have values with the data type datetime64. 
Some summary statistics — like mean — don't make a ton of sense on dates, 
but others are super helpful, for example, minimum and maximum, 
which allow you to see what time range your data covers.
'''
print('')
print('summary stats on DATE cols.')
# Print the maximum of the date column
print('the latest date is %s' % sales['date'].max())
# Print the minimum of the date column
print('the earliest date is %s' % sales['date'].min())

'''
While pandas and NumPy have tons of functions, sometimes, you may need a different function to 
summarize your data.

The .agg() method allows you to apply your own custom functions to a DataFrame, 
as well as apply functions to more than one column of a DataFrame at once, 
making your aggregations super-efficient. 

For example,

In the custom function for this exercise, "IQR" is short for inter-quartile range, 
which is the 75th percentile minus the 25th percentile. 
It's an alternative to standard deviation that is helpful if your data contains outliers.
'''
print('')
print(' Custom functions using agg method - can use multiple functions on multiple columns')

# A custom IQR function
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)

# Print IQR of the temperature_c column
print(sales['temperature_c'].agg(iqr))

# Update to print IQR of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg(iqr))
# Update to print IQR and median of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg([iqr, np.median]))
'''
The .agg() method makes it easy to compute multiple statistics on multiple columns, all in just one line of code.
'''
print('')
print('cumulative methods return a whole data column')
# Sort sales_1_1 by date
sales_1_1 = sales.sort_values('date')

# Get the cumulative sum of weekly_sales, add as cum_weekly_sales col
sales_1_1['cum_weekly_sales'] = sales_1_1['weekly_sales'].cumsum()

# Get the cumulative max of weekly_sales, add as cum_max_sales col
sales_1_1['cum_max_sales'] = sales_1_1['weekly_sales'].cummax()

# See the columns you calculated
print(sales_1_1[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]])

print('')
print('counting step 1 drop duplicate')
# Drop duplicate store/type combinations
store_types = sales.drop_duplicates(subset=['store', 'type'])
print(store_types.head())

# Drop duplicate store/department combinations
store_depts = sales.drop_duplicates(subset=['store','department'])
print(store_depts.head())

# Subset the rows where is_holiday is True and drop duplicate dates
holiday_dates = sales[sales['is_holiday']].drop_duplicates(subset = 'date')

# Print date col of holiday_dates
print(holiday_dates['date'])

print('counting step 2 actually count. normalise and sort. WHAT IS NORMALISE')
print('value_counts gives you the counts but if you set normalise to true you get the proportion out of the total')
print('all the normalised numbers add up to 1')
# Count the number of stores of each type
store_counts = store_types['type'].value_counts()
print(store_counts)

# Get the proportion of stores of each type
store_props = store_types['type'].value_counts(normalize = True)
print(store_props)

# Count the number of each department number and sort
dept_counts_sorted = store_depts['department'].value_counts(sort=True)
print(dept_counts_sorted)

# Get the proportion of departments of each number and sort
dept_props_sorted = store_depts['department'].value_counts(sort=True, normalize=True)
print(dept_props_sorted)