# Day 47: Inheritance in Python
## What is Inheritance?
Inheritance is an Object-Oriented Programming (OOP) concept where one class (child class) acquires the properties and methods of another class (parent class).<br>
It allows code reuse and creates a logical relationship between classes.

* Parent class = Base class
* Child class = Derived class
Syntax
```python
class Parent:
    pass

class Child(Parent):
    pass
```
The child class automatically inherits all attributes and methods from the parent class.
#### Example 1: Simple Inheritance
```python
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    pass

d = Dog()
d.speak()
```
Dog class inherits the speak() method from Animal.
#### Example 2: Child Adding Its Own Method
```python
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()
d.bark()
```
The child class can:
* Use parent methods
* Add new methods
#### Example 3: 
```python
class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Name:", self.name)

class Student(Person):
    def study(self):
        print(self.name, "is studying")

s = Student("Ahmad")
s.show_name()
s.study()
```
Student inherits name and show_name() from Person.
## Multilevel Inheritance
Inheritance can happen in multiple levels.
```python
class Animal:
    def eat(self):
        print("Animal eats")

class Mammal(Animal):
    def walk(self):
        print("Mammal walks")

class Dog(Mammal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.eat()
d.walk()
d.bark()
```
Hierarchy:
Animal → Mammal → Dog
## Types of Inheritance in Python
### 1. Single Inheritance
One child inherits from one parent.
Animal → Dog

### 2. Multilevel Inheritance
Inheritance chain.
Animal → Mammal → Dog

### 3. Multiple Inheritance
One child inherits from multiple parents.
Father + Mother → Child
## Why Use Inheritance?
1. Code reuse
2. Cleaner structure
3. Logical hierarchy
4. Easier maintenance
5. Scalable programs


