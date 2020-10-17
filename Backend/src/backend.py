import requests
import json
import zlib
from datetime import datetime

url = 'http://localhost:5000/total'

print(datetime.now(tz=None), "Start")
numbers_to_add = ['0','1','2','3']
post_data={ 'n' : numbers_to_add }
print(datetime.now(tz=None), "Call API with json")
response =  requests.get(url, data=post_data)
print(response.text)
print(datetime.now(tz=None), "Finished json")

print(datetime.now(tz=None), "Call API with dumps")
post_data=json.dumps(post_data)
response =  requests.get(url, data=post_data)
print(response.text)
print(datetime.now(tz=None), "Finished dumps")
