from src.services import expensesService


def get_all_user_expenses(id_user):
    return expensesService.search_by_user_id(id_user)


def get_all_by_category(id_user, category):
    return expensesService.search_by_category(id_user, category)
