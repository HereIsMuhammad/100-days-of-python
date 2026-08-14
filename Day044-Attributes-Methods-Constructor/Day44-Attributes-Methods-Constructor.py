# Day 44: Attributes, Methods, and __init__ Constructor

# Example 1: Attributes using __init__
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Ahmad", 20)
s2 = Student("Ali", 21)

print("Student 1:", s1.name, s1.age)
print("Student 2:", s2.name, s2.age)

# Example 2: Method inside Class
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def show_info(self):
        print("Car:", self.brand, self.color)

c1 = Car("Toyota", "White")
c2 = Car("Honda", "Black")

c1.show_info()
c2.show_info()

# Example 3: Real Example
class Mobile:
    def __init__(self, company, price):
        self.company = company
        self.price = price

    def details(self):
        print("Mobile Company:", self.company)
        print("Price:", self.price)

m1 = Mobile("Samsung", 50000)
m2 = Mobile("Apple", 150000)

m1.details()
print()
m2.details()
