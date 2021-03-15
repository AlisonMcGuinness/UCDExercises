import pandas as pd

file = "C:\\Users\\Admin\\Documents\\UCD_Data\\temp.csv"
temperatures = pd.read_csv(file, sep=",", parse_dates=['date'])
temperatures['avg_temp_c'] = temperatures['temperature']

# Look at temperatures
print(temperatures.info())

# Index temperatures by city
temperatures_ind = temperatures.set_index('city')


# Look at temperatures_ind
'''
Setting an index allows more concise code for subsetting for rows of a categorical variable via .loc[].
'''
print(temperatures_ind)

# Reset the index, keeping its contents
print(temperatures_ind.reset_index())

# Reset the index, dropping its contents
print(temperatures_ind.reset_index(drop=True))

# Make a list of cities to subset on
cities = ["Moscow", "Saint Petersburg"]

# Subset temperatures using square brackets
print(temperatures[temperatures['city'].isin( cities)])

# Subset temperatures_ind using .loc[]
# pass list of cities OR use double [[]] and pass direct
print(temperatures_ind.loc[cities].head())

print('')
print('multiple indexes')
'''
Setting multi-level indexes
Indexes can also be made out of multiple columns, 
forming a multi-level index (sometimes called a hierarchical index). 
There is a trade-off to using these.

The benefit is that multi-level indexes make it more natural to reason about nested categorical variables.
 For example, in a clinical trial, you might have control and treatment groups. 
 Then each test subject belongs to one or another group, and we can say that a test subject 
 is nested inside the treatment group. 
 Similarly, in the temperature dataset, the city is located in the country, 
 so we can say a city is nested inside the country.

The main downside is that the code for manipulating indexes is different 
from the code for manipulating columns, 
so you have to learn two syntaxes and keep track of how your data is represented.


'''
# Index temperatures by country & city
temperatures_ind = temperatures.set_index(["country", "city"])

# List of tuples: Brazil, Rio De Janeiro & Pakistan, Lahore
rows_to_keep = [("Brazil", "Rio De Janeiro"), ("Pakistan", "Lahore")]
rows_to_keep = [("Russia", "Moscow")]

# Subset for rows to keep  THIS CRAShES IF THE values in rows to keep do not exist in the index.
print(temperatures_ind.loc[rows_to_keep].head())

print('')
print('sorting by index examples')
'''
Sorting index values is similar to sorting values in columns,
 except that you call .sort_index() instead of .sort_values().

'''
# Sort temperatures_ind by index values
print(temperatures_ind.sort_index())
# Sort temperatures_ind by index values at the city level
print(temperatures_ind.sort_index(level = ["city"]))
# Sort temperatures_ind by country then descending "city
print(temperatures_ind.sort_index(level = ["country", "city"], ascending=[True, False]))

print('')
print('SLICING INDEX ROWS')
'''

Slicing index values
Slicing lets you select consecutive elements of an object using first:last syntax. 
DataFrames can be sliced by index values or by row/column number; 
we'll start with the first case. This involves slicing inside the .loc[] method.

Compared to slicing lists, there are a few things to remember.

You can only slice an index if the index is sorted (using .sort_index()).
To slice at the outer level, first and last can be strings.
To slice at inner levels, first and last should be tuples.
If you pass a single slice to .loc[], it will slice the rows.

'''

# Sort the index of temperatures_ind
temperatures_srt = temperatures_ind.sort_index()

# Subset rows from Pakistan to Russia
print(temperatures_srt.loc["Pakistan":"Russia"])

# Try to subset rows from Lahore to Moscow
#print(temperatures_srt.loc["Lahore":"Moscow"])

# Subset rows from Pakistan, Lahore to Russia, Moscow
print(temperatures_srt.loc[("Pakistan", "Lahore"):("Russia", "Moscow")])

print('')
print('Slicking in both directions')
'''
Slicing in both directions
You've seen slicing DataFrames by rows and by columns, 
but since DataFrames are two-dimensional objects, 
it is often natural to slice both dimensions at once. 
That is, by passing two arguments to .loc[], you can subset by rows and columns in one go.
'''
# Subset rows from India, Hyderabad to Iraq, Baghdad
print(temperatures_srt.loc[("India", "Hyderabad"):("Iraq","Baghdad")])

# Subset columns from date to avg_temp_c
print(temperatures_srt.loc[:, "date":"avg_temp_c"])

# Subset in both directions at once
print(temperatures_srt.loc[("India", "Hyderabad"):("Iraq","Baghdad"), "date":"avg_temp_c"])

print('')
print('Slicing TIME SERIES')
'''
Slicing is particularly useful for time series since it's a common thing to want to filter for 
data within a date range. Add the date column to the index, 
then use .loc[] to perform the subsetting. 
The important thing to remember is to keep your dates in ISO 8601 format, that is, yyyy-mm-dd.

Recall from Chapter 1 that you can combine multiple Boolean conditions using logical operators 
(such as &). To do so in one line of code, you'll need to add parentheses () around each condition.

Using .loc[] in conjunction with a date index 
provides an easy way to subset for rows before or after some date.
'''
print('without an index! ')
# Use Boolean conditions to subset temperatures for rows in 2010 and 2011
temperatures_bool = temperatures[(temperatures["date"] >= "2010-01-01") & (temperatures["date"] <= "2011-12-31")]
print(temperatures_bool)
print('with an index!!')
# Set date as an index and sort the index
temperatures_ind = temperatures.set_index("date").sort_index()
# Use .loc[] to subset temperatures_ind for rows in 2010 and 2011
print(temperatures_ind.loc["2010":"2011"])
# Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb 2011
print(temperatures_ind.loc["2010-08":"2011-02"])

print('')
print('USING ILOC')
# Get 23rd row, 2nd column (index 22, 1)
print(temperatures.iloc[22:23, 1:2])

# Use slicing to get the first 5 rows
print(temperatures.iloc[:5])

# Use slicing to get columns 3 to 4
print(temperatures.iloc[:,2:5])

# Use slicing in both directions at once
print(temperatures.iloc[:5,2:5])


print('')
print('pivot by city and year')
# Add a year column to temperatures
temperatures["year"] = temperatures["date"].dt.year
# Pivot avg_temp_c by country and city vs year
temp_by_country_city_vs_year = temperatures.pivot_table(values="avg_temp_c", index=["country","city"], columns="year")
# See the result
print(temp_by_country_city_vs_year)

print('')
print('can slice the pivot table same as usual')
# Subset for Egypt to India
print(temp_by_country_city_vs_year.loc["Egypt":"India"])

# Subset for Egypt, Cairo to India, Delhi
print(temp_by_country_city_vs_year.loc[("Egypt","Cairo"):("India", "Delhi")])

# Subset in both directions at once
print(temp_by_country_city_vs_year.loc[("Egypt","Cairo"): ("India", "Delhi"), "2005":"2010"])

print('')
print('calculating on a pivot table')
'''
Pivot tables are filled with summary statistics, but they are only a first step to finding 
something insightful. 
Often you'll need to perform further calculations on them. 
A common thing to do is to find the rows or columns where the highest or lowest value occurs.

Recall from Chapter 1 that you can easily subset a Series or DataFrame to find rows of interest 
using a logical condition inside of square brackets. For example: series[series > value].

'''
# Get the worldwide mean temp by year
mean_temp_by_year = temp_by_country_city_vs_year.mean()
print(mean_temp_by_year)

# Filter for the year that had the highest mean temp
print(mean_temp_by_year[mean_temp_by_year == mean_temp_by_year.max()])

# Get the mean temp by city
mean_temp_by_city = temp_by_country_city_vs_year.mean(axis = "columns")
print(mean_temp_by_city)

# Filter for the city that had the lowest mean temp
print(mean_temp_by_city[mean_temp_by_city == mean_temp_by_city.min()])