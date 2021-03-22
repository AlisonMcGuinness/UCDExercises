
import numpy as np
import pandas as pd

gdp = pd.read_csv('data\\WorldBank_GDP.csv', delimiter=',')
sp500 = pd.read_csv('data\\S&P500.csv', delimiter=',')
pop = pd.read_csv('data\\WorldBank_POP.csv', delimiter=',')

print(gdp.head())
print(gdp.info())
print(sp500.head())
print(sp500.info())
print('')
print('MERGE ORDERED')
print(' the results are in order (of whatever they aare merged ON?) = good if you have time sequenced data and you want ')
print(' to use fill forward or fill back - the fill will only make sense if the data is in the right order')
print(' see example with pop and gdp later on')
print('dataset.corr()  returns a matrix of correlations of each column to every other columns. whatever that means.')
'''
You can see the different aspects of merge_ordered() and how you might use it on data that can be ordered. 
By using this function, you were able to fill in the missing data from 2019. 
Finally, the correlation of 0.21 between the GDP and S&P500 is low to moderate at best. 
You may want to find another predictor if you plan to play in the stock market
'''
# Use merge_ordered() to merge gdp and sp500, interpolate missing value
gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on='year', right_on='date',
                             how='left',  fill_method='ffill')

# Subset the gdp and returns columns
gdp_returns = gdp_sp500[['gdp', 'returns']]

# Print gdp_returns correlation
print(gdp_returns.corr())


print('')
print(' merge_ordered orders by the ON column')
print('see example here of ordering by 2 cols and see how result changes when you switch cols.')
'''
THIS IS VERY IMPORTANT FOR THE FORWARD or Backward FILL!!!

When you merge on date first, the table is sorted by date then country. 
When forward fill is applied, Sweden's population value in January is used to fill in the 
missing values for both Australia and the Sweden for the remainder of the year. 
This is not what you want. 
The fill forward is using unintended data to fill in the missing values. 

However, when you merge on country first, the table is sorted by country then date, 
so the forward fill is applied appropriately in this situation.

but could the pop for one contry be forward filled to first value for next country? says me

'''

# Merge gdp and pop on date and country with fill and notice rows 2 and 3
print(gdp.head())
print(pop.head())
ctry_date = pd.merge_ordered(gdp, pop, on=["year", "country name"],
                             fill_method='ffill')

# Print ctry_date
print('')
print('This is merged on YEAR then country name:')
print(ctry_date)
print('')

# Merge gdp and pop on country and date with fill
date_ctry = pd.merge_ordered(gdp, pop, on=["country name", "year"], fill_method="ffill")

# Print date_ctry
print('this is merged on country name, then year')
print(date_ctry)
print('')

print('')
print('MERGE_ASOF')
'''
this can be used to do fuzzy matching, particularly for time orderd data
works same as merge_ordered  but it matches on the mearest key column and
not exact matches
the dataframes must be already sorted by the column you are merging ON.
direction = 'forwards', 'backwards' 'nearest' can control how the data is matched.

The critical point here is that the merge_asof() function is very useful 
in performing the fuzzy matching between the timestamps of all the tables.
'''
# Use merge_asof() to merge jpm and wells
jpm_wells = pd.merge_asof(jpm, wells, on='date_time',
                          suffixes=('', '_wells'), direction='nearest')

# Use merge_asof() to merge jpm_wells and bac
jpm_wells_bac = pd.merge_asof(jpm_wells, bac, on='date_time',
                              suffixes=('_jpm', '_bac'), direction='nearest')

# Compute price diff
price_diffs = jpm_wells_bac.diff()

# Plot the price diff of the close of jpm, wells and bac only
price_diffs.plot(y=['close_jpm','close_wells','close_bac'])
plt.show()

print('')
print('using merge_asof function to create a data set')
'''
The merge_asof() function can be used to create datasets where you have a table of start and stop dates, 
and you want to use them to create a flag in another table. You have been given gdp, 
which is a table of quarterly GDP values of the US during the 1980s. 
Additionally, the table recession has been given to you. 
It holds the starting date of every US recession since 1980, and the date 
when the recession was declared to be over. 
Use merge_asof() to merge the tables and create a status flag 
if a quarter was during a recession. Finally, to check your work, plot the data in a bar chart.

'''
# Merge gdp and recession on date using merge_asof()
gdp_recession = pd.merge_asof(gdp, recession, on="date")

# gdp is 2 cols date and gdp
# recesssion is 2 cols date and econ_status
# gdp_recession is all he gdp rows with the econ_status set to the econ status of nearest date that matches.
# Create a list based on the row value of gdp_recession['econ_status']
is_recession = ['r' if s=='recession' else 'g' for s in gdp_recession['econ_status']]

# Plot a bar chart of gdp_recession
# Note you can pass in a LIST of colors for the color paramter, should be one item in the list
# for each row in the data frame?
gdp_recession.plot(kind="bar", y="gdp", x="date", color=is_recession, rot=90)
plt.show()


print('')
print('QUERY function')
print('just one of the many methods for selecting data from table')
'''
ust use .query(querystring)
where the query strin gis like what is after the WHERE clause in sql
eg .query('col1 == "abc" and col2 > 100')
'''
# Merge gdp and pop on date and country with fill
gdp_pop = pd.merge_ordered(gdp, pop, on=['country','date'], fill_method='ffill')

# Add a column named gdp_per_capita to gdp_pop that divides the gdp by pop
gdp_pop['gdp_per_capita'] = gdp_pop['gdp'] / gdp_pop['pop']

# Pivot data so gdp_per_capita, where index is date and columns is country
gdp_pivot = gdp_pop.pivot_table('gdp_per_capita', 'date', 'country')

# Select dates equal to or greater than 1991-01-01
recent_gdp_pop = gdp_pivot.query('date >= "1991-01-01"')

# Plot recent_gdp_pop
recent_gdp_pop.plot(rot=90)
plt.show()


print('')
print('MELT method')
'''
converts data from WIDE (one row for each subject)
to LONG/TALL - one row for each subject for each attribute 

In general, data is often provided (especially by governments) 
in a format that is easily read by people but not by machines. 
The .melt() method is a handy tool for reshaping data into a useful form.
'''
# unpivot everything besides the year column
# ur_wide has 1 row for each Year with cols with unemplyrate for each month so cols - Jan, feb, Mar, April etc that hold the un
#print(ur_wide.head())

ur_tall = ur_wide.melt(id_vars=['year'], var_name='month', value_name='unempl_rate')
print(ur_tall)
# ur_tall now has col for Year, variable col (called Month) and value col called unempl_rate.

# Create a date column using the month and year columns of ur_tall
ur_tall['date'] = pd.to_datetime(ur_tall['year'] + '-' + ur_tall['month'])

# Sort ur_tall by date in ascending order
ur_sorted = ur_tall.sort_values('date')

# Plot the unempl_rate by date
ur_sorted.plot(x='date', y='unempl_rate')
plt.show()

'''
another obscure melt example on data that I don't have and don't understand
# Use melt on ten_yr, unpivot everything besides the metric column
bond_perc = ten_yr.melt(id_vars=['metric'], var_name='date', value_name='close')

# Use query on bond_perc to select only the rows where metric=close
bond_perc_close = bond_perc.query('metric == "close"')

# Merge (ordered) dji and bond_perc_close on date with an inner join
dow_bond = pd.merge_ordered(dji, bond_perc_close, on="date", how="inner", suffixes=('_dow', '_bond'))

print(dow_bond)
# Plot only the close_dow and close_bond columns
dow_bond.plot(y=['close_dow', 'close_bond'], x='date', rot=90)
plt.show()
'''

'''
There is an economic theory developed by A. W. Phillips which states that inflation and unemployment 
have an inverse relationship. 
The theory claims that with economic growth comes inflation, which in turn should lead 
to more jobs and less unemployment.

You will take two tables of data from the U.S. Bureau of Labor Statistics, 
containing unemployment and inflation data over different periods, and create a Phillips curve. 
The tables have different frequencies. 
One table has a data entry every six months, while the other has a data entry every month. 
You will need to use the entries where you have data within both tables.

The tables unemployment and inflation have been loaded for you.
Oh no they haven't.


# Use merge_ordered() to merge inflation, unemployment with inner join
inflation_unemploy = pd.merge_ordered(inflation, unemployment, how="inner")

# Print inflation_unemploy
print(inflation_unemploy)

# Plot a scatter plot of unemployment_rate vs cpi of inflation_unemploy
inflation_unemploy.plot(kind="scatter", x = "unemployment_rate", y="cpi")
plt.show()

data looked like this
            date      cpi     seriesid                  data_type  unemployment_rate
    0  2014-01-01  235.288  CUSR0000SA0  SEASONALLY ADJUSTED INDEX                6.7
    1  2014-06-01  237.231  CUSR0000SA0  SEASONALLY ADJUSTED INDEX                6.1
    2  2015-01-01  234.718  CUSR0000SA0  SEASONALLY ADJUSTED INDEX                5.6
    3  2015-06-01  237.684  CUSR0000SA0  SEASONALLY ADJUSTED INDEX                5.3
    4  2016-01-01  237.833  CUSR0000SA0  SEASONALLY ADJUSTED INDEX                5.0
    5  2016-06-01  240.167  CUSR0000SA0  SEASONALLY ADJUSTED INDEX                4.9
    6  2017-01-01  243.780  CUSR0000SA0  SEASONALLY ADJUSTED INDEX                4.7
    7  2017-06-01  244.182  CUSR0000SA0  SEASONALLY ADJUSTED INDEX                4.3
    8  2018-01-01  248.884  CUSR0000SA0  SEASONALLY ADJUSTED INDEX                4.1
    9  2018-06-01  251.134  CUSR0000SA0  SEASONALLY ADJUSTED INDEX                4.0

There are critics of the curve, but what is more important in this example 
is that you were able to use entries where you had entries in both tables by using an inner join. 
You might ask why not use the default outer join and use forward fill to fill to estimate 
the missing variables. 
You might choose differently. In this case, instead of showing an estimated unemployment rate 
(which is a continually changing measure) for five periods, 
that data was dropped from the plot.    
'''