from src.controllers import config

collection = config.db.expenses

def save(expense):
    collection.insert_one(expense)


def get_all():
    return collection.find({})
