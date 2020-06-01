from bson import ObjectId

from src.services import config

collection = config.db.incomes


def search_by_user_email(user_email):
    return collection.find({"user_email": user_email})


def sum_amounts_by_user(user_email):
    pipeline = [{ "$match": { "user_email": user_email } }, {"$group": { "_id": "null", "total": { "$sum": "$amount" } } }]
    return collection.aggregate(pipeline)


def save(income):
    collection.insert_one(income.__dict__)


def update(income_id, income):
    collection.find_one_and_update(
        {"_id": ObjectId(income_id)},
        {"$set": income.__dict__},
        upsert=True)


def delete(income_id):
    collection.delete_one({"_id": ObjectId(income_id)})
