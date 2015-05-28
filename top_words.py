#Purpose: Print the top words most recently spoken by the United States Congress using the Capitol Words API (http://capitolwords.org/api/1/#)
from datetime import date, timedelta
import pprint
import requests

#get top words from 2 days ago because words are typically not updated until then
recent_day = date.today() - timedelta(days=2)
query_params = {'apikey' : 'f6ab5f2e4f69444b9f2c0a44d9a5223d',
                'entity_type' : 'date',
                'entity_value' : recent_day}

endpoint = "http://capitolwords.org/api/1/phrases.json"
response = requests.get(endpoint, params=query_params)
data = response.json()
for record in data:
    print record['ngram']
