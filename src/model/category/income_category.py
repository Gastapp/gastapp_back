from enum import Enum


class IncomeCategory(Enum):
    inversiones = "inversiones"
    otro = "otro"
    premio = "premio"
    regalo = "regalo"
    venta = "venta"


def get_income_category(category):
    category = category.replace(" ", "_")
    return IncomeCategory[category].value
