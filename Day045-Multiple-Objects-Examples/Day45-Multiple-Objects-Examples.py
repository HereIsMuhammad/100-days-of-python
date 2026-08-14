# Day 45: Multiple Objects and Examples

# Example 1: Student Class
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("Name:", self.name, "| Age:", self.age)


# Creating multiple student objects
s1 = Student("Ahmad", 20)
s2 = Student("Ali", 22)
s3 = Student("Sara", 19)

print("=== Student Objects ===")
s1.show()
s2.show()
s3.show()


# Example 2: Car Class
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def info(self):
        print("Brand:", self.brand, "| Color:", self.color)


# Creating multiple car objects
c1 = Car("Toyota", "White")
c2 = Car("Honda", "Black")
c3 = Car("BMW", "Blue")

print("\n=== Car Objects ===")
c1.info()
c2.info()
c3.info()


# Example 3: Bank Account Class
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def show_balance(self):
        print("Owner:", self.owner, "| Balance:", self.balance)


# Creating multiple bank account objects
a1 = BankAccount("Ahmad", 5000)
a2 = BankAccount("Ali", 12000)

print("\n=== Bank Accounts ===")
a1.show_balance()
a2.show_balance()
