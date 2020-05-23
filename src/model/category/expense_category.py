from enum import Enum


class ExpenseCategory(Enum):
    casa = "casa"
    comida = "comida"
    entretenimiento = "entretenimiento"
    otro = "otro"
    ropa = "ropa"
    servicios = "servicios"
    salud = "salud"
    transporte = "transporte"


def get_expense_category(category):
    category = category.replace(" ", "_")
    return ExpenseCategory[category].value
