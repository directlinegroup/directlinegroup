import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

from src.backend import get_arg, get_sum_api, get_total_api
import json

class TestSum(unittest.TestCase):
    n = 10000001
    numbers = list(range(n))
    numbers_in_json = { 'n' :  numbers }
    response = get_sum_api()

    def test_json(self):
        self.assertEqual(get_arg(self.numbers),
                         self.numbers_in_json,
                         'Should be {"n": [0,1,2...10000000]}')

    def test_response_200(self):
        self.assertTrue(self.response.status_code == 200)

    def test_response_total(self):
        self.assertEqual(self.response.text,
                         json.dumps({"total": 50000005000000.0}),
                         'Should be {"total": 50000005000000}')

    def test_response_blank_list(self):
        self.assertTrue(get_total_api(numbers_to_add = []).text,
                        json.dumps({"total": 0}))

    def test_response_string_list(self):
        self.assertTrue(get_total_api(numbers_to_add = ['1','2','3']).text,
                        json.dumps({"total": 6}))

    def test_response_random_list(self):
        self.assertTrue(get_total_api(numbers_to_add = [1,'2hjdg','dskjf3']).text,
                        json.dumps({"total": 1}))

    def test_response_random_list(self):
        self.assertTrue(get_total_api(numbers_to_add = [1.1,1.2,1.3]).text,
                        json.dumps({"total": 3.6}))

if __name__ == '__main__':
    unittest.main()
