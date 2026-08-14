# Day 49: Polymorphism in Python

# Example 1: Same method, different classes
class Dog:
    def speak(self):
        print("Dog barks")


class Cat:
    def speak(self):
        print("Cat meows")


animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()   # same method name


print("\n--- Example 2 ---")

# Polymorphism with inheritance

class Animal:
    def speak(self):
        print("Animal sound")


class Dog(Animal):
    def speak(self):
        print("Dog bark")


class Cat(Animal):
    def speak(self):
        print("Cat meow")


animals = [Dog(), Cat(), Animal()]

for a in animals:
    a.speak()


print("\n--- Example 3 ---")

# Example 3

class Shape:
    def area(self):
        print("Area not defined")


class Rectangle(Shape):
    def area(self):
        print("Area = length × width")


class Circle(Shape):
    def area(self):
        print("Area = π × r²")


shapes = [Rectangle(), Circle()]

for s in shapes:
    s.area()