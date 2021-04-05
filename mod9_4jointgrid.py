import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print('JointGrid')
'''
Building a JointGrid and jointplot
Seaborn's JointGrid combines univariate plots such as histograms, rug plots and kde plots 
with bivariate plots such as scatter and regression plots. 
The process for creating these plots should be familiar to you now. 
These plots also demonstrate how Seaborn provides convenient functions 
to combine multiple plots together.
'''

df = pd.read_csv('data9\\dcbikes.csv')
# Build a JointGrid comparing humidity and total_rentals
sns.set_style("whitegrid")
g = sns.JointGrid(x="hum",
            y="total_rentals",
            data=df,
            xlim=(0.1, 1.0))

g.plot(sns.regplot, sns.distplot)

plt.show()
plt.clf()

# Same as above but use jointplot()
# Create a jointplot similar to the JointGrid
sns.jointplot(x="hum",
        y="total_rentals",
        kind='reg',
        data=df)

plt.show()
plt.clf()
'''
These plots show that there is limited relationship between rental amounts and humidity levels.
'''

'''
Jointplots and regression
Since the previous plot does not show a relationship between humidity and rental amounts, 
we can look at another variable that we reviewed earlier. 
Specifically, the relationship between temp and total_rentals.
'''

# Plot temp vs. total_rentals as a regression plot
sns.jointplot(x="temp",
         y="total_rentals",
         kind='reg',
         data=df,
         order=2,
         xlim=(0, 1))

plt.show()
plt.clf()
# then do the same plot but as a residual plot to show the appropriateness of the model
# Plot a jointplot showing the residuals
sns.jointplot(x="temp",
        y="total_rentals",
        kind='resid',
        data=df,
        order=2)

plt.show()
plt.clf()
# This shows there is a positive relationship between temperature and total_rentals.?

'''
Complex jointplots
The jointplot is a convenience wrapper around many of the JointGrid functions. 
However, it is possible to overlay some of the JointGrid plots on top of the standard jointplot. 
In this example, we can look at the different distributions for riders 
that are considered casual versus those that are registered.
'''
# Create a jointplot of temp vs. casual riders
# Include a kdeplot over the scatter plot
g = (sns.jointplot(x="temp",
                   y="casual",
                   kind='scatter',
                   data=df,
                   marginal_kws=dict(bins=10, rug=True))
     .plot_joint(sns.kdeplot))

plt.show()
plt.clf()

# and the same for the registered users
# Replicate the above plot but only for registered riders
g = (sns.jointplot(x="temp",
             y="registered",
             kind='scatter',
             data=df,
             marginal_kws=dict(bins=10, rug=True))
    .plot_joint(sns.kdeplot))

plt.show()
plt.clf()


'''
Got It!
1. Selecting Seaborn Plots
We have covered a lot of different plots in Seaborn. The final section of this course will bring all of the concepts together and give you a framework for deciding when to use each Seaborn plot.

2. Seaborn plot map
We will reinforce the previous lessons by showing how these plot types fit together. The power of Seaborn is the way that the different plots build on each other. For instance, a kdeplot can be used on its own or it can be generated from a distplot(). In addition, the PairGrid() and JointGrid() plots build on top of the regression and distribution plots. Let's explore this in more detail and discuss guidelines on how to approach using Seaborn in your daily data science workflow.

3. Univariate Distribution Analysis
One of the first steps in analyzing numerical data is looking at its distribution. Seaborn's distplot() combines many of the features of the rugplot(), kdeplot(), and matplotlib histogram into a single function. The distplot() function is the best place to start when trying to do distribution analysis with Seaborn.

4. Regression Analysis
A regression plot is an example of a plot that shows the relationship between two variables. matplotlib's scatter() plot is a very simple method to compare the interaction of two variables on the x and y-axis. The lmplot() combines many of these features of the underlying regplot() and residplot() in addition to the ability to plot the data on a FacetGrid(). In many instances, lmplot() is the best function to use for determining linear relationships between data.

5. Categorical Plots
Seaborn has many types of categorical plots as well. In most scenarios, it makes sense to use one of the categorical plots such as the boxplot() or violinplot() to examine the distribution of the variables. Then, follow up with the statistical estimation plots such as the point, bar, or countplot. If you need to facet the data across rows or columns, use a factorplot().

6. pairplot() and jointplot()
The pairplot() and jointplot() visualizations are going to be most useful after you have done some preliminary analysis of regressions or distributions of the data. Once you are familiar with the data, the pairplot() and jointplot() can be very useful in understanding how two or more variables interact with each other.

7. Thank You!
Congratulations on completing the course. You are now familiar with the Seaborn library and can start to incorporate it into your own data analysis tasks!

'''