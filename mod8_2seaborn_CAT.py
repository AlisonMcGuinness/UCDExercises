import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

print('')
print(' CAT PLOT')
print('for plotting categorical values')

'''
categorical values are those which have a fixed (usally small) number of values 
eg survey results with fixed options, days of week, etc

we have seen countplot - shows the NUMBEr OF observations in each category (only one value)
barplot - looks ike countplot but is showing mean of a quantitive variable for each category (2 values)

Now we see sns.catplot(kind='count', xxxx)
just like relplot expands scatter plot,  catplot expands countplot??
can easily do subplots and confidence intervals - 
use the row and col parameters to create sub plots based on those values

CATplot is a CATagorical plot - shows the distribution of a quantative variable within
categories defined by a catagorical variable.
bar, count, box and point plots are all types of CATEGORICAL plots

Add third variable either with hue - to show in differetn colour on same plot
OR row, col parameters to create muliple plots on same graphi
'''


survey_data = pd.read_csv('data8\\young-people-survey-responses.csv')
# note np.where !!! make new column based on conditionn
# if you try to do if else  on the the existing column you get this error
# ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all()
survey_data['Age Category'] = np.where(survey_data['Age'] <=21, 'Less than 21', 'Over 21')

# Create column subplots based on age category
sns.catplot(y="Internet usage", data=survey_data,
            kind="count",col="Age Category")

# Show plot
plt.show()

print('cat plot to create a bar plot')
'''
As a reminder, we'll create a bar plot using the catplot() function, 
providing the name of categorical variable to put on the x-axis (x=____), 
the name of the quantitative variable to summarize on the y-axis (y=____), 
the Pandas DataFrame to use (data=____), and the type of categorical plot (kind="bar").
'''
print(survey_data['Interested in Math'].mean())
# Create a bar plot of interest in math, separated by gender
sns.catplot(kind='bar', data=survey_data, x='Gender', y='Interested in Math')
# Show plot
plt.show()
student_data = pd.read_csv('data8\\student-alcohol-consumption.csv')
print('')
print(' another example, can set the oder of the bars')
''' in this one each bar is the mean grade result gotten by all studnets in that category'''
# Turn off the confidence intervals
sns.catplot(x="study_time", y="G3",
            data=student_data,
            kind="bar",
            order=["<2 hours",
                   "2 to 5 hours",
                   "5 to 10 hours",
                   ">10 hours"],
                  ci=None)
# Show plot
plt.show()

print('')
print(' use catplot() to make box plots')
'''
https://dataschool.com/fundamentals-of-analysis/what-is-an-outlier/
'''
# Specify the category ordering
study_time_order = ["<2 hours", "2 to 5 hours",
                    "5 to 10 hours", ">10 hours"]

# Create a box plot and set the order of the categories
sns.catplot(kind='box', order=study_time_order, x='study_time', y='G3', data=student_data)
plt.show()
print(' using catplot allows you to do sub plots based on a third value' )
# Create a box plot with subgroups and omit the outliers
sns.catplot(x='internet', y='G3', data=student_data, kind='box', col='location', hue='location', sym='')
# Show plot
'''
The median grades are quite similar between each group, 
but the spread of the distribution looks larger among students who have internet access.
'''
plt.show()

print(' WHISKERS')
'''
The whiskers are the lines out of the box. and the tails are the end of the whiskers
by default the whiskers extend to 1.5 * IQR (Inter Quartile Range) and the outliers are the values
outside of that
YOu can control the whiskers with whis parater
'''
# Extend the whiskers to the 5th and 95th percentile
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box",
            whis=0.5)  # change to 0.5 * IQR
# whis=[5,95]  to extend to 5th and 95th percentile
# whis=[0, 100] will extend to the min and max values (so there will be no outliers)

# Show plot
plt.show()

print('')
print('POINT PLOTS')
'''
As a reminder, to create a point plot, use the catplot() function and specify the 
name of the categorical variable to put on the x-axis (x=____), 
the name of the quantitative variable to summarize on the y-axis (y=____), 
the Pandas DataFrame to use (data=____), and the type of categorical plot (kind="point").
'''
# Remove the lines joining the points
sns.catplot(x="famrel", y="absences",
            data=student_data,
            kind="point",
            capsize=0.2,  # add lines to end of confidence interval lines
            join=False)  # don't join up the points
# Also can set ci=None to remove confidence interval
# Aso can set esimate=np.median  to use the median instead of mean (better if lots of outliers)
'''
While the average number of absences is slightly smaller among students with higher-quality 
family relationships, the large confidence intervals tell us that we can't be 
sure there is an actual association here.
'''

# Show plot
plt.show()

# Plot the median number of absences instead of the mean
sns.catplot(x="romantic", y="absences",
			data=student_data,
            kind="point",
            hue="school",
            ci=None,
            estimator=np.median)

# Show plot
plt.show()

print('')
print('more customisations')
print('change plot style and colour')

# Change the color palette to "RdBu"
sns.set_style("whitegrid")  # also dark, darkgrid, ticks, white (default) and whitegrid
sns.set_palette("RdBu")  # loads of diverting and sequential palettes availalbe see sheets also can customise

# Set a custom color palette
#sns.set_palette(["#39A7D0","#36ADA4"])
'''
Each context name gives Seaborn's suggestion on when to use a given plot scale 
(in a paper, in an iPython notebook, in a talk/presentation, or in a poster session).
'''
sns.set_context('poster')

# Create a count plot of survey responses
category_order = ["Never", "Rarely", "Sometimes",
                  "Often", "Always"]

sns.catplot(x="Parents Advice",
            data=survey_data,
            kind="count",
            order=category_order)

# Show plot
plt.show()

'''
So far, we've looked at several things in the dataset of survey responses from young people, 
including their internet usage, how often they listen to their parents, and how many of them report feeling lonely. 
However, one thing we haven't done is a basic summary of the type of people answering this survey, 
including their age and gender. 
*** Providing these basic summaries is always a good practice when dealing with an unfamiliar dataset.
'''
print('')
print('titles')
'''
any plot that can create multiple plots is a FacetGrid
any plot that is just a single plot is an AxesSubplot
different ways to set title on each.

eg FacetGrid (relplot, catplot)

g = sns.relplot(xxx)
g.fig.suptitle('Car Weight vs. Horsepower')

eg AxesSubPlot ( scatterplot, lineplot, countplot etc)
g = sns.scatterplot(xxx)
g.set_title('abc')

Setting X and Y axis lables  (Same for both)

# Add x-axis and y-axis labels
g.set(xlabel='Car Model Year', ylabel='Average MPG')

# rotate labels (same for both - use matplotlib method)
# Rotate x-tick labels
plt.xticks(rotation=90)
'''
