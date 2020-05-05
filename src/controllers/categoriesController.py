from src.model import category


def get_all():
    return [c.value for c in category.Category]

