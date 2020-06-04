from model.accounts import expense_account, income_account


def get_all_for_expenses():
    return [c.value for c in expense_account.ExpenseAccount]


def get_all_for_incomes():
    return [c.value for c in income_account.IncomeAccount]
