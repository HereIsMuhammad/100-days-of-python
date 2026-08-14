# Day 33: Exception Handling in Python

## Introduction
Exception Handling is used to **handle errors** in a program so that the program does not crash.
Instead of stopping suddenly, the program can show a friendly message and continue working.

In Python, we use:
- try
- except
- else
- finally

## Why Exception Handling is Important?
- Prevents program from crashing
- Handles wrong user input
- Makes programs more safe and user-friendly
- Helps in debugging errors
- 
## Basic Syntax
```python
try:
    # code that may cause error
except:
    # code that runs if error occurs
```
Using try and except

Example:
```python
try:
    x = int(input("Enter a number: "))
    print(10 / x)
except:
    print("Something went wrong!")
```
If user enters wrong input or zero, program will not crash.

## Handling Specific Errors
Common errors:

1. ValueError → when wrong type is given (e.g. text instead of number)
2. ZeroDivisionError → when dividing by zero

Example:
```python
try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ValueError:
    print("Please enter a valid number!")
except ZeroDivisionError:
    print("You cannot divide by zero!")
```
### Using else
else runs when no error occurs.
```python
try:
    x = int(input("Enter a number: "))
    result = 10 / x
except Exception:
    print("Error occurred!")
else:
    print("Result is:", result)
```
### Using finally
finally always runs, whether error occurs or not.
```python
try:
    x = int(input("Enter a number: "))
    print(10 / x)
except:
    print("Error occurred!")
finally:
    print("This will always run.")
```
### Summary
* try → put risky code here
* except → runs if error occurs
* else → runs if no error occurs
* finally → always runs

