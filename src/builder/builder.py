from datetime import datetime

from model.category import getCategory
from model.expense import Expense


def build_user(data):
    pass


def build_expense(data):
    expense = Expense(data["id_user"], int(data["amount"]), getCategory(data["category"]), datetime.fromisoformat(data["date"][:-1]))

    if 'description' in data:
        expense.description = data["description"]

    return expense

