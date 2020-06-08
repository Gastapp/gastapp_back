import pymongo
from bson import ObjectId
from src.services import config

collection = config.db.expenses


def search_by_user_email(user_email, etype):
    return collection.find({"user_email": user_email, "etype": etype})


def search_by_category(user_email, category):
    return collection.find({"user_email": user_email, "category": category})


def sum_amounts_by_user(user_email, etype):
    pipeline = [{"$match": {"user_email": user_email, "etype": etype}}, {"$group": {"_id": "null", "total": {"$sum": "$amount"}}}]
    return collection.aggregate(pipeline)


def sum_amounts_by_category(user_email, category):
    pipeline = [{"$match": {"user_email": user_email, "category": category}}, {"$group": {"_id": "null", "total": {"$sum": "$amount"}}}]
    return collection.aggregate(pipeline)


def save(expense):
    collection.insert_one(expense.__dict__)


def update(expense_id, expense):
    collection.find_one_and_update(
        {"_id": ObjectId(expense_id)},
        {"$set": expense.__dict__},
        upsert=True)


def delete(expense_id):
    collection.delete_one({"_id": ObjectId(expense_id)})


def filter(user_email, category, date, account):
    pipeline = [{
        "$match": {
             "user_email": user_email,
             "category": category,
             "date": date,
             "account": account,
        }},
        {"$sort": {"date": pymongo.DESCENDING}}
    ]
    return collection.aggregate(pipeline)
