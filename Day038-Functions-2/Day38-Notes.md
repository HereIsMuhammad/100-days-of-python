# Day 38: Functions in Python

## Introduction
In this lesson, I learn advanced concepts of Python functions.  
Functions help us reuse code, organize programs, and make our code clean and readable.

What I cover:
- Default arguments
- Keyword arguments
- *args (multiple arguments)
- **kwargs (key-value arguments)
- Returning multiple values from a function

## 1. Default Arguments
Default arguments allow us to set a default value for a parameter.  
If the user does not pass a value, the default value is used.

Example:
```python
def greet(name="User"):
    print("Hello", name)

greet("Ali")   # Hello Ali
greet()        # Hello User
```
## 2. Keyword Arguments
Keyword arguments are passed using the parameter name.
Order does not matter when using keyword arguments.

Example:
```python
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(age=18, name="Ahmed")
```
## 3. *args (Multiple Arguments)
When we do not know how many arguments will be passed, we use *args.
It stores values in a tuple.

Example:
```python
def add(*numbers):
    total = 0
    for n in numbers:
        total += n
    print("Sum:", total)

add(1, 2, 3)
add(5, 10, 15, 20)
```
## 4. **kwargs (Key-Value Arguments)
When we want to pass data in key-value form, we use **kwargs.
It stores values in a dictionary.

Example:
```python
def info(**data):
    for key, value in data.items():
        print(key, ":", value)

info(name="Ali", age=20, city="Lahore")
```
## 5. Returning Multiple Values
A function can return more than one value in Python.
Python returns them as a tuple.

Example:
```python
def calc(a, b):
    add = a + b
    sub = a - b
    return add, sub

x, y = calc(10, 5)
print("Add:", x)
print("Sub:", y)
```
### Summary
* Default arguments provide a default value to parameters.
* Keyword arguments allow passing values using parameter names.
* *args is used for multiple values (stored as tuple).
* **kwargs is used for key-value arguments (stored as dictionary).
* A function can return multiple values in Python.
