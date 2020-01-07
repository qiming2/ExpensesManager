from Account import *


class Manager(object):
    def __init__(self):
        self.people = {}

    def add_people(self, name):
        self.people[name] = Account(name)

    def add_expense(self, amount, name):
        self.is_person_existed(name)
        self.people[name].add_expense(float(amount))

    def add_paid(self, amount, name):
        self.is_person_existed(name)
        self.people[name].add_paid(float(amount))

    def get_bill(self):
        chart = ""
        if len(self.people) == 0:
            chart = "no person is in this account bill"
        else:
            name = "Name"
            left_aligned = "Expense"
            center = "Paid"
            right_aligned = "Balance"
            title = f"{name:<10s} {left_aligned:>10s}{center:>20s}{right_aligned:>20s}"
            chart += title
            for name, account in self.people.items():
                chart += "\n"
                left_aligned = str(round(account.expense, 2))
                center = str(round(account.paid, 2))
                right_aligned = str(round(account.balance(), 2))
                one_line = f"{name:<10s}{left_aligned:>10s}{center:>20s}{right_aligned:>20s}"
                chart += one_line
        return chart

    def clear(self):
        self.people.clear()

    def is_person_existed(self, person):
        check = person in self.people
        if not check:
            print("The person is not in the list, we have added to the list")
            self.people[person] = Account(person)
