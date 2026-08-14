# Day 54: Static Methods & Class Methods

## Concept
In Python, methods inside a class are not all the same. Some methods work with object data, some work with class data, and some do not depend on either.

Two important special methods are:
- `@staticmethod`
- `@classmethod`

These are used when a method does not need normal object behavior.
## Why Use Static and Class Methods?
They are used to organize code better inside a class.

They help when:
- a method belongs to the class logically
- but it does not need full access to object data
- or it needs to work with class-level data instead of instance-level data

This makes code cleaner and more meaningful.
## What is a Static Method?
A static method is a method that belongs to the class, but it does **not** use:
- `self`
- `cls`
It behaves like a normal function, but it is placed inside the class because it is related to that class.
### Syntax
```python
@staticmethod
def method_name():
    pass
```
#### Use Case
Use a static method when:
* the method does not need instance variables
* the method does not need class variables
* but it is still logically connected to the class

For example, a helper function.

## What is a Class Method?
A class method works with the class itself, not individual objects.
It uses cls as its first parameter.
### Syntax
```python
@classmethod
def method_name(cls):
    pass
```
#### Use Case
Use a class method when:
* you want to access or modify class variables
* you want behavior related to the whole class
* not just one object
  
## Counter Class Example
Suppose we want to count how many objects are created from a class.
We can:
* use a class variable to store the count
* use a class method to display that count
* use a static method for a simple helper message
This helps us understand the difference clearly.

### Key Points
* @staticmethod does not use self or cls
* @classmethod uses cls
* static methods are like utility functions inside a class
* class methods are used to work with class-level data
* both improve code organization

## Conclusion
@staticmethod and @classmethod are useful when you want more control over how methods behave inside a class. Static methods are best for helper tasks, while class methods are best for working with shared class data.
