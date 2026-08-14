# Day 41: List Comprehension in Python

## Introduction
In Python, list comprehension is a **short and clean way** to create lists.
I use list comprehension when I want to **create a new list from an existing list** in one line.

It makes code:
- Shorter
- Cleaner
- Easier to read (for simple logic)

## Basic Syntax
new_list = [expression for item in iterable]

- `expression` = what I want to store in the list
- `item` = each value from the list (or any iterable)
- `iterable` = list, range, string, etc.

## Example 1: Normal Way vs List Comprehension
Normal way:

numbers = [1, 2, 3, 4, 5]
squares = []
for n in numbers:
    squares.append(n * n)

Using list comprehension:
squares = [n * n for n in numbers]

Both do the same thing, but list comprehension is shorter.

## Example 2: Using range()
numbers = [x for x in range(1, 6)]

This creates a list: [1, 2, 3, 4, 5]

## Example 3: With Condition (if)

I can also add a condition:
even_numbers = [x for x in range(1, 11) if x % 2 == 0]

This will store only even numbers.

## Example 4: Working with Strings
names = ["ali", "ahmad", "usman"]
upper_names = [name.upper() for name in names]

This converts all names to uppercase.

## Why I Use List Comprehension
- To write **shorter code**
- To make code **clean and readable**
- To create lists **quickly** from other lists

## Important Note
- Use list comprehension for **simple logic**
- For **complex logic**, I should use normal `for` loops

## Summary
- List comprehension is a short way to create lists
- It uses one line instead of multiple lines
- It can also include conditions
- It makes code clean and pythonic
