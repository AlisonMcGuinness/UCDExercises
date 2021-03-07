import json
import requests

print(' how to load json from file  into dict')
print(' this won\'t find the file. works if I do full path thugh. hmmm.')
# Load JSON: json_data
'''
with open("a_movie.json") as json_file:
    json_data = json.load(json_file)

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])
'''
print('' )
print(' how to load json from API  using requests.get')

# Import package
import requests

# Assign URL to variable: url
url = 'http://www.omdbapi.com/?apikey=72bc447a&t=social+network'
# Package the request, send the request and catch the response: r
r = requests.get(url)
# Decode the JSON data into a dictionary: json_data
print(' response has special method to decode json to dict')
json_data = r.json()
# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])


print('also try out wikipedia api  https://www.mediawiki.org/wiki/API:Main_page   for NESTED JSON')