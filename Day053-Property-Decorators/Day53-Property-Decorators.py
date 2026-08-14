# Day 53: Property Decorators (@property)

class BankAccount:
    def __init__(self, balance):
        self._balance = 0
        self.balance = balance   # setter will handle validation

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            print("Balance cannot be negative")
        else:
            self._balance = value


account = BankAccount(1000)
print("Current balance:", account.balance)

account.balance = 500
print("Updated balance:", account.balance)

account.balance = -200
print("Final balance:", account.balance)