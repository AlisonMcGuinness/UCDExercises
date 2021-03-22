import pandas as pd

pd.set_option('display.max_columns', 10)
pd.set_option('display.width',2000)
pd.set_option('display.max_rows', 200)

ca_videos = pd.read_csv('data\\CAvideos.csv')
gb_videos = pd.read_csv('data\\GBvideos.csv')

'''
concat example
# this example doesn't make a lot of sense because there is no ON
# te first row of table 1 is joined with first row of table 2 and so on.
# no actual connetion to them though.
# It would make sense to concat vertically though! (axis = 0)
concat_data = pd.concat([ca_videos, gb_videos], axis=1)
print(ca_videos.shape, gb_videos.shape, concat_data.shape)
print(concat_data.head())
# there is 2 video_id columsn and 2 title columns
print(concat_data[['video_id', 'title']])

'''
'''
join_data = ca_videos.join(gb_videos,  lsuffix="_can", rsuffix= '_gb')
print(ca_videos.shape, gb_videos.shape, join_data.shape)
print(join_data.head())
# same as concat it doesn't make a lot of sense because there is no ON, 
# but at least you can specify suffixes.
'''

merge_data  = ca_videos.merge(gb_videos, how="inner", on=["video_id", "trending_date"], suffixes=('_can', '_gb'))
print(ca_videos.shape, gb_videos.shape, merge_data.shape)
print(merge_data.head())
print(merge_data[['video_id', 'title_can', 'title_gb']])

'''
Just with video id - there are lots of duplicate matches - it is many to many!
inner join
(40881, 16) (38916, 16) (47342, 31)

left join
(40881, 16) (38916, 16) (85514, 31)

right
(40881, 16) (38916, 16) (70852, 31)

outer
(40881, 16) (38916, 16) (109024, 31)


on video id AND trending_date
inner
(40881, 16) (38916, 16) (2159, 30)
left
(40881, 16) (38916, 16) (40900, 30)  - still duplicate records for same videoId and trending_date in the right table
right
(40881, 16) (38916, 16) (38916, 30)  - result is same count as right table - so no duplicates in left?
outer
(40881, 16) (38916, 16) (77657, 30)
'''

print(gb_videos.info())