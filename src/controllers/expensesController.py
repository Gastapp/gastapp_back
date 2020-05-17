import pymongo

from builder.builder import build_expense
from model.category import getCategory
from src.services import expensesService


def get_all_user_expenses(id_user):
    return expensesService.search_by_user_id(id_user).sort('date', pymongo.DESCENDING)


def get_all_by_category(id_user, category):
    category = getCategory(category)
    id_user = int(id_user)
    return expensesService.search_by_category(id_user, category).sort('date', 1)


def get_lastest_user_expenses(id_user):
    id_user = int(id_user)
    return expensesService.search_by_user_id(id_user).sort('date', pymongo.DESCENDING).limit(3)


def get_total_expenses_amount_by_user(id_user):
    id_user = int(id_user)
    return expensesService.sum_amounts_by_user(id_user)


def get_total_expenses_amount_by_category(id_user, category):
    category = getCategory(category)
    id_user = int(id_user)
    return expensesService.sum_amounts_by_category(id_user, category)


def add_expense(expense_data):
    expense = build_expense(expense_data)
    expensesService.add_expense(expense)


