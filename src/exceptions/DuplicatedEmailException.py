from werkzeug.exceptions import HTTPException


class DuplicatedEmailException(HTTPException):
    code = 409
    description = "Email already registered."
