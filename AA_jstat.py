import requests
import json

from pyjstat import pyjstat
from urllib.request import urlopen
import matplotlib.pyplot as plt
import pandas as pd

pd.set_option('display.max_columns', 10)
pd.set_option('display.width',2000)
pd.set_option('display.max_rows', 200)
'''
pyjstat.from_json_stat(datasets, naming='label', value='value')
Decode JSON-stat formatted data into pandas.DataFrame object.
Parameters:	datasets (OrderedDict, list) – data in JSON-stat format, previously deserialized to a python object by json.load() or json.loads(), for example. Both List and OrderedDict are accepted as inputs.
naming (string, optional) – dimension naming. Possible values: ‘label’ or ‘id’.Defaults to ‘label’.
value (string, optional) – name of the value column. Defaults to ‘value’.
Returns:	results – list of pandas.DataFrame with imported data.
Return type:	list
'''
# mainstream class numbers, mainstream pupils, average class size.
#  https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/ED114/JSON-stat/1.0/
url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/ED112/JSON-stat/1.0/"
results = pyjstat.from_json_stat(json.load(urlopen(url)))
# print(results)  - List with 1 element

data = results[0]  # a PANDAS DATAFRAME! Hurah.
print(data.head())
summary = data.groupby("Statistic")["value"].sum()
print(summary)

summary.plot(kind="bar")
plt.show()

