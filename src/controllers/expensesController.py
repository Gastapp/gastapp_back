from src.services import expensesService


def get_all_user_expenses(id_user):
    return expensesService.search_by_user_id(id_user)


def get_all_by_category(id_user, category):
    return expensesService.search_by_category(id_user, category)


def get_total_expenses_amount_by_user(id_user):
    return expensesService.sum_amounts_by_user(id_user)


def get_total_expenses_amount_by_category(id_user, category):
    return expensesService.sum_amounts_by_category(id_user, category)

