import pymongo

from builder.builder import build_expense, build_date
from model.category.expense_category import get_expense_category
from src.services import expensesService


def get_all_user_expenses(email_user):
    return expensesService.search_by_user_email(email_user).sort('date', pymongo.DESCENDING)


def get_all_by_category(user_email, category):
    category = get_expense_category(category)
    return expensesService.search_by_category(user_email, category).sort('date', 1)


def get_lastest_user_expenses(user_email):
    return expensesService.search_by_user_email(user_email).sort('date', pymongo.DESCENDING).limit(3)


def get_total_expenses_amount_by_user(user_email):
    cursor = expensesService.sum_amounts_by_user(user_email)
    result = list(cursor)
    if not result:
        return 0
    return result[0]['total']


def get_total_expenses_amount_by_category(user_email, category):
    category = get_expense_category(category)
    return expensesService.sum_amounts_by_category(user_email, category)


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


def filter_expenses(user_email, filter_data):
    if "category" in filter_data:
        category = filter_data["category"]
    else:
        category = {"$exists": True}

    if "date" in filter_data:
        date = {"$gte": build_date(filter_data["date"]["from"]), "$lt": build_date(filter_data["date"]["to"])}
    else:
        date = {"$exists": True}

    if "account" in filter_data:
        account = filter_data["account"]
    else:
        account = {"$exists": True}

    return expensesService.filter(user_email, category, date, account)
