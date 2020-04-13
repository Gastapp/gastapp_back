from src.controllers import config

collection = config.db.expenses


def save(expense):
    collection.insert(expense)


def get_all():
    return collection.find({})
