from src.services import config

collection = config.db.incomes


def search_by_user_email(user_email):
    return collection.find({"user_email": user_email})


def sum_amounts_by_user(user_email):
    pipeline = [{ "$match": { "user_email": user_email } }, {"$group": { "_id": "null", "total": { "$sum": "$amount" } } }]
    return collection.aggregate(pipeline)


def save(income):
    collection.insert_one(income.__dict__)


