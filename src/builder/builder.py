from datetime import datetime
import hashlib
from model.category import getCategory
from model.expense import Expense
from model.user import User


def build_user(data):
    password = data["password"].encode('utf-8')
    user = User(data["name"], data["email"], hashlib.sha256(password).hexdigest())
    return user


def build_expense(data):
    expense = Expense(data["user_email"], int(data["amount"]), getCategory(data["category"]), datetime.fromisoformat(data["date"][:-1]))

    if 'description' in data:
        expense.description = data["description"]

    return expense

