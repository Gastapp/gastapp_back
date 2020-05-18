import pymongo

from builder.builder import build_expense
from model.category import getCategory
from src.services import expensesService


def get_all_user_expenses(email_user):
    return expensesService.search_by_user_email(email_user).sort('date', pymongo.DESCENDING)


def get_all_by_category(user_email, category):
    category = getCategory(category)
    return expensesService.search_by_category(user_email, category).sort('date', 1)


def get_lastest_user_expenses(user_email):
    return expensesService.search_by_user_email(user_email).sort('date', pymongo.DESCENDING).limit(3)


def get_total_expenses_amount_by_user(user_email):
    return expensesService.sum_amounts_by_user(user_email)


def get_total_expenses_amount_by_category(user_email, category):
    category = getCategory(category)
    return expensesService.sum_amounts_by_category(user_email, category)


def add_expense(expense_data):
    expense = build_expense(expense_data)
    expensesService.add_expense(expense)


