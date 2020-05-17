from builder import builder
from exceptions.LoginException import LoginException
from services import userService
import hashlib
from bson.json_util import dumps


def login(data):
    password = data["password"].encode('utf-8')
    result = userService.verify_user(data["email"], hashlib.sha256(password).hexdigest())
    if not result:
        raise LoginException()
    print(result)
    return dumps(result)


def register(data):
    user = builder.build_user(data)
    userService.register(user)
    return user.email
