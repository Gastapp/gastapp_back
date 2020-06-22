from pymongo.errors import DuplicateKeyError

from exceptions.DuplicatedEmailException import DuplicatedEmailException
from src.services import config
import pymongo

collection = config.db.users

collection.create_index([('email', pymongo.ASCENDING)], name='email', unique = True)


def verify_user(email, password):
    return collection.find_one({'email': email, 'password': password}, limit = 1)


def register(user):
    try:
        return collection.insert_one(user.__dict__)
    except DuplicateKeyError:
        print("ayuda por favor")
        raise DuplicatedEmailException()
