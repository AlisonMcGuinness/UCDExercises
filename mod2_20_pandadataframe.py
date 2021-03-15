# Import cars data
import pandas as pd
import numpy as np
dir = 'C:\\Users\\Admin\\PycharmProjects\\UCDExercises'
file = 'cars.csv'
cars = pd.read_csv(file, index_col=0)

# cars is a Pandas Data Frame
print(cars)
print(type(cars))

# access values with plain square brackets

print('1. Access values with plain square brackets')
print('eg one or more columns use the labels')
print(cars[['drives_right', 'cars_per_cap']])

print('for one or more rows must SLICE so only consecutive rows')
print(cars[1:4])

print('for subset of data can use i, j notations (row, column')
print('must use lables for the columns')
print(cars[1:3]['country'])


# Print out drives_right value of Morocco
print('square bracket notation is limited so also can use loc and iloc')
print('2. loc is label based access')
print('use row and column lables')

#help(cars.loc)

print('to get rows use row lables')
print(cars.loc[['MOR']])

# Print sub-DataFrame
print('a sub data frame with non consecutive rows and columns')
print(cars.loc[['RU', 'MOR'],['country','drives_right']])


print('3. iloc is same as loc but using indexes')
print('each index must be a slice?? ')
print(cars.iloc[2:4,0:1])
print('or can pass in list of non consec indexes')
print(cars.iloc[[2,4],[0,1]])

print('4. to get ALL a column use : as first paramter to get all rows')
# Print out drives_right column as Series
print('column as a series')
print(cars.loc[:, 'drives_right'])


# Print out drives_right column as DataFrame
print('column as data frame')
print(cars.loc[:,['drives_right']])

print('multi cols as data frame')
# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:,['drives_right', 'cars_per_cap']])


print('FILTERING DATA in PANDAS dataframe')
print(' can pass in a list of booleans to pick out only rows where corresponding boolean is True')
print(' (i) select the column  eg cars[''drives_right'']')
print(' (ii) add the comparison eg cars[''drives_right''] == True - this gives series of booleans')
print(' (iii) use that to index the area to only get the rows with ''True''')
print('  (iv) put all above into one line! eg cars[cars[''drives_right''] == True')

print('eg get all right hand drive ')

# Extract drives_right column as Series: dr
dr = cars['drives_right']
print(dr)
# Use dr to subset cars: sel
sel = cars[dr]
# Print sel
print(sel)
print('or one liner')
print(cars[cars['drives_right']])   # this works becaus the column is already a boolean# so don't need the compare step!

print('check all rows where one col passes filter')
# Create car_maniac: observations that have a cars_per_cap over 500
car_maniac = cars['cars_per_cap'] > 500
# Print car_maniac
print(car_maniac)
print(cars[car_maniac])

print('multiple filters use the numpy logical_and etc methods to concatenate')
# Create medium: observations with cars_per_cap between 100 and 500
medium = cars[np.logical_and(cars['cars_per_cap'] >=100, cars['cars_per_cap'] <=500)]
# Print medium
print(medium)

print('ITERATE OVER Data frame - each row_data is a panda Series')
# Iterate over rows of cars
for row_lable, row_data in cars.iterrows():
    print(row_lable)
    print(row_data)
    print(row_data['country'] + ': ' + str(row_data['cars_per_cap']))

print(' use APPLY method to run the same method on every item in a column')
# Use .apply(str.upper)
cars['COUNTRY'] = cars['country'].apply(str.upper)
print(cars)
print(cars)
