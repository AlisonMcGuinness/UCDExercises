import numpy as np
import matplotlib.pyplot as plt


np.random.seed(123)
tries = 500
each_go = 100

all_walks = []
for i in range(tries) :

    # Initialization
    random_walk = [0]

    for x in range(each_go):
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        # clumsiness
        if np.random.rand() <= 0.001:
            step = 0

        random_walk.append(step)
    # use this to show 1 walk
    # plt.plot(random_walk)

    # save the whole walk
    all_walks.append(random_walk)

# plot all walks just to see - apparently this is not right though
# plt.plot(all_walks)
# plt.show()
# plt.clf()
print('all walks norm')
print(all_walks)
print('you have to transpose to get the correct plot - Transpose swaps rows and columns')
np_aw_t = np.transpose(np.array(all_walks))
print('after being transposed')
print(np_aw_t)
plt.clf()
plt.plot(np_aw_t)
#plt.show()

print('to get probability of how likely you are to get to step 60. ')
print('get all the end steps, which is now last row of the array')
ends = np_aw_t[-1,:]
print(ends)

print('best way to show a distribution of values in with a histogram')
print('the hist is not relevant to the calculating probabiltiy, just interesting')
#plt.clf()
#plt.hist(ends)
#plt.show()

print('count how many times you got to 60')
win = len(ends[ends>=60])
print('probability is num of wins over total trys')
prob = win/tries

print(prob)
print('Out of %d tries, we won %d times, so prob is %f' % (tries, win, prob))

