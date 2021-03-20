
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