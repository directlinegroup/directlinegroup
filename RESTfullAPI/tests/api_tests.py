import unittest
import requests
import json
import random
import string

#Main class to test the Sum API and [0,1,2,3,4,5,6,7,8,9] as input parameter in json data
class TestSum(unittest.TestCase):

    url = 'http://localhost:5000/total'
    
    def get_list(self):
        return list(range(10))

    def get_sum(self, numbers_to_add):
        return sum(numbers_to_add)

    def get_post_data(self, numbers_to_add):
        return { 'n' : numbers_to_add }

    def get_method(self, data):
        return requests.get(self.url, data=data)

    def test_sum(self):
        numbers_to_add = self.get_list()
        response =  self.get_method(self.get_post_data(numbers_to_add))
        
        self.assertTrue(response.status_code == 200)
        self.assertTrue(response.headers["Content-Type"] == "application/json")
        self.assertTrue(response.json()["total"] == self.get_sum(numbers_to_add))

#Negative test case when the list submitted with an incorrect argument as json
class TestWrongParam(TestSum):
    def get_post_data(self, numbers_to_add):
        letters = string.ascii_letters.join('0123456789')
        param = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        return { param : numbers_to_add }
    
    def test_sum(self):
        numbers_to_add = self.get_list()
        response =  self.get_method(self.get_post_data(numbers_to_add))

        self.assertTrue(response.status_code == 500)
        self.assertTrue(response.headers["Content-Type"] == "text/html; charset=utf-8")
        self.assertTrue("Exception: Argument &quot;n&quot; is not found" in response.text)

#Negative test case when the list submitted with an incorrect argument and not form-encoded
class TestWrongParamDumps(TestWrongParam):
    def get_post_data(self, numbers_to_add):
      return json.dumps(super().get_post_data(numbers_to_add))

#[0..9] submitted as JSON
class TestJSON(TestSum):
    def get_method(self, data):
        return requests.get(self.url, json=data)
    
#[0..9] submitted as PARAM
class TestParam(TestSum):
    def get_method(self, data):
        return requests.get(self.url, params=data)

#List submitted as strings
class TestString(TestSum):
    def get_list(self):
        return ['0','1','2','3']

    def get_sum(self, numbers_to_add):
        return 1 + 2 + 3

#List submitted as float
class TestFloat(TestSum):
    def get_list(self):
        return [0.5,1.5,2.5,3.5]

#[0..9] submitted as not form-encoded
class TestDumps(TestSum):
    def get_post_data(self, numbers_to_add):
      return json.dumps(super().get_post_data(numbers_to_add))

#[0..10000000] submitted as not form-encoded
class TestMillion(TestDumps):
    def get_list(self):
      return list(range(10000001))

#Randon million numbers submitted as not form-encoded
class TestRandomMillion(TestDumps):
    def get_list(self):
      return [random.randint(9, 99) for iter in range(10000001)]
        
if __name__ == '__main__':
    unittest.main()
