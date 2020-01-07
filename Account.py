class Account(object):
    def __init__(self, name):
        self.name = name
        self.expense = 0.0
        self.paid = 0.0

    def add_expense(self, expense):
        self.expense += float(expense)

    def add_paid(self, paid):
        self.paid += float(paid)

    def balance(self):
        return self.paid - self.expense
