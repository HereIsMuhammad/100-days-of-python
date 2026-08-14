# Day 46: Encapsulation (Public and Private Attributes)
## What is Encapsulation?
Encapsulation is an Object-Oriented Programming (OOP) concept that means restricting direct access to data and controlling it through methods.<br>
It protects object data and ensures safe access.

In simple words:
Encapsulation = Data hiding + Controlled access

## Public Attributes
Public attributes can be accessed and modified directly from outside the class.
Example:
```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Ahmad", 20)

print(s1.name)   # accessible
print(s1.age)

s1.age = 21      # direct modification allowed
```
* Accessible anywhere
* No restriction
## Private Attributes
Private attributes are created using double underscore (__).
They cannot be accessed directly from outside the class.
Example:
```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

acc = BankAccount("Ahmad", 5000)

print(acc.owner)      # OK
# print(acc.__balance)  # Error
```
* Data is hidden
* Protected from direct access
## Accessing Private Data (Using Methods)
Private data is accessed using class methods.
```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def show_balance(self):
        print(self.__balance)

acc = BankAccount("Ali", 8000)
acc.show_balance()
```
## Getter and Setter Methods
Encapsulation often uses getter and setter methods to control data.

Getter → read private value
Setter → modify private value safely
Example:
```python
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

Usage:

a = Account("Ali", 10000)

print(a.get_balance())
a.set_balance(15000)
```
## Why Encapsulation is Important
* Protects data from accidental change
* Improves security
* Controls how data is accessed
* Makes code safer and structured
## Key Points
* Public → self.name
* Private → self.__name
* Private accessed via methods
* Getter & Setter control data
* Encapsulation = data protection
