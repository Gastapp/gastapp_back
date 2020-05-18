class Expense:

    def __init__(self, user_email, amount, category, date, description=""):
        self.user_email = user_email
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

