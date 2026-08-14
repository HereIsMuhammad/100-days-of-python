# Day 49: Polymorphism in Python
## What is Polymorphism?

Polymorphism means "many forms".
In Python OOP, polymorphism means:
Different objects can use the same method name but perform different actions.

## Basic Idea

* Same method name
* Different class
* Different behavior

### Example 1: Same Method Name
```python
class Dog:
    def speak(self):
        print("Dog barks")

class Cat:
    def speak(self):
        print("Cat meows")

animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()
```
Output:
Dog barks
Cat meows

### Polymorphism with Inheritance
```python
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Dog bark")

class Cat(Animal):
    def speak(self):
        print("Cat meow")
```
Each child overrides the same method.
### Example 3
```python
class Shape:
    def area(self):
        print("Area not defined")

class Rectangle(Shape):
    def area(self):
        print("Length × Width")

class Circle(Shape):
    def area(self):
        print("π × r²")
```
Same method: area()
## Why Polymorphism?
* Same interface for different objects
* Cleaner code
* Flexible design
## Key Points
* Same method name
* Different objects
* Different behavior
* Often used with inheritance
* Based on method overriding
