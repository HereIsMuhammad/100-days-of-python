# Day 40: Lambda Functions in Python

## Introduction
In Python, a lambda function is a **small, anonymous function** (a function without a name).
I use lambda functions when I need a **short and simple function for a short time**.

A normal function is written using `def`, but a lambda function is written using the `lambda` keyword.

## Syntax

lambda arguments : expression

- `lambda` is the keyword
- `arguments` are the inputs
- `expression` is the result that will be returned automatically

## Example 1: Simple Lambda Function

Normal function:

def add(a, b):
    return a + b

Same thing using lambda:

add = lambda a, b: a + b

## Example 2: Lambda with One Argument

square = lambda x: x * x

This returns the square of a number.

## Example 3: Using Lambda with Built-in Functions

I can use lambda with functions like `map()` and `filter()`.

Example with map():
numbers = [1, 2, 3, 4]
result = list(map(lambda x: x * 2, numbers))

This will double every number in the list.

Example with filter():
numbers = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 == 0, numbers))

This will keep only even numbers.

## Why I Use Lambda Functions

- When I need a **short function**
- When I don’t want to write a full `def` function
- When I use functions like `map()`, `filter()`, or `sorted()`

## Important Note

- Lambda functions can only have **one expression**
- They are best for **small and simple tasks**
- For big logic, I should use normal `def` functions

## Summary

- Lambda is a small anonymous function
- It is written in one line
- It is useful for short and simple operations
- It makes code shorter and cleaner
