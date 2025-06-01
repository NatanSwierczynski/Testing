import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
from tracker import add_expense, get_total
# from src.tracker import add_expense, get_total
import json, os

TEST_FILE = "tests/test_data2.json"

class TestExpenseTracker(unittest.TestCase):

    def setUp(self):
        with open(TEST_FILE, "w") as f:
            json.dump([], f)

    def tearDown(self):
        os.remove(TEST_FILE)

    def test_add_and_total(self):
        add_expense(TEST_FILE, 10, "misc")
        self.assertEqual(get_total(TEST_FILE), 10)

    def test_invalid_amount(self):
        with self.assertRaises(ValueError):
            add_expense(TEST_FILE, 0, "misc")

if __name__ == "__main__":
    unittest.main()
