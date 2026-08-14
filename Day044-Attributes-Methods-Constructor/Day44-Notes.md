# Day 44: Attributes, Methods, and __init__ Constructor
# Introduction
In Object-Oriented Programming (OOP), classes store data and behavior together.<br>
The data of a class is called attributes, and the behavior is called methods.
<br>
Python uses a special method called __init__ to initialize object data when an object is created.

## 1. What is __init__?
__init__ is a constructor method in Python.
It runs automatically when an object is created.
It is used to assign values to object attributes.
### Syntax
```python
class ClassName:
    def __init__(self, parameters):
        self.attribute = parameters
```
## 2. Attributes in Python Classes
Attributes are variables that belong to an object.
Example:
```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Ahmad", 20)
print(s1.name)
```
Here:
* name and age are attributes
* self.name stores object data
## 3. What is self?
self refers to the current object.
It allows each object to store its own values.
Example:
```python
s1 = Student("Ahmad", 20)
s2 = Student("Ali", 21)
```
s1 and s2 have different values because of self.
## 4. Methods in Classes
Methods are functions inside a class.
They define object behavior.
Example:
```python
class Car:
    def __init__(self, brand):
        self.brand = brand

    def show(self):
        print("Car brand:", self.brand)

Calling method:

c1 = Car("Toyota")
c1.show()
```
## 5. Example
```python
class Mobile:
    def __init__(self, company, price):
        self.company = company
        self.price = price

    def details(self):
        print(self.company, self.price)

Objects:

m1 = Mobile("Samsung", 50000)
m2 = Mobile("Apple", 150000)

m1.details()
m2.details()
```
## 6. Key Concepts Learned
1. Attributes store object data
2. Methods define object behavior
3. __init__ initializes attributes
4. self refers to current object
5. Each object has its own values
### Summary
* __init__ is a constructor that automatically runs when an object is created.
* It assigns values to attributes using self.
* Methods allow objects to perform actions using their stored data.
* This is the foundation of Object-Oriented Programming in Python.

