import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print('FacetGrid')
'''
Building a FacetGrid
Seaborn's FacetGrid is the foundation for building data-aware grids. 
A data-aware grid allows you to create a series of small plots that 
can be useful for understanding complex data relationships.

For these exercises, we will continue to look at the College Scorecard Data 
from the US Department of Education. 
This rich dataset has many interesting data elements that we can plot with Seaborn.

When building a FacetGrid, there are two steps:

1. Create a FacetGrid object with columns, rows, or hue.
2. Map individual plots to the grid.
'''
df = pd.read_csv('data9\\scores.csv')
# Create FacetGrid with Degree_Type and specify the order of the rows using row_order
g2 = sns.FacetGrid(df,
            row="Degree_Type",
             row_order=['Graduate', 'Bachelors', 'Associates', 'Certificate'])

# Map a pointplot of SAT_AVG_ALL onto the grid
g2.map(sns.pointplot, 'SAT_AVG_ALL')

# Show the plot
plt.show()
plt.clf()
print('factorplot()')
'''
factorplot() is shortcut to do above in ONE line of code
'''
# Create a factor plot that contains boxplots of Tuition values
sns.factorplot(data=df,
         x='Tuition',
         kind='box',
         row='Degree_Type')

plt.show()
plt.clf()

degree_ord = ['Graduate', 'Bachelors', 'Associates', 'Certificate']
# Create a facetted pointplot of Average SAT_AVG_ALL scores facetted by Degree Type
sns.factorplot(data=df,
        x='SAT_AVG_ALL',
        kind='point',
        row='Degree_Type',
        row_order=degree_ord)

plt.show()
plt.clf()

print('lmplot')
'''
Using a lmplot
The lmplot is used to plot scatter plots with regression lines on FacetGrid objects. 
The API is similar to factorplot with the difference that the default behavior of lmplot 
is to plot regression lines.

For the first set of exercises, we will look at the Undergraduate population (UG) 
and compare it to the percentage of students receiving Pell Grants (PCTPELL).

For the second lmplot exercise, we can look at the relationships between Average SAT scores 
and Tuition across the different degree types and public vs. non-profit schools.
'''

# Create a FacetGrid varying by column and columns ordered with the degree_order variable
g = sns.FacetGrid(df, col="Degree_Type", col_order=degree_ord)

# Map a scatter plot of Undergrad Population compared to PCTPELL
g.map(plt.scatter, 'UG', 'PCTPELL')

plt.show()
plt.clf()
# use lmplot for the same as above but with extra fancy stuff.
# Create an lmplot that has a column for Ownership, a row for Degree_Type and hue based on the WOMENONLY column
sns.lmplot(data=df,
        x='SAT_AVG_ALL',
        y='Tuition',
        col="Ownership",
        row='Degree_Type',
        row_order=['Graduate', 'Bachelors'],
        hue='WOMENONLY',
        col_order=['Public', 'Private non-profit'])

plt.show()
plt.clf()
'''
 Creating small multiples of plots is very useful for many types of analysis. 
 With Seaborn, it is easy to use the plot types to quickly perform complex visualizations.
 '''