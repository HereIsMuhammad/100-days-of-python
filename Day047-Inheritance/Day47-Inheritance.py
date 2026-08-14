# Day 47: Inheritance in Python

# Parent Class
class Animal:
    def speak(self):
        print("Animal makes a sound")


# Child Class (inherits Animal)
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Using inherited method
d = Dog()
d.speak()   # inherited from Animal
d.bark()    # Dog's own method


print("\n--- Example 2 ---")

# Real-life Example
class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Name:", self.name)


class Student(Person):
    def study(self):
        print(self.name, "is studying")


s = Student("Ahmad")
s.show_name()   # inherited
s.study()       # own method


print("\n--- Example 3 ---")

# Multilevel Inheritance
class Animal:
    def eat(self):
        print("Animal eats")


class Mammal(Animal):
    def walk(self):
        print("Mammal walks")


class Dog(Mammal):
    def bark(self):
        print("Dog barks")


dog = Dog()
dog.eat()
dog.walk()
dog.bark()
