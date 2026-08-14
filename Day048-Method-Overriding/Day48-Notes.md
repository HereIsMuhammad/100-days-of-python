# Day 48: Method Overriding in Python
## What is Method Overriding?
Method overriding is an OOP concept where a child class provides its own implementation of a method that already exists in the parent class.<br>
The child method replaces (overrides) the parent method when called from the child object.

## Basic Idea
If both parent and child have a method with the same name:
The child version runs.
Syntax
```python
class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def show(self):
        print("Child method")
```
### Example 1: Basic Overriding
```python
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

d = Dog()
d.speak()
```
Output:
Dog barks
The child method overrides the parent method.

## Calling Parent Method using super()
Sometimes we want both parent and child behavior.
Python provides super() to access the parent method.
```python
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Dog bark")

d = Dog()
d.speak()
```
Output:
Animal sound
Dog bark
### Another Example 
```python
class Person:
    def role(self):
        print("General role")

class Teacher(Person):
    def role(self):
        print("Teaches students")

class Student(Person):
    def role(self):
        print("Studies subjects")
```
Each child defines its own role.
## Why Method Overriding?
* Customize parent behavior
* Different implementation per class
* Polymorphism support
* Flexible design
## Key Points
* Same method name in parent and child
* Child method overrides parent
* Child object calls child version
* Parent method accessible via super()
## Difference: Inheritance vs Overriding
* Inheritance → reuse parent method
* Overriding → change parent method behavior
