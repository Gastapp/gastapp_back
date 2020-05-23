from model.category import expense_category, income_category


def get_all_for_expenses():
    return [c.value for c in expense_category.ExpenseCategory]


def get_all_for_incomes():
    return [c.value for c in income_category.IncomeCategory]
