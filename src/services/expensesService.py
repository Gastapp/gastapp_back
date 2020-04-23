from src.services import config

collection = config.db.expenses


def save(expense):
    collection.insert_one(expense)


def search_by_user_id(id_user):
    return collection.find({"id_user": id_user})


def search_by_category(id_user, category):
    return collection.find({"id_user": id_user, "category": category})
