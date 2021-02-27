# height and weight are available as a regular lists

# Import numpy
import numpy as np
import random


weight_lb = []
height_in = []

for x in range(1, 1000):
    weight_lb.append(int(random.random()*10))
for x in range(1, 1000):
    height_in.append(int(random.random()*10))
# print(height_in)
# print(weight_lb)
print('Lists are great but numpy arrays are better! You can do calculations on them very efficiently'
      'and pass them into numpy stats methods to easily do stats'
      'All Elements in a numpy array must be the SAME TYPE'
      'numpy arrays behave differently to certain operators eg arr1 + arr2 will ADD all the elements'
      'use a boolean condition to get an ARRAY of booleans for each element!'
      'AND can index a numpy array with an array of booleans to subset')
# Store weight and height lists as numpy arrays
print('create numpy arrays from normal list')
np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Print out the weight at index 50
print('zero index on numpy array')
print(np_weight_lb[50])


# Print out sub-array of np_height_in: index 100 up to and including index 110
print('use a slice to get sub-array ')
print(np_height_in[100:111])

print('apply operator to the whole array eg * 2 - returns a new array')
print(np_height_in[100:111] * 2)


print('use numpy methods to get stats:')
print('np.mean(array) (average')
print(np.mean(height_in))
print('np.median(array) - value in the middle. If not close to mean indicates outliying data')
print(np.median(np_height_in))
print('np.corrcoef(array) - ??')
print(np.corrcoef(np_height_in))
print('np.std(array)  - standard deviation ')
print(np.std(np_height_in))

print('Also can efficiently sum and sort - quicker than using a list')

print(np.sum(np_height_in))
print(np.sort(np_height_in[0:11]))
# Create new arrays for BOOLEAN stuff

my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

print('apply boolean operator to the array to get a new array of booleans')
print(my_house > 18.5)

print('then select all elements that match')
print(my_house[my_house > 18.5])
# my_house greater than 18.5 or smaller than 10

print('use np_logical_X to combine and/ or conditions')
print(np.logical_or(my_house > 18.5, my_house < 10))

# Both my_house and your_house smaller than 11
print(np.logical_and(my_house < 11, your_house < 11))
