# Day 45: Multiple Objects and Real Examples
## Introduction
In Object-Oriented Programming (OOP), a class is a blueprint.<br>
From one class, we can create many objects.

Each object has:
* its own data (attributes)
* same behavior (methods)
This means multiple objects can exist independently from the same class.
## 1. Creating Multiple Objects
```python
Example:

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("Name:", self.name, "| Age:", self.age)

Objects:

s1 = Student("Ahmad", 20)
s2 = Student("Ali", 22)
s3 = Student("Sara", 19)

s1.show()
s2.show()
s3.show()
```
Output shows each object has different data.
## 2. Each Object Stores Its Own Values
Even though objects come from same class:
* s1.name ≠ s2.name
* s2.age ≠ s3.age
Because each object has its own memory.
## 3. Example 01 (Cars)
```python
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def info(self):
        print(self.brand, "-", self.color)

Objects:

c1 = Car("Toyota", "White")
c2 = Car("Honda", "Black")
c3 = Car("BMW", "Blue")

c1.info()
c2.info()
c3.info()
```
## 4. Example 02 (Bank Account)
```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def show_balance(self):
        print(self.owner, "Balance:", self.balance)


Objects:

a1 = BankAccount("Ahmad", 5000)
a2 = BankAccount("Ali", 12000)

a1.show_balance()
a2.show_balance()
```
Each account has different balance.
## 5. Why Multiple Objects Matter
Real-world systems always have many entities:
* Many students
* Many cars
* Many users
* Many products
OOP models this using multiple objects from one class.

## 6. Key Concepts Learned
1. One class → many objects
2. Each object has separate data
3. Methods are shared
4. Objects represent real-world entities

### Summary
* A class is a blueprint, and objects are real instances.
* Multiple objects can be created from one class, each storing its own data while sharing the same methods.
* This allows Python programs to model real-world systems effectively.

