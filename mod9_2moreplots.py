import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


rents = pd.read_csv('data9\\fairrent2018.csv')
df = pd.read_csv('data9\\carinsurance.csv')
awards = pd.read_csv('data9\\grants.csv')

print('3 types of categorical plot')
'''
1. Strip plot and SWArm plot
show every single observation
'''
# Create the stripplot
sns.stripplot(data=awards,
         x='Award_Amount',
         y='Model Selected',
         jitter=True)

plt.show()

# Create and display a swarmplot with hue set to the Region
sns.swarmplot(data=awards,
         x='Award_Amount',
         y='Model Selected')
# add hue='Region' to futher break down by different color dots for each region

plt.show()


print('')
print('2. Boxplot, voilinplot and lvplot')
'''
these allshow statistical estimates
boxplot - as per chap 8 - shows mean 25%, 75% and outliers
violin - uses Kernal Density - more sophisticated but intensive for big data
lvplot (letter value)  - mix between the above, runs well on large data sets

Seaborn's categorical plots also support several abstract representations of data. 
The API for each of these is the same 
so it is very convenient to try each plot and see if the data lends itself to one over the other.
'''

# Create a boxplot
sns.boxplot(data=awards,
         x='Award_Amount',
         y='Model Selected')

plt.show()
plt.clf()

# Create a violinplot with the husl palette
sns.violinplot(data=awards,
         x='Award_Amount',
         y='Model Selected',
         palette='husl')

plt.show()
plt.clf()
'''
# Create a lvplot with the Paired palette and the Region column as the hue
sns.lvplot(data=awards,
         x='Award_Amount',
         y='Model Selected',
         palette='Paired',
         #hue='Region'  # if you want to subgroup by Region
           )

plt.show()

plt.clf()
'''
print('')
print('3. bar, point and count')
'''
The final group of categorical plots are barplots, pointplots and countplot 
which create statistical summaries of the data. 
The plots follow a similar API as the other plots and 
allow further customization for the specific problem at hand
'''
# Show a countplot with the number of models used with each region a different color
sns.countplot(data=awards,
         y="Model Selected",
         hue="Region")

plt.show()
plt.clf()

# Create a pointplot and include the capsize in order to show caps on the error bars
sns.pointplot(data=awards,
         y='Award_Amount',
         x='Model Selected',
         capsize=.1)

plt.show()
plt.clf()

# Create a barplot with each Region shown as a different color
sns.barplot(data=awards,
         y='Award_Amount',
         x='Model Selected',
         hue="Region")

plt.show()
plt.clf()


print('REGRESSION')
'''
Regression and residual plots
Linear regression is a useful tool for understanding the relationship between numerical variables. 
Seaborn has simple but powerful tools for examining these relationships.

For these exercises, we will look at some details from the US Department of Education 
on 4 year college tuition information and see if there are any interesting insights 
into which variables might help predict tuition costs.
A residual is the difference between the observed y-value (from scatter plot) 
and the predicted y-value (from regression equation line). 
It is the vertical distance from the actual plotted point to the point on the regression line. ... 
The plot will help you to decide on whether a linear model is appropriate for your data.
Ideally, residual values should be equally and randomly spaced around the horizontal axis.
'''
df = pd.read_csv('data9\\scores.csv')
# Display a regression plot for Tuition
sns.regplot(data=df,
         y='Tuition',
         x="SAT_AVG_ALL",
         marker='^',
         color='g')

plt.show()
plt.clf()
# Display the residual plot
sns.residplot(data=df,
          y='Tuition',
          x="SAT_AVG_ALL",
          color='g')

plt.show()
plt.clf()

'''
Regression plot parameters
Seaborn's regression plot supports several parameters that can be used to configure 
the plots and drive more insight into the data.
In this data set, each University has some percentage of students that receive these grants. 
Since this data is continuous, 
using x_bins can be useful to break the percentages 
into categories in order to summarize and understand the data.
'''
# Plot a regression plot of Tuition and the Percentage of Pell Grants
sns.regplot(data=df,
            y='Tuition',
            x="PCTPELL",
            x_bins=5,
            order=2)  # use a 2nd order polynomial to draw the line (instead of linear/straightline)

plt.show()
plt.clf()

print('BINS')
'''
Binning data
When the data on the x axis is a continuous value, it can be useful to break it into different bins 
in order to get a better visualization of the changes in the data.

For this exercise, we will look at the relationship between tuition 
and the Undergraduate population abbreviated as UG in this data. 
We will start by looking at a scatter plot of the data and examining 
the impact of different bin sizes on the visualization.
'''

# Create a scatter plot by disabling the regression line
sns.regplot(data=df,
            y='Tuition',
            x="UG",
            fit_reg=False)

plt.show()
plt.clf()

# Create a regplot and bin the data into 8 bins
sns.regplot(data=df,
         y='Tuition',
         x="UG",
         x_bins=8)  # try 5 as well

plt.show()
plt.clf()

print('')
print('HEAT MAPS')
'''
Creating heatmaps
A heatmap is a common matrix plot that can be used to graphically summarize the relationship 
between two variables. 
For this exercise, we will start by looking at guests of the Daily Show from 1999 - 2015 and see how the occupations of the guests have changed over time.

The data includes the date of each guest appearance as well as their occupation. 
For the first exercise, we need to get the data into the right format for 
Seaborn's heatmap function to correctly plot the data. 
All of the data has already been read into the df variable.
'''

df = pd.read_csv('data9\dailyguests.csv')
# Create a crosstab table of the data
print(df)
pd_crosstab = pd.crosstab(df["Group"], df["YEAR"])
print(pd_crosstab)

# Plot a heatmap of the table
# sns.heatmap(pd_crosstab)


# Plot a heatmap of the table with no color bar and using the BuGn palette
# cbar is the LEGEND - why would you hide this?
sns.heatmap(pd_crosstab, cbar=False, cmap="BuGn", linewidths=0.3)
# fmt='d'   show as decimal
# annot = True - show the value on the square
# centre!!


# Rotate tick marks for visibility
plt.yticks(rotation=0)
plt.xticks(rotation=90)

plt.show()


