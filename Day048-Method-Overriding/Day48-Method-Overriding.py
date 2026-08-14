# Day 48: Method Overriding in Python

# Example 1: Basic Overriding

class Animal:
    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    def speak(self):   # overriding parent method
        print("Dog barks")


d = Dog()
d.speak()   # Dog version runs


print("\n--- Example 2 ---")

# Parent method still accessible via super()

class Animal:
    def speak(self):
        print("Animal sound")


class Dog(Animal):
    def speak(self):
        super().speak()   # call parent method
        print("Dog bark")


d = Dog()
d.speak()


print("\n--- Example 3 ---")

# Real-life Example

class Person:
    def role(self):
        print("Person has a general role")


class Teacher(Person):
    def role(self):
        print("Teacher teaches students")


class Student(Person):
    def role(self):
        print("Student studies subjects")


p = Person()
t = Teacher()
s = Student()

p.role()
t.role()
s.role()
