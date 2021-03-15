import numpy as np
print('mat plot lib examples')
# make up fake year and pop lists
np.random.seed(654)
year = [1900]
pop = [np.random.randint(10000,50000000)]
for i in range(100):
    if i == 0:
        continue
    year.append(1900 + (i * 10))
    pop.append(int(pop[-1] / np.random.rand()))
print(year)
print(pop)

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

print('1. LINE PLOT EXAMPLE')
print('pass in 2 lists, x axix, y axix')
# Make a line plot: year on the x-axis, pop on the y-axis
plt.plot(year, pop)

# Display the plot with plt.show()
# plt.show()

print('2. smae but without the lines - a SCATTER PLot')
gdp_cap = []
life_exp = []
for i in range(100):
    gdp_cap.append(np.random.randint(100, 200))
    life_exp.append(np.random.randint(1, 100))
print(gdp_cap)
print(life_exp)
plt.clf()
plt.scatter(gdp_cap, life_exp)
# Put the x-axis on a logarithmic scale
plt.xscale('log')

# Show plot
plt.show()


print('3 HISTOGRAM')
print('use a histogram to show distribution ')
print('range is diveded into bins and graph shows how many results are in each bin')
print(' Too few bins will oversimplify reality and won''t show you the details. ')
print('prToo many bins will overcomplicate reality and won''t show the bigger picture.')
plt.clf()
plt(life_exp, bins=10)

print('customisations!!')
print('lables for x and y')
plt.ylabel('this is the x')
plt.xlabel('this is the life expectency')
print('title')
plt.title('This is a crazy graph')
print('Ticks = values for x and y axis - can use this to make it start at 0')
print(' can also set lables for each tick')
plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90])
plt.yticks([0, 4, 8, 12, 16, 20], ["None", "4 times", "8 times", "12 times", "16 times", "20 times"])

plt.grid(True)
print('put text into the graph at given coordinates')
plt.text(2,2, 'wow')


# Display histogram
plt.show()