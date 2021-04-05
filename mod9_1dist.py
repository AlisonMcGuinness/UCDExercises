import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


rents = pd.read_csv('data9\\fairrent2018.csv')
df = pd.read_csv('data9\\carinsurance.csv')
awards = pd.read_csv('data9\\grants.csv')
print('Intermediate Seaborn')

print('distplot - just pass on one column to get distribution - just like df[col].plot.hist()')
'''
distplot will calculated Gaussian Kernal Density Estimate (KDE)
'''

# Display a Seaborn distplot
sns.distplot(awards['Award_Amount'])
plt.show()

# Clear the distplot
plt.clf()

# Create a distplot
sns.distplot(awards['Award_Amount'],
             kde=False, # disable the KDE line, this just makes a hist plot
             bins=20,  # set number of bins
             hist=False,
             rug=True,  # shows values underneath?? shows how the values are distributed?
             kde_kws={'shade': True})  # can pass in customisation properties for the kde??

'''
A rug plot is like a histogram with zero width bins.
it's a one-d display that you can add to existing plos
'''
# Display the plot
plt.show()

print('')
print('Regression Plots (regplot')
'''
Regression lines, or best fit lines, are a type of annotation on scatterplots 
that show the overall trend of a set of data. .
Linear regression is a statistical method for modeling the relationship between two variables. 
The method works well with scatterplots because scatterplots show two variables. 
The resulting line from a linear regression analysis can be plotted on a 
scatterplot of the same data and shows the general trend of the data. 
The goal of linear regression is to create a mathematical model 
so one can predict the value of Y when the value of X is known.

While regression lines are most often seen on scatter plots, 
they are also compatible with bar charts and column charts with time ordered bars, and line charts.
'''

print('regplot is the basic version')
# Create a regression plot of premiums vs. insurance_losses
sns.regplot(data=df, x="insurance_losses", y ="premiums")

# Display the plot
plt.show()

print('lmplot is the more powerful version that allow faceting with row, col, hue etc')
# this will do the exact same graph but we can add more customisations to lmplot!
sns.lmplot(data=df, x="insurance_losses", y ="premiums",
           hue="Region",  # add regression line for each region on same plot
           # row="Region" # add a separate plot for each region on different rows.

           )
print('')
print('more palette examples')
for p in ['bright', 'colorblind']:
    sns.set_palette(p)
    sns.distplot(rents['fmr_3'])
    plt.show()

    # Clear the plots
    plt.clf()

print('make your own palettes')
# sequential
sns.palplot(sns.color_palette("Purples", 8))
# kind of random?
sns.palplot(sns.color_palette("husl", 10))
# diverging
sns.palplot(sns.color_palette("coolwarm", 6))  # or "BrGr" brown to green?
'''
Color palette possibilities are limitless. 
Using these helper functions will allow you to create unique and visually appealing plots that will stand out and get your points across.
'''

'''
Using the underlying matplotlib methods to customiste your seaborn plot
if you get the fig. ax first from plt
then pass the axes into seaborn,
then use all the customisations available on Axes to style it up
'''
# Create a figure and axes. Then plot the data
fig, ax = plt.subplots()
sns.distplot(rents['fmr_1'], ax=ax)

# Customize the labels and limits
ax.set(xlabel="1 Bedroom Fair Market Rent", xlim=(100,1500), title="US Rent")

# Add vertical lines for the median and mean
ax.axvline(x=rents['fmr_1'].median(), color='m', label='Median', linestyle='--', linewidth=2)
ax.axvline(x=rents['fmr_1'].mean(), color='b', label='Mean', linestyle='-', linewidth=2)

# Show the legend and plot the data
ax.legend()
plt.show()
'''
For the final exercise we will plot a comparison of the fair market rents for 1-bedroom and 
2-bedroom apartments.
'''

# Create a plot with 1 row and 2 columns that share the y axis label
fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2, sharey=True)

# Plot the distribution of 1 bedroom apartments on ax0
sns.distplot(rents['fmr_1'], ax=ax0)
ax0.set(xlabel="1 Bedroom Fair Market Rent", xlim=(100,1500))

# Plot the distribution of 2 bedroom apartments on ax1
sns.distplot(rents['fmr_2'], ax=ax1)
ax1.set(xlabel="2 Bedroom Fair Market Rent", xlim=(100,1500))

# Display the plot
plt.show()

