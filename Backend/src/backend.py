import requests
import json


def get_arg( numbers ):
    return { 'n' : numbers }

def get_total_api( url = 'http://localhost:5000/total', numbers_to_add = []):
    return requests.get(url, data=get_arg( numbers_to_add ))

def get_sum_api( url = 'http://localhost:5000/total', n = 10000001):
  numbers_to_add = list(range(n))
  return get_total_api(url, numbers_to_add)

if __name__ == '__main__':
  response = get_sum_api()
  print(response.text)

