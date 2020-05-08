from datetime import datetime

from model.category import Category
from model.expense import Expense


def build_user(data):
    pass


def build_expense(data):
    expense = Expense(data["id_user"], int(data["amount"]), Category[data["category"]].value, datetime.now())

    if 'description' in data:
        expense.description = data["description"]

    return expense

