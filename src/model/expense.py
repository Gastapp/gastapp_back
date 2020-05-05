class Expense:

    def __init__(self, id_user, amount, category, date, description=""):
        self.id_user = id_user
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

