from pickle import dumps

from src.services import config

collection = config.db.expenses


def save(expense):
    collection.insert_one(expense)


def search_by_user_email(user_email):
    return collection.find({"user_email": user_email})


def search_by_category(user_email, category):
    return collection.find({"user_email": user_email, "category": category})


def sum_amounts_by_user(user_email):
    pipeline = [{ "$match": { "user_email": user_email } }, {"$group": { "_id": "null", "total": { "$sum": "$amount" } } }]
    return collection.aggregate(pipeline)


def sum_amounts_by_category(user_email, category):
    pipeline = [{ "$match": { "user_email": user_email, "category": category} }, {"$group": { "_id": "null", "total": { "$sum": "$amount" } } }]
    return collection.aggregate(pipeline)


def add_expense(expense):
    collection.insert_one(expense.__dict__)


