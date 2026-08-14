# Day 46: Encapsulation (Public and Private Attributes)

# Encapsulation means restricting direct access to some data
# and controlling it using methods.

# Example 1: Public Attributes
class Student:
    def __init__(self, name, age):
        self.name = name      # public
        self.age = age        # public


s1 = Student("Ahmad", 19)

print("=== Public Attributes ===")
print("Name:", s1.name)
print("Age:", s1.age)

# Direct modification allowed
s1.age = 21
print("Updated Age:", s1.age)

# Example 2: Private Attributes
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # public
        self.__balance = balance    # private (double underscore)

    def show_balance(self):
        print("Balance:", self.__balance)


acc = BankAccount("Ahmad", 5000)

print("\n=== Private Attribute ===")
print("Owner:", acc.owner)

# Access via method
acc.show_balance()

# Direct access (will cause error if uncommented)
# print(acc.__balance)

# Example 3: Controlled Access (Getter & Setter)
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid amount")


a = Account("Ali", 10000)

print("\n=== Getter & Setter ===")
print("Balance:", a.get_balance())

a.set_balance(15000)
print("Updated Balance:", a.get_balance())

a.set_balance(-500)   # invalid
