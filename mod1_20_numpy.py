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


# Store weight and height lists as numpy arrays
np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Print out the weight at index 50
print(np_weight_lb[50])


# Print out sub-array of np_height_in: index 100 up to and including index 110
print(np_height_in[100:111])


# Create new arrays for BOOLEAN stuff

my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than 18.5 or smaller than 10
print(np.logical_or(my_house > 18.5, my_house < 10))

# Both my_house and your_house smaller than 11
print(np.logical_and(my_house < 11, your_house < 11))
