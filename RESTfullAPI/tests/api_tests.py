import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))
from src.api import get_total, get_total_in_json 


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(get_total(
            list(range(10000001))),
                         50000005000000,
                         "Should be 50000005000000")

    def test_json(self):
        self.assertEqual(get_total_in_json(
            sum(list(range(10000001)))),
                         {"total": 50000005000000},
                         'Should be {"total": 50000005000000}')

if __name__ == '__main__':
    unittest.main()
