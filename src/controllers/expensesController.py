import pymongo

from builder.builder import build_expense
from model.types import Type
from src.services import expensesService


def get_all_user_expenses(email_user):
    return expensesService.search_by_user_email(email_user, Type.unico.value).sort('date', pymongo.DESCENDING)


def get_lastest_user_expenses(user_email):
    return expensesService.search_by_user_email(user_email, Type.unico.value).sort('date', pymongo.DESCENDING).limit(3)


def get_total_expenses_amount_by_user(user_email):
    cursor = expensesService.sum_amounts_by_user(user_email, Type.unico.value)
    result = list(cursor)
    if not result:
        return 0
    return result[0]['total']


def add_expense(expense_data):
    expense = build_expense(expense_data)
    expensesService.save(expense)


def edit_expense(expense_data):
    expense = build_expense(expense_data)
    expense_id = expense_data["id"]
    expensesService.update(expense_id, expense)


def delete_expense(expense_data):
    expense_id = expense_data["id"]
    expensesService.delete(expense_id)


