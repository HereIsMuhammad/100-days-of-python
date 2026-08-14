# Day 5: Comments in Python

Comments are used to explain code and make it easier to understand.
They are ignored by the Python interpreter and do not affect program execution.

## Why Comments Are Used
Comments are helpful to:
- Explain what the code does
- Make code readable
- Help others understand the logic
- Remember code functionality later

## Types of Comments in Python
Python does not have a specific syntax for multi-line comments, but there are two commonly used methods.

### Single-line Comments
Single-line comments start with the `#` symbol.

Example:
```python
# This is a single-line comment
print("Hello, Python")
```
## Method 1: Multiple Single-line Comments (Recommended)
* This method uses # at the beginning of each line.

Example:
```python
# This program prints a message
# It is written for beginners
# Comments help in understanding the code

print("Welcome to Python")
```

* This is the best practice
* Most professional Python developers use this method

## Method 2: Triple Quotes (''' or """)
* Triple quotes are mainly used for docstrings, but they can also be used to write multi-line explanations.

Example:
```python
"""
This is a multi-line comment
It explains what the program does
Python ignores this if it is not assigned to a variable
"""

print("Learning Python Comments")
```
