# Import cars data
import pandas as pd
dir = 'C:\\Users\\Admin\\PycharmProjects\\UCDExercises'
file = ''
cars = pd.read_csv(dir + '\\cars.csv', index_col=0)

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