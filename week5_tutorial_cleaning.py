# This is notes from tutorial week 5 with examples for cleaning data
# similar to mod5_missingdata.py
# this code does not run - just need some sample data.
import pandas as pd

pd.set_option('display.max_columns', 20)
pd.set_option('display.width',2000)

data = pd.read_csv("filename")

print(data.head(), data.shape)
print(data.info()) # shows type of each col and how many are not missing

missing_val = data.isnull()
missing_val = data.isna() # SAME!

print(missing_val.isna().any())


print(missing_val)	# this is matching data fram with True for all null values
print(missing_val.sum())

# PLOT THE NUMBER OF MISSING VALUES FOR EACH COLUM!
data.isna().sum().plot(kind="bar")
plt.show()

# OPTION 1 - drop the rows and/or cols that have missing values
# drop Not available = dropna() method on dataframe
new_data = data.dropna() 	# will drop rows or cols (default rows)
# this will drop any rows that have any missing value
new_data = data.dropna(axis=1)  # will drop any cols with missing values
# dropping the data might cause you to lose too much data.

# OR you can fill the null values
new_data = data.fillna(value)

# this will fill every null value with the mean of the column - good for number values
new_data = data.fillna(data.mean())

# also other parameters to fillna - bfill will use value before see docs
# can string fillna to gether to catch all
new_data = data.fillna(method="bfill).fillna(method="ffill")
# There are loads of sophisticated ways of filling in missing data using fillna() method
# see documentation for details.

# www.pandas.pydata.org
new_data = data.drop_duplicates(subset=["type","director","title"])

