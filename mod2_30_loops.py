import numpy as np
import pandas as pd

print('cheat sheet for loops')

print('loop a fixed number of times')
print('for x in range(3)')
for x in range(3):
    print(x)
print('note it will the loop the number of times specified but starts at 0!!')

print(' ')
print('loop through a dicitionary - note dict is UNSORTED so cannot guarantee what order they will be in')
d = {'key1': 'value 1', 'key2': 'other value', 'key3': 'last value'}
print('for k, v in d.items()  -- NOTE THIS IS METHOD OF DICT')
for k, v in d.items():
    print('key is %s, value is %s' % (k, v))

print('')
print('loop through a list')
print('for x in my_list:')
my_list = ['ha ha', 234, [1, 2], False, 'that''s it folks!']
for x in my_list:
    print(x)

print('')
print('loop through a numpy array - like a list')
print('for x in my_array')
np_arr = np.array([1, 2, 3, 4, 78, 44])
for x in np_arr:
    print(x)

print('')
print('loop through 2d numpy array SLOW')
d2 = np.array([[1, 2, 3, 4, 78, 44], [100, 200, 300, 400, 780, 440]])


for x in d2:
    print(x)
    for y in x:
      print(y)

print('loop through n2 array quick - NOTE THIS IS Np FUNCTION , pass in array')
for x in np.nditer(d2):
    print(x)


print('')
print('loop panda dataframe')

s = pd.array(d2)
print('done')


