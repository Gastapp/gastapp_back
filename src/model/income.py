class Income:

    def __init__(self, user_email, amount, category, date, account, description=""):
        self.user_email = user_email
        self.amount = amount
        self.category = category
        self.date = date
        self.account = account
        self.description = description

