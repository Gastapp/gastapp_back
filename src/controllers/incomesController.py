import pymongo

from model.types import Type
from builder.builder import build_income, build_date
from src.services import incomesService


def get_all_user_incomes(email_user):
    return incomesService.search_by_user_email(email_user, Type.unico.value).sort('date', pymongo.DESCENDING)


def get_lastest_user_incomes(user_email):
    return incomesService.search_by_user_email(user_email, Type.unico.value).sort('date', pymongo.DESCENDING).limit(3)


def get_total_incomes_amount_by_user(user_email):
    cursor = incomesService.sum_amounts_by_user(user_email, Type.unico.value)
    result = list(cursor)
    if not result:
        return 0
    return result[0]['total']


def add_income(income_data):
    income = build_income(income_data)
    incomesService.save(income)


def edit_income(income_data):
    income = build_income(income_data)
    income_id = income_data["id"]
    incomesService.update(income_id, income)


def delete_income(income_data):
    income_id = income_data["id"]
    incomesService.delete(income_id)


def filter_incomes(user_email, filter_data):
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

    return incomesService.filter(user_email, category, date, account)
