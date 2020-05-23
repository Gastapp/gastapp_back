from dateutil import parser
from datetime import datetime
import hashlib
from model.category.expense_category import get_expense_category
from model.category.income_category import get_income_category
from model.expense import Expense
from model.income import Income
from model.user import User


def build_user(data):
    password = data["password"].encode('utf-8')
    email = data["email"].lower()
    user = User(data["name"], email, hashlib.sha256(password).hexdigest())
    return user


def build_expense(data):
    expense = Expense(data["id_user"], int(data["amount"]), get_expense_category(data["category"]), parser.isoparse(data["date"][:-1]))

    if 'description' in data:
        expense.description = data["description"]

    return expense


def build_income(data):
    income = Income(data["user_email"], int(data["amount"]), get_income_category(data["category"]), datetime.now())

    if 'description' in data:
        income.description = data["description"]

    return income
