from enum import Enum


class Category(Enum):
    clothes = "clothes"
    food = "food"
    home_appliances = "home appliances"


def getCategory(category):
    category = category.replace(" ", "_")
    return Category[category].value
