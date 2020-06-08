from enum import Enum


class Type(Enum):
    unico = "unico"
    mensual = "mensual"


def get_type(t):
    return Type[t].value
