import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read & print the first 3 lines
print('reading from a text file')
print('can set mode= r or w on the open call for read/write access')
print('you must close the file!!! unless you put it in block like this')
with open('moby_dick.txt') as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())
    print('THE WHOLE FILE')
    print(file.read())



print('FLAT files are files with rows of data where each row is a collection of info about 1 record.')
print('if all data same type eg numbers use NUMPY')

print('no example file for this but...')
print('Import flat file to numpy array example')
print('use np.loadtxt(filename, OPTIONS')
print('note lots of paremeters to specify rows/cols etc.')
# Assign the filename: file
#file = 'digits_header.txt'
# Load the data: data
#data = np.loadtxt(file, delimiter="\t", skiprows=1, usecols=[0,2])
# Print data
#print(data)

print('data must all be of same type or convertable to one type')
print('example here to set the type when importing')

file = 'seaslug.csv'
# Import file: data
data = np.loadtxt(file, delimiter=',', dtype=str)
# Print the first element of data
print(data[0])
# this is header row with 2 strings
# Import data as floats and skip the first row: data_float
data_float = np.loadtxt(file, delimiter=',', dtype=float, skiprows=1)
# Print the 10th element of data_float
print(data_float[9])
# this will be data row with 2 floats

# Plot a scatterplot of the data
'''
plt.scatter(data_float[:, 0], data_float[:, 1])
plt.xlabel('time (min.)')
plt.ylabel('percentage of larvae')
plt.show()
'''

print('')
print('')
print('MIXED DATA TYPES - use np.genfromtxt')
'''
Working with mixed datatypes (1)
Much of the time you will need to import datasets which have different datatypes 
in different columns; one column may contain strings and another floats, for example.
The function np.loadtxt() will freak at this. 
There is another function, np.genfromtxt(), which can handle such structures. If we pass dtype=None to it, it will figure out what types each column should be.

Import 'titanic.csv' using the function np.genfromtxt() as follows:
'''
#print('')
#print('titanic into np one d array')
#print('cannot get this to work and do not really see the point of it - it creates a list of tuples?')
##data = np.genfromtxt('titanic.tsv', delimiter=',', names=True, dtype=None)

#print(data[0])

'''
Here, the first argument is the filename, the second specifies the delimiter , and the third argument names tells us there is a header. Because the data are of different types, data is an object called a structured array. Because numpy arrays have to contain elements that are all the same type, the structured array solves this by being a 1D array, where each element of the array is a row of the flat file imported. You can test this by checking out the array's shape in the shell by executing np.shape(data).

Accessing rows and columns of structured arrays is super-intuitive: to get the ith row, 
merely execute data[i] and to get the column with name 'Fare', execute data['Fare'].

After importing the Titanic data as a structured array (as per the instructions above), print the entire column with the name 
Survived to the shell. What are the last 4 values of this column?
'''
print('')
print('also function recfromcsv does similar')
'''
Also recfromcsv does the same
Import titanic.csv using the function np.recfromcsv() and assign it to the variable, d. 
You'll only need to pass file to it because it has 
the defaults delimiter=',' and names=True in addition to dtype=None!

d = np.recfromcsv(filename)
'''
print('')
print(' example of importing to pandas with comments and null data')
# Import file: data
file = 'titanic.tsv'
data = pd.read_csv(file, sep='\t', comment='#', na_values=['Nothing'])

# Print the head of the DataFrame
print('data.head(5) first 5 rows')
print(data.head(5))
print('')
print('iloc !')
print(data.iloc[0:4, 0:])
print('')
print('get one column using loc')
print(data.loc[0:4,"Survived"])

print('')
print('get all who survied by creating true/false array and using that as the index to make a subset')
survived  = data["Survived"] == 1
# print(survived)
print('%d survived' % len(data[survived]))
print('their names were')
print(data[survived]['Name'])

# Plot 'Age' variable in a histogram
print('plot the age in a histogram')
print(type(data['Age']))
print('use the [[]]] to get a DataFrame')
print(type(data[['Age']]))
'''
pd.DataFrame.hist(data[['Age']])
plt.xlabel('Age (years)')
plt.ylabel('count')
plt.show()
'''

print('')
print('PICKLED example don''t have a file but this is code to read a pickle file')
'''
import pickle
# Open pickle file and load data: d
with open('data.pkl', 'rb') as file:
    d = pickle.load(file)
# Print d
print(d)
# Print datatype of d
print(type(d))
'''

print('')
print('EXCEL')
'''
Notes about excel
The main difference between XLS and XLSX is that XLS files use a proprietary binary 
format whereas, XLSX use a newer file format known as Open XML.
I saved google doc as XLSX and tryed to read it. 
IT told me to install xlrd but then said that xlrd could only read XLS files.
so then it told me to install openpyxl instead which I did
and then it seem to kind of work!! 
Note I installed things from File, Settings, PRoject Interpreter just click the Plus button
to add and then search for package and install. Very easy

'''

# Import pandas
# Assign spreadsheet filename: file
file = 'battledeath.xlsx'

print('load spread sheet using pd.ExcelFile()')
# Load spreadsheet: xls
xls = pd.ExcelFile(file)

# Print sheet names
print('get the sheet names')
print(xls.sheet_names)
print('Load a sheet into a DataFrame using parse by name or by index')
df1 = xls.parse('2004')
# Print the head of the DataFrame df1
print(df1.head())
# Load a sheet into a DataFrame by index: df2
df2 = xls.parse(0)
# Print the head of the DataFrame df2
print(df2.head())
print('customising import  - skip rows, select columns, rename ')
print('these are all parameters to PARSE')
# Parse the first sheet and rename the columns: df1
df1 = xls.parse(0, skiprows=[0], names=['Country','AAM due to War (2002)'])
# Print the head of the DataFrame df1
print(df1.head())
# Parse the first column of the second sheet and rename the column: df2
df2 = xls.parse(1, usecols=[0], skiprows=[0], names=['Country'])
# Print the head of the DataFrame df2
print(df2.head())


print('')
print('SAS Example')
print(' have no sas file but this is code to import to pandas data frame')
'''
# Import sas7bdat package
from sas7bdat import SAS7BDAT
# Save file to a DataFrame: df_sas
with SAS7BDAT('sales.sas7bdat') as file:
    df_sas = file.to_data_frame()
# Print head of DataFrame
print(df_sas.head())
# Plot histogram of DataFrame features (pandas and pyplot already imported)
pd.DataFrame.hist(df_sas[['P']])
plt.ylabel('count')
plt.show()
'''

print('')
print('STATA FILES')
print('no stat file but here is code to import to data frame')

'''
# Load Stata file into a pandas DataFrame: df
df  = pd.read_stata('disarea.dta')
# Print the head of the DataFrame df
print(df.head())'''


print('')
print('HDF5 files')
import h5py
filename = 'H-H1_LOSC_4_V1-1126259446-32.hdf5'
# Load file: data
data = h5py.File(file, 'r')
# Print the datatype of the loaded file
print(type(data))
# Print the keys of the file
for key in data.keys():
    print(key)

'''
there are 3 main keys
meta
quality
strain
each of this is a ldf5 Group and also has keys()
can drill down to get the actual data out of ['strain']['Strain'].value

'''
print(' CODE TO DRILL DOWN TOGET actuall data into numpy array?')
'''
# Get the HDF5 group: group
group = data['strain']
# Check out keys of group
for key in group.keys():
    print(key)
# Set variable equal to time series data: strain
strain = data['strain']['Strain'].value
print(type(strain))  # <numpy.ndarray> in the eample anyway
print(strain.shape)
'''

print('')
print('MATLAB')
print('have no matlab file but example code here')
'''
import scipy.io
# Load MATLAB file: mat
mat = scipy.io.loadmat('albeck_gene_expression.mat')
# Print the datatype type of mat
print(type(mat))  # it is a dictionary
# the keys are the variable names
# the values are the objects assigned to the variables
print(mat.keys())

# Print the type of the value corresponding to the key 'CYratioCyt'
print(type(mat['CYratioCyt']))  # it is a numpy array

# Print the shape of the value corresponding to the key 'CYratioCyt'
print(mat['CYratioCyt'].shape)


'''
