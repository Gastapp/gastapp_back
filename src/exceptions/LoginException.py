from werkzeug.exceptions import HTTPException


class LoginException(HTTPException):
        code = 401
        description = "Usuario o contraseña incorrectos."


