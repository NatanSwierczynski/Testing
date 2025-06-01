import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import pytest
from tracker import add_expense, get_total, get_by_category
# from src.tracker import add_expense, get_total, get_by_category
# import os
import json

TEST_FILE = "tests/test_data.json"

@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Clear file before each test
    with open(TEST_FILE, "w") as f:
        json.dump([], f)
    yield
    os.remove(TEST_FILE)

def test_add_expense_and_total():
    add_expense(TEST_FILE, 50, "food")
    add_expense(TEST_FILE, 30, "transport")
    assert get_total(TEST_FILE) == 80

def test_get_by_category():
    add_expense(TEST_FILE, 20, "food")
    add_expense(TEST_FILE, 10, "books")
    food_expenses = get_by_category(TEST_FILE, "food")
    assert len(food_expenses) == 1
    assert food_expenses[0]["category"] == "food"

def test_add_expense_invalid():
    with pytest.raises(ValueError):
        add_expense(TEST_FILE, -10, "error")
