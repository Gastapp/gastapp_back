class Expense:

    def __init__(self, email_user, amount, category, date, description=""):
        self.email_user = email_user
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

