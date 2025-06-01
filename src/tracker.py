import json
from datetime import datetime

def add_expense(file_path, amount, category, description=""):
    if amount <= 0:
        raise ValueError("Amount must be positive.")
    expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "timestamp": datetime.now().isoformat()
    }
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    data.append(expense)
    with open(file_path, "w") as f:
        json.dump(data, f)

def get_total(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
    return sum(item["amount"] for item in data)

def get_by_category(file_path, category):
    with open(file_path, "r") as f:
        data = json.load(f)
    return [item for item in data if item["category"] == category]
