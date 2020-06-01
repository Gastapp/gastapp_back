from werkzeug.exceptions import HTTPException


class DuplicatedEmailException(HTTPException):
    code = 409
    description = "Ya existe un usuario con ese email."
