from dateutil import parser
import hashlib
from model.category.expense_category import get_expense_category
from model.category.income_category import get_income_category
from model.accounts.expense_account import get_expense_account
from model.accounts.income_account import get_income_account
from model.expense import Expense
from model.income import Income
from model.user import User


def build_user(data):
    password = data["password"].encode('utf-8')
    email = data["email"].lower()
    user = User(data["name"], email, hashlib.sha256(password).hexdigest())
    return user


def build_expense(data):
    expense = Expense(
        data["user_email"],
        int(data["amount"]),
        get_expense_category(data["category"]),
        get_expense_account(data["account"]),
        parser.isoparse(data["date"][:-1])
    )

    if 'description' in data:
        expense.description = data["description"]

    return expense


def build_income(data):
    income = Income(
        data["user_email"],
        int(data["amount"]),
        get_income_category(data["category"]),
        get_income_account(data["account"]),
        parser.isoparse(data["date"][:-1])
    )

    if 'description' in data:
        income.description = data["description"]

    return income


def build_date(date):
    return parser.isoparse(date[:-1])
