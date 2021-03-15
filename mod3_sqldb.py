import pandas as pd
from sqlalchemy import create_engine

print('how to query SQLITE db!')

print(' 1. create database engine ')
print('(Note this does not work if you put chinook.db in the project workspace??')
print('But is fine if you open it from c:\sqlite folder')
print(' I THINK this was because I need to run pycharm as Administrator')
print('- you need to have read/write access to be able to open the db')
print('')
# engine = create_engine('sqlite:///chinook.db')
engine = create_engine('sqlite:///c:\sqlite\chinook.db')


print('2. Get a connection to the database engine')
print('(note do this in context manager or else do con.close() at the end)')
#  Open engine in context manager

# Perform query and save results to DataFrame: df
with engine.connect() as con:
    # rs = con.execute('select LastName, Title from Employee')
    #df = pd.DataFrame(rs.fetchmany(size=3))
    #df.columns = ['Employee Name', 'Title']
    print('3. QUERY the database using con.execute()')
    rs = con.execute("select * from Employee where EmployeeId >= 6")
    print('4. use FETCH on teh query to get the records')
    print('5. Convert the results of the fetch to a Pandas DataFrame ')
    df = pd.DataFrame(rs.fetchall())
    print('get column headers from rs.keys()')
    df.columns = rs.keys()

# Print the length of the DataFrame df
print('rows in table = %d' % len(df))

# Print the head of the DataFrame df
print(df.head())


print('')
print(' OR the more efficient way to avoid all of the above!!')
# use pandas built in method that just needs the engine and the query strings

# Execute query and store records in DataFrame: df
df = pd.read_sql_query('select * from Album', engine)
print(df.head())

print('')
print('inner join example')
with engine.connect() as con:
    rs = con.execute('select Album.Title, Artist.Name from Album Inner join Artist on Album.ArtistId = Artist.ArtistId')
    df = pd.DataFrame(rs.fetchall())
    df.columns = ['Title','Name']
    # Print head of DataFrame df
    print(df.head())

print('')
print('inner join example with read_sql_query')
# Execute query and store records in DataFrame: df
df = pd.read_sql_query('select * from PlayListTrack inner join Track on PlayListTrack.TrackId = Track.TrackId where Milliseconds < 250000', engine)

# Print head of DataFrame
print(df.head())

