from enum import Enum


class IncomeAccount(Enum):
    efectivo = "efectivo"
    debito = "debito"


def get_income_account(category):
    return IncomeAccount[category].value
