# Import package
from urllib.request import urlretrieve

# Import pandas
import pandas as pd

# Assign url of file: url
url = "https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv"

# Save file locally
print(' Note you may get PermissionError: [Errno 13] Permission denied: ''winequality-red.csv''')
print(' this means you don''t have rights to WRITE the csv file ')
print(' close pycharm and start it up again by right clicking and Run as Administrator!')
urlretrieve(url, 'winequality-red.csv')

# Read file into a DataFrame and print its head
df = pd.read_csv('winequality-red.csv', sep=';')
print(df.head())


print('')
print('if you don\'t want to save the data locally you can read direct from web to pandas')
print(' pd.read_csv(''url'', sep='';'')')
# Import packages
import matplotlib.pyplot as plt
import pandas as pd

# Assign url of file: url
url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'
# Read file into a DataFrame: df
df = pd.read_csv(url, sep=';')

# Print the head of the DataFrame
print(df.head())

# Plot first column of df
'''
pd.DataFrame.hist(df.ix[:, 0:1])
plt.xlabel('fixed acidity (g(tartaric acid)/dm$^3$)')
plt.ylabel('count')
plt.show()
'''

help(pd.read_excel)
print('')
print(' read EXCEL file from the web into pandas')
print('using pd.read_excel(url, sheet_name=None')
# Assign url of file: url
url = 'http://s3.amazonaws.com/assets.datacamp.com/course/importing_data_into_r/latitude.xls'
# Read in all sheets of Excel file: xls
xls = pd.read_excel(url, sheet_name=None)
print('read_excel returns an object of type %s ' %type(xls))    # orderedDictionayr
# Print the sheetnames to the shell
print('The keys are the sheet names are: %s ' % str(xls.keys()))   # KEYS are the sheetnames
print('The VALUES are of type %s, all data for that sheet' % type(xls.get('1700')))  # VALUES are pand dataframes
# Print the head of the first sheet (using its name, NOT its index)
print(xls['1700'].head())


print('')
print(' How to get data from url request using urllib')
# Import packages
from urllib.request import urlopen, Request
# Specify the url
url = "https://campus.datacamp.com/courses/1606/4135?ex=2"
# This packages the request: request
print(' use Request to make a request object from the url')
request = Request(url)
# Sends the request and catches the response: response
print(' use urlopen with the request to get a response')
response = urlopen(request)
# Print the datatype of response
print(type(response))
print('use read() to get the html from the webpage')
html = response.read()
#print(html)
# Be polite and close the response!
response.close()

print('')
print('Now do the same thing but with higher level "requests" library')
# Import package
import requests
# Specify the url: url
url = 'http://www.datacamp.com/teach/documentation'
# Packages the request, send the request and catch the response: r
print('use requests.get to create/send request and get response. No need to close!')
r = requests.get(url)

print('use response text attribute to get the html')
text = r.text
#print(text)

print('')
print(' use BeautifulSoup to make sense of the html')
from bs4 import BeautifulSoup

# Specify url: url
url = 'https://www.python.org/~guido/'
# Package the request, send the request and catch the response: r
r = requests.get(url)
# Extracts the response as html: html_doc
html_doc = r.text
# Create a BeautifulSoup object from the HTML: soup
print('make BeautifSoupr object by passing in html')
soup = BeautifulSoup(html_doc)
# Prettify the BeautifulSoup object: pretty_soup
print('then LOADS of methods on object to find/prettify/title etc')
pretty_soup = soup.prettify()

print(' use get_text to just get the text, with all tags removed')
guido_text = soup.get_text()
#print(guido_text)
print(type(pretty_soup))
print(' use title to get the text in the <title> tags, including the tags!')
print(type(soup.title))
print(soup.title)

# Find all 'a' tags (which define hyperlinks): a_tags
print('')
print('use find_all to get a list (ResultSet) of all of a certain tag (element.Tag). eg the anchor tags')
a_tags = soup.find_all('a')
# Print the URLs to the shell
for x in a_tags:
    print(x.get('href'))
#print(pretty_soup)