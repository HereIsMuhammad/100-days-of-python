# Day 34: Modules & Import in Python

## Introduction
A module in Python is a file that contains Python code such as functions, variables, and classes.
Modules help us organize code and reuse it in different programs.

Python also provides many built-in modules like:
- math
- random
- datetime
- os

We use the `import` keyword to use a module.
## Why Use Modules?
- To reuse code
- To keep code organized
- To avoid writing the same code again and again
- To use powerful built-in features of Python

## Importing a Module

### 1. Import the whole module
```python
import math
print(math.sqrt(16))
Here, we use math.sqrt() because we imported the whole math module.
```
### 2. Import specific functions from a module
```python
from math import sqrt
print(sqrt(25))
Now we can use sqrt() directly without writing math.sqrt().
```
### 3. Import with alias 
```python
import math as m
print(m.sqrt(36))
Here, m is a short name for math.
```
Using the random Module
The random module is used to generate random numbers.

Example:
```python
import random
print(random.randint(1, 10))
This will print a random number between 1 and 10.
```
### Some Useful Modules
math → for mathematical operations<br>
random → for random numbers<br>
datetime → for date and time<br>
os → for working with files and folders<br>

### Summary
* A module is a Python file with code
* Use import module_name to import a module
* Use from module import function to import specific functions
* Use as to give a short name to a module
* Built-in modules save time and make work easier

