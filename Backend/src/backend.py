import requests
import json
from datetime import datetime


def get_arg( numbers ):
    return { 'n' : numbers }

def get_total_api( url, numbers_to_add):
    print("convert list to json ", datetime.now(tz=None))
    data=get_arg( numbers_to_add )
    print("call localhost api ", datetime.now(tz=None))
    return requests.get(url, data=data)

def get_sum_api( url = 'http://localhost:5000/total', n = 10000001):
  numbers_to_add = list(range(n))
  return get_total_api(url, numbers_to_add)

if __name__ == '__main__':
  response = get_sum_api()
  print(response.text)
  print("completed at ", datetime.now(tz=None))

