# Day 55: Magic/Dunder Methods

## Concept
Magic methods (also called **dunder methods**) are special methods in Python that start and end with double underscores (`__method__`).  
They allow you to define how your objects behave with built-in Python operations.

Common magic methods include:
- `__str__` → defines the string representation of an object
- `__add__` → defines behavior for the `+` operator
- `__len__` → defines behavior for the `len()` function

## Why Use Magic Methods?
- Customize **object behavior** for operators and built-in functions
- Make objects **more Pythonic**
- Allow user-defined classes to **integrate seamlessly** with Python syntax

Example uses:
- `__str__`: How an object is displayed when printed
- `__add__`: How two objects are added using `+`
- `__len__`: How `len(object)` returns a meaningful value

## Key Points
- Magic methods start and end with `__`
- They let you define behavior of **operators and functions**
- Using them makes custom classes easier to use
- Common examples: `__init__`, `__str__`, `__add__`, `__len__`, `__eq__`, etc.

## Example Scenario
We will create a **Vector class** that represents 2D vectors:
- `__str__` to display vector as `(x, y)`
- `__add__` to add two vectors
- `__len__` to get the magnitude (length) of the vector