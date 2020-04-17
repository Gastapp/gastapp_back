from src.controllers import config

collection = config.db.expenses

def save(expense):
    collection.insert_one(expense)


def get_all_user_expenses(id_user):
    return collection.find({"id_user": id_user})


def get_by_category(category):
    return collection.find({"category": category})

