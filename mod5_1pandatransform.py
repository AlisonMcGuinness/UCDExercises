import pandas as pd


print('Basic pandas examples')
print('df.head()   - show first 5 rows')
print('df.info()   - names and types of columns plus how many filled in each')
print('df.shape   - how many rows and cols')
print('df.describe()  - summary stats for eery numerical column')

print('')
print('Data frame components  (attributes)')
print('df.values  - all the data in a 2d numpy array')
print('df.columns  - Index object, list of column names')
print('df.index  - INdex object - all the row numbers or row lables.')

# dummy up some data and put it in dataframe
data = [['Leinster','Dublin', 1010,500,62000],
        ['Munster','Cork', 8700,550,15000],
        ['Leinster','Meath', 4000,600,25000],
        ['Leinster','Wicklow', 5500,650,12000],
        ['Leinster', 'Wexford', 7100,700,350000],
        ['Munster','Kerry', 10340,750,403400],
        ['Connaught','Mayo', 9123,800,40470]]

homelessness = pd.DataFrame(data)
homelessness.columns = ['region', 'state', 'individuals', 'family_members', 'state_pop']

print(homelessness.values)


print('')
print('SORTING data frames')
print('sort by 1 col asc or desc')
# Sort homelessness by descending family members
homelessness_fam = homelessness.sort_values('family_members', ascending=False)
# Print the top few rows
print(homelessness_fam.head())

print('sort by multiple columms in differetn asc/desc orders')
# Sort homelessness by region, then descending family members
homelessness_reg_fam = homelessness.sort_values(['region','family_members'], ascending = [True,False])
# Print the top few rows
print(homelessness_reg_fam.head())

print('')
print('SUBSETTING dataframes')
'''
Subsetting columns
When working with data, you may not need all of the variables in your dataset. 
Square brackets ([]) can be used to select only the columns 
that matter to you in an order that makes sense to you. 
To select only "col_a" of the DataFrame df, use

df["col_a"]
To select "col_a" and "col_b" of df, use

df[["col_a", "col_b"]]
'''

# Select the individuals column
individuals = homelessness["individuals"]
# Print the head of the result
print(individuals.head())
# Select the state and family_members columns
# NOTE DOUBLE SQUARE BRACKETS!
state_fam = homelessness[['state','family_members']]
# Print the head of the result
print(state_fam.head())

print('')
print('SUBSETTING ROWS')
'''
Subsetting rows
A large part of data science is about finding which bits of your dataset are interesting.
One of the simplest techniques for this is to find a subset of rows that match some criteria. 
This is sometimes known as filtering rows or selecting rows.

There are many ways to subset a DataFrame, perhaps the most common is to use relational 
operators to return True or False for each row, then pass that inside square brackets.

dogs[dogs["height_cm"] > 60]
dogs[dogs["color"] == "tan"]
You can filter for multiple conditions at once by using the "bitwise and" operator, &.

dogs[(dogs["height_cm"] > 60) & (dogs["color"] == "tan")]
'''
print('ONE FILTER')
# Filter for rows where individuals is greater than 10000
ind_gt_10k = homelessness[homelessness['individuals'] > 10000]
# See the result
print(ind_gt_10k)

print('multi condition filters')
fam_lt_1k_pac = homelessness[(homelessness['family_members'] > 1000) & (homelessness['region'] == 'Pacific')]
# See the result
print(fam_lt_1k_pac)

print('')
print('subset rows based on categoyr')
'''
Subsetting rows by categorical variables
Subsetting data based on a categorical variable often involves 
using the "or" operator (|) to select rows from multiple categories. 
This can get tedious when you want all states 
in one of three different regions, for example. 
Instead, use the .isin() method, which will allow you to tackle this problem 
by writing one condition instead of three separate ones.

colors = ["brown", "black", "tan"]
condition = dogs["color"].isin(colors)
dogs[condition]
'''
print('SUBSET using is in example')
# Subset for rows in South Atlantic or Mid-Atlantic regions
south_mid_atlantic = homelessness[homelessness['region'].isin(['Munster', 'Connaught'])]

# See the result
print(south_mid_atlantic)

print('')
print('TRANSFORMING datasets')
print('otherwise known as adding columns')
print('if your data set doesn\'t have the cols you want you can create them from the existing cols')
# Add total col as sum of individuals and family_members
homelessness["total"] = homelessness["individuals"] + homelessness["family_members"]
# Add p_individuals col as proportion of individuals
homelessness['p_individuals'] = homelessness['individuals'] /homelessness['total']
# See the result
print(homelessness)

print('COMBINE EVERYTHING')
# Create indiv_per_10k col as homeless individuals per 10k state pop
homelessness["indiv_per_10k"] = 10000 * homelessness['individuals'] / homelessness['state_pop']

# Subset rows for indiv_per_10k greater than 20
high_homelessness = homelessness[homelessness['indiv_per_10k'] > 20]

# Sort high_homelessness by descending indiv_per_10k
high_homelessness_srt = high_homelessness.sort_values('indiv_per_10k', ascending=False)

# From high_homelessness_srt, select the state and indiv_per_10k cols
result = high_homelessness_srt[['state','indiv_per_10k']]

# See the result
print(result)