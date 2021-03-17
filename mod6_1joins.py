import pandas as pd



print('' )
print('INNER JOIN with merge() method')
# Merge the taxi_owners and taxi_veh tables setting a suffix
taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid', suffixes=('_own','_veh'))
# Print the value_counts to find the most popular fuel_type
print(taxi_own_veh['fuel_type'].value_counts())

'''
NOTE tha merge() only returns row where there is a mathcing value in both dataframes
if there is no match then row is skipped
'''

print('')
print(' one to many join')
print('exact same syntax')
# Merge the licenses and biz_owners table on account
# license can have multiple owners
licenses_owners = licenses.merge(biz_owners, on="account")
print(licenses_owners.groupby("title"))
# Group the results by title then count the number of accounts
counted_df = licenses_owners.groupby("title").agg({'account':'count'})
# Sort the counted_df in descending order
sorted_df = counted_df.sort_values("account", ascending = False)

# Use .head() method to print the first few rows of sorted_df
print(sorted_df.head())


print('')
print('multiple joins - just concategnate')
'''
ridership is station id, date, num rides
cal is date, and type
stations is station id and station name
'''
# Merge the ridership, cal, and stations tables
ridership_cal_stations = ridership.merge(cal, on=['year','month','day']) \
							.merge(stations, on='station_id')

# Create a filter to filter ridership_cal_stations
filter_criteria = ((ridership_cal_stations['month'] == 7)
                   & (ridership_cal_stations['day_type'] == "Weekday")
                   & (ridership_cal_stations['station_name'] == "Wilson"))

# Use .loc and the filter to select for rides
print(ridership_cal_stations.loc[filter_criteria, 'rides'].sum())

print('')
print('LEFT JOIN - will include ALL rows in the left table and matching rows if they exist. NaN values if no match')
print('count missing values in the right table by doing left join then counting which rows have Nan')
# Merge the movies table with the financials table with a left join
movies_financials = movies.merge(financials, on='id', how='left')
# Count the number of rows in the budget column that are missing
# the data camp exercise said sum() instead of count()  I don't understand this
# if the values are NaN surely the sum would be NaN
'''
Explain: ['budget'].isnull() returns a data frame column of True or False
the count of these is the total number of rows! which is the full number
but the SUM is the number of True - because True is 1 and False is 0

so sum is correct!

'''

number_of_missing_fin = movies_financials['budget'].isnull().sum()

# Print the number of movies missing financials
print(number_of_missing_fin)
'''
Great job! You used a left join to find out which rows in the financials table were missing data. 
When performing a left join, the .merge() method returns a row full of null values for columns 
in the right table if the key column does not have a matching value in both tables. 
We see that there are at least 1,500 rows missing data. 
Wow! That sounds like a lot of work.

'''

'''
Enriching a dataset
Setting how='left' with the .merge()method is a useful technique for enriching or enhancing a 
dataset with additional information from a different table. 
In this exercise, you will start off with a sample of movie data from the movie series Toy Story. 
Your goal is to enrich this data by adding the marketing tag line for each movie. 
You will compare the results of a left join versus an inner join.

'''

# Merge the toy_story and taglines tables with a left join
toystory_tag = toy_story.merge(taglines, how="left")

# Print the rows and shape of toystory_tag
print(toystory_tag)
print(toystory_tag.shape)

# Merge the toy_story and taglines tables with a inner join
toystory_tag = toy_story.merge(taglines)
# Print the rows and shape of toystory_tag
print(toystory_tag)
print(toystory_tag.shape)
'''
If your goal is to enhance or enrich a dataset, then you do not want to lose any of your original data. 
A left join will do that by returning all of the rows of your left table, while using an inner join 
may result in lost data if it does not exist in both tables.

'''

print('')
print('OTHER JOINS')
'''
You found over 250 action only movies by merging action_movies and scifi_movies using a right join. 
With this, you were able to find the rows not found in the action_movies table. 
Additionally, you used the left_on and right_on arguments to merge in the movies table. 

'''
# Merge action_movies to the scifi_movies with right join
action_scifi = action_movies.merge(scifi_movies, on='movie_id', how='right',
                                   suffixes=('_act','_sci'))

# From action_scifi, select only the rows where the genre_act column is null
scifi_only = action_scifi[action_scifi['genre_act'].isnull()]


# Merge the movies and scifi_only tables with an inner join
movies_and_scifi_only = movies.merge(scifi_only, left_on="id", right_on="movie_id")

# Print the first few rows and shape of movies_and_scifi_only
print(movies_and_scifi_only.head())
print(movies_and_scifi_only.shape)

print('')
print('OUTEr JOIN')
'''
returns all rows from both with nulls here there is no match

find all rows that are not in both
'''
# Merge iron_1_actors to iron_2_actors on id with outer join using suffixes
iron_1_and_2 = iron_1_actors.merge(iron_2_actors,
                                     on="id",
                                     how="outer",
                                     suffixes=("_1", "_2"))

# Create an index that returns true if name_1 or name_2 are null
m = ((iron_1_and_2['name_1'].isnull()) |
     (iron_1_and_2['name_2'].isnull()))

# Print the first few rows of iron_1_and_2  - rows that have a null, theremore Not in both
print(iron_1_and_2[m].head())

print('')
print('SELF MERGE / SELF JOIN')
'''
Can  merge to same dataframe - for hierchichal, sequential or graph data for example

Can be left, inner, right, outer join etc - all as usual.

By merging the table to itself, you compared the value of the director 
from the jobs column to other values from the jobs column. 
With the output, you can quickly see different movie directors and the 
people they worked with in the same movie.
'''
# Merge the crews table to itself
crews_self_merged = crews.merge(crews, on='id', how='inner',
                                suffixes=('_dir','_crew'))

# Create a boolean index to select the appropriate rows
boolean_filter = ((crews_self_merged['job_dir'] == 'Director') &
                  (crews_self_merged['job_crew'] != 'Director'))
direct_crews = crews_self_merged[boolean_filter]

# Print the first few rows of direct_crews
print(direct_crews.head())


print('')
print('another exmpale that makes no sense')
'''
To complete this exercise, you needed to merge tables on their index and merge another table to itself. 
After the calculations were added and sub-select specific columns, the data was sorted. 
You found out that Jurassic World had one of the highest of all, improvement in revenue 
compared to the original movie.

'''
# Merge sequels and financials on index id
sequels_fin = sequels.merge(financials, on='id', how='left')

# Self merge with suffixes as inner join with left on sequel and right on id
orig_seq = sequels_fin.merge(sequels_fin, how='inner', left_on='sequel',
                             right_on='id', right_index=True,
                             suffixes=('_org','_seq'))

# Add calculation to subtract revenue_org from revenue_seq
orig_seq['diff'] = orig_seq['revenue_seq'] - orig_seq['revenue_org']

# Select the title_org, title_seq, and diff
titles_diff = orig_seq[['title_org','title_seq','diff']]

# Print the first rows of the sorted titles_diff
print(titles_diff.sort_values("diff", ascending=False).head())


print('')
print(' semi join')
'''

 You have a sense of the steps in this technique. 
 It first merges the tables, then searches it for which rows belong in the final result creating a filter 
 and subsets the left table with that filter.
 
 n this exercise, you replicated a semi-join to filter the table of tracks 
 by the table of invoice items to find the top revenue non-musical tracks. 
 With some additional data manipulation, you discovered that 'TV-shows' is the 
 non-musical genre that has the most top revenue-generating tracks. 

  '''

# Merge the non_mus_tck and top_invoices tables on tid
tracks_invoices = non_mus_tcks.merge(top_invoices, on="tid")

# Use .isin() to subset non_mus_tcks to rows with tid in tracks_invoices
top_tracks = non_mus_tcks[non_mus_tcks['tid'].isin(tracks_invoices['tid'])]

# Group the top_tracks by gid and count the tid rows
cnt_by_gid = top_tracks.groupby(['gid'], as_index=False).agg({'tid':'count'})

# Merge the genres table to cnt_by_gid on gid and print
print(genres.merge(cnt_by_gid, on="gid"))

print('')
print('anti join')
'''
eg find employees who are NOT assigned to a customer
indicator = True will add a _merge column to the result that tells you
if the values were in both or left_only

this all seems very convulted, must be a better way??
'''

# Merge employees and top_cust
empl_cust = employees.merge(top_cust, on='srid',
                                 how='left', indicator=True)

# Select the srid column where _merge is left_only
# this is a list of the employee ids that have NO match in customer
srid_list = empl_cust.loc[empl_cust['_merge'] == 'left_only', 'srid']

# Get employees not working with top customers
# subset JSUT the  employee data base on that list.
print(employees[employees["srid"].isin(srid_list)])
'''
You performed an anti-join by first merging the tables with a left join, 
selecting the ID of those employees who did not support a top customer, 
and then subsetting the original employee's table. 
From that, we can see that there are five employees not supporting top customers. 
Anti-joins are a powerful tool to filter a main table (i.e. employees) 
by another (i.e. customers).

'''
print('')
print('CONCATENATE (vertical)')
# Concatenate the tracks, show only columns names that are in all tables
# default is Vertial, set axis = 1 for horizontal?
# sort True means sort the columns in alpha betical
# join inner means only columns tat are common to all tables are included.
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st],
                               join="inner",
                               ignore_index=True,
                               sort=True)
print(tracks_from_albums)
'''
There are many ways to write code for this task. 
However, concatenating the tables with a key provides a hierarchical 
index that can be used for grouping. 
Once grouped, you can average the groups and create plots. 
You were able to find out that September had the highest average invoice total.
'''
# Concatenate the tables and add keys (which become the index col)
inv_jul_thr_sep = pd.concat([inv_jul, inv_aug, inv_sep],
                            keys=['7Jul', '8Aug', '9Sep'])

# Group the invoices by the index keys and find avg of the total column
# gropu by(lvel=0) means group by the 0 level which is the index?
avg_inv_by_month = inv_jul_thr_sep.groupby(level=0).agg({'total':'mean'})

# Bar plot of avg_inv_by_month
avg_inv_by_month.plot(kind="bar")
plt.show()

print('')
print('append')
print(' append is simpler but less flexible than concat')
# Use the .append() method to combine the tracks tables
metallica_tracks = tracks_ride.append([tracks_master, tracks_st], sort=False)

# Merge metallica_tracks and invoice_items
tracks_invoices = metallica_tracks.merge(invoice_items, on="tid")

# For each tid and name sum the quantity sold
tracks_sold = tracks_invoices.groupby(['tid','name']).agg({'quantity':'sum'})

# Sort in decending order by quantity and print the results
print(tracks_sold.sort_values('quantity', ascending=False))