import seaborn as sns
import matplotlib.pyplot as plt
'''

Scatter plots are important in statistics because they can show the extent of correlation,
if any, between the values of observed quantities or phenomena (called variables).
If no correlation exists between the variables, the points appear randomly scattered
on the coordinate plane.

Scatter plots show how much one variable is affected by another. 
The relationship between two variables is called their correlation . ... 
The closer the data points come when plotted to making a straight line, 
the higher the correlation between the two variables, or the stronger the relationship.


Seaborn
built on top of matplotlib - to make it easy to use the flexibilty of matplotlib but taking
away some of the complexity
'''

print('SCATTER PLOT EXAMPLE')
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

all_countries = pd.read_csv('data8\\countries-of-the-world.csv', decimal=",")
gdp = all_countries['gdp']
percent_literate = all_countries['percent_literate']
phones = all_countries['phones']
#print(gdp)
#print(phones)
#print(percent_literate)
# Change this scatter plot to have percent literate on the y-axis
sns.scatterplot(x=gdp, y=percent_literate)

# Show plot
plt.show()

sns.scatterplot(x=gdp, y=phones)
plt.show()
'''
if you put phones on the y axis, tere is kind of a diagonal line pattern of dots which show a correleation
when you put literacy on the y axis most of dots are at the top in a straight line - this is explained as:
While this plot does not show a linear relationship between GDP and percent literate, 
countries with a lower GDP do seem more likely to have a lower percent of the population 
that can read and write.
'''

print('')
print(' COUNT PLOT')
'''
Count plots take in a categorical list and return bars that represent the 
number of list entries per category. 
You can create one here using a list of regions for each country,
'''
region = all_countries['region']
# Create count plot with region on the y-axis
sns.countplot(y=region)

# Show plot
plt.show()

print('using seaborn with PANDAS more examples')
'''
Note you can use a data frame with countplot() by passing in the column NAME
AND the dataframe like this..
BUT ONLY IF DATA IS TIDY _ EG ONE ROW PER OBSERVATION, ONE COLUMN PER VARIABLE

but surely this is just the same as passing in the column from the dataframe directly?
try it and see is there any difference?
'''

df = pd.read_csv('data8\\young-people-survey-responses.csv')
# Create a count plot with "Spiders" on the x-axis
#sns.countplot(x='Spiders', data=df)

# Display the plot
#plt.show()
# is it the same if you do this?? YES IT IS!
#sns.countplot(df['Spiders'])
#plt.show()

print('')
print('Addng a third variable with HUE (color!)')
student_data = pd.read_csv('data8\\student-alcohol-consumption.csv')
# Change the legend order in the scatter plot
sns.scatterplot(x="absences", y="G3",
                data=student_data,
                hue="location", hue_order=['Rural','Urban'])

# Show plot
'''
It looks like students with higher absences tend to have lower grades in both rural and urban areas.
DOES IT REALLY??? I don't think so.
'''
plt.show()

'''
COlors on a COUNTPLOT  - if you add hue then it splits bars to show count for each var 
Students at GP tend to come from an urban location, 
but students at MS are more evenly split. Congratulations on finishing Chapter 1!
'''
# Create a dictionary mapping subgroup values to colors
palette_colors = {"Rural": "green", "Urban": "blue"}

# Create a count plot of school with location subgroups
sns.countplot(x="school", data=student_data, hue="location", palette=palette_colors)

# Display plot
plt.show()

print('')
print(' RELATIONAL PLOTS')
print(' relplot() method can be used to create any plot, just pass in kind="scatter" or "line" ')
'''
Because these subplots had a large range of x values, 
it's easier to read them arranged in rows instead of columns.
'''
# Change to make subplots based on study time
sns.relplot(x="absences", y="G3",
            data=student_data,
            kind="scatter",
            row="study_time") # this creates a sub plot for each value in the 'study_time' col

# Show plot
plt.show()
print('subdivide by 2 sepaarate col vlaues on row and col')
print('i guess this works best if there are yes/no, true/false values in both cols so you get 2x2 grid')
sns.relplot(x="G1", y="G3",
            data=student_data,
            kind="scatter",
            col="schoolsup",
            col_order=["yes", "no"],
            row="famsup",
            row_order=['yes', 'no'])

# Show plot
'''
It looks like the first semester grade does correlate with the final grade, 
regardless of what kind of support the student received.
'''
plt.show()

print('')
print('MORE CUSTOMISATIONS eg SIZE')
'''
What is the difference between quantitative and categorical variables?
Quantitative variables are any variables where the data represent amounts 
(e.g. height, weight, or age).

Categorical variables are any variables where the data represent groups. 
This includes rankings (e.g. finishing places in a race), classifications 
(e.g. brands of cereal), and binary outcomes (e.g. coin flips).

for scatterplot and relplot you can set size="column name"  and this will change 
the size of the point on the graph. Works best if column name is quantative OR categorical
that represents level of something
'''
# setting the size and hue to same col makes the graph clearer - the larger vlaues are bigger and darker
# Create scatter plot of horsepower vs. mpg
mpg = pd.read_csv('data8\\mpg.csv')
sns.relplot(x="horsepower", y="mpg",
            data=mpg, kind="scatter",
            size="cylinders", hue="cylinders")
# Show plot
plt.show()

# use the style customisation to change teh style of each point,
# again is good to use with hue to make it clearer
# Create a scatter plot of acceleration vs. mpg
sns.relplot(x="acceleration", y="mpg", kind="scatter", data=mpg, style="origin", hue="origin")

# Show plot
'''
Cars from the USA tend to accelerate more quickly and get lower miles per gallon 
compared to cars from Europe and Japan.
'''
plt.show()