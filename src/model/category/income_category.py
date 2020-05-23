from enum import Enum


class IncomeCategory(Enum):
    inversiones = "inversiones"
    premio = "premio"
    regalo = "regalo"
    otro = "otro"


def get_income_category(category):
    category = category.replace(" ", "_")
    return IncomeCategory[category].value
