from enum import Enum


class ExpenseAccount(Enum):
    efectivo = "efectivo"
    debito = "debito"
    credito = "credito"


def get_expense_account(category):
    return ExpenseAccount[category].value
