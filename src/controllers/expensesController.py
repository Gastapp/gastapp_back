from src.controllers import config

collection = config.db.expenses

def save(expense):
    collection.insert_one(expense)


def get_all():
    return collection.find({})


def get_by_category(category):
    return collection.find({"category": category})

