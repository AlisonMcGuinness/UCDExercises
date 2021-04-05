import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

'''
see docs here for good info on FacetGrid and PairGrid
https://seaborn.pydata.org/tutorial/axis_grids.html#grid-tutorial
'''

print('PairGrid')
'''
similar to facetgrid
It’s important to understand the differences between a FacetGrid and a PairGrid. 
In the former, each facet shows the same relationship conditioned on 
different levels of other variables. 
In the latter, each plot shows a different relationship 
(although the upper and lower triangles will have mirrored plots). 
Using PairGrid can give you a very quick, very high-level summary of interesting 
relationships in your dataset.
'''

df = pd.read_csv('data9\\carinsurance.csv')
# Create the same PairGrid but map a histogram on the diag
g = sns.PairGrid(df, vars=["fatal_collisions", "premiums"])
g2 = g.map_diag(plt.hist)
g3 = g2.map_offdiag(plt.scatter)

plt.show()
plt.clf()
'''
This analysis provides useful insight into the distribution of premium amounts as well 
as the limited relationships between fatal_collision and premiums.
Really??? But what does the fatal collistions historgram show??? I don't understand it.

look at carinsurance.csv  - each row is a summary data for ONE state
so each row has one number for fatal collisisions. so the histogram tells us??
confusing that it is same scale on x and y but on one x it must be number of collisions 
and y is number of states that have that number of collisions?
'''

# Same as above but with pairplot
# Create a pairwise plot of the variables using a scatter plot
sns.pairplot(data=df,
        vars=["fatal_collisions", "premiums"],
        kind='scatter')

plt.show()
plt.clf()


# same again but with more fancy options
# Plot the same data but use a different color palette and color code by Region
sns.pairplot(data=df,
        vars=["fatal_collisions", "premiums"],
        kind='scatter',
        hue='Region',
        palette='RdBu',
        diag_kws={'alpha':.5})  # transparency

plt.show()
plt.clf()

'''
Additional pairplots
This exercise will go through a couple of more examples of how the pairplot() can be customized 
for quickly analyzing data and determining areas of interest that might be worthy of additional analysis.

One area of customization that is useful is to explicitly define the x_vars and y_vars 
that you wish to examine. 
Instead of examining all pairwise relationships, 
this capability allows you to look only at the specific interactions that may be of interest.

We have already looked at using kind to control the types of plots. 
We can also use diag_kind to control the types of plots shown on the diagonals. 
In the final example, we will include a regression and kde plot in the pairplot.
'''
# This has te x vars on the x axis and y on the y so you
# don't have the plots with the same var against itself.
# Build a pairplot with different x and y variables
sns.pairplot(data=df,
        x_vars=["fatal_collisions_speeding", "fatal_collisions_alc"],
        y_vars=['premiums', 'insurance_losses'],
        kind='scatter',
        hue='Region',
        palette='husl')

plt.show()
plt.clf()

# and another basic one with different kinds of plot on the diagonals
# what is a kde plot - Kernal Density Estimate  - no idea what this is.
# plot relationships between insurance_losses and premiums
sns.pairplot(data=df,
             vars=["insurance_losses", "premiums"],
             kind='reg',
             palette='BrBG',
             diag_kind = 'kde',
             hue='Region')

plt.show()
plt.clf()