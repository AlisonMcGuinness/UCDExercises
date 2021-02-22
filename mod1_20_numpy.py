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

