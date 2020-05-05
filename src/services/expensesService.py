from pickle import dumps

from src.services import config

collection = config.db.expenses


def save(expense):
    collection.insert_one(expense)


def search_by_user_id(id_user):
    return collection.find({"id_user": int(id_user)})


def search_by_category(id_user, category):
    return collection.find({"id_user": id_user, "category": category})


def sum_amounts_by_user(id_user):
    pipeline = [{ "$match": { "id_user": id_user } }, {"$group": { "_id": "null", "total": { "$sum": "$amount" } } }]
    return collection.aggregate(pipeline)


def sum_amounts_by_category(id_user, category):
    pipeline = [{ "$match": { "id_user": id_user, "category": category} }, {"$group": { "_id": "null", "total": { "$sum": "$amount" } } }]
    return collection.aggregate(pipeline)


def add_expense(expense):
    collection.insert_one(expense.__dict__)


