# Day 42: Dictionary Comprehension in Python

## Introduction
In Python, dictionary comprehension is a **short and clean way** to create dictionaries.
I use dictionary comprehension when I want to **create a new dictionary from an existing list or dictionary** in one line.

It makes my code:
- Shorter
- Cleaner
- Easier to read (for simple logic)

## Basic Syntax

new_dict = {key_expression: value_expression for item in iterable}

- `key_expression` = key I want to store
- `value_expression` = value I want to store
- `item` = each item from iterable (list, range, dictionary, etc.)
- `iterable` = list, range, dictionary, etc.

## Example 1: Creating a Dictionary from range()

squares = {x: x*x for x in range(1, 6)}

This will create:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

## Example 2: From a List

numbers = [1, 2, 3, 4]
double_numbers = {x: x*2 for x in numbers}

This creates a dictionary where:
- key = number
- value = number * 2

## Example 3: With Condition (if)

even_squares = {x: x*x for x in range(1, 11) if x % 2 == 0}

This stores only even numbers and their squares.

## Example 4: Working with Strings

names = ["ali", "ahmad", "usman"]
name_lengths = {name: len(name) for name in names}

This creates a dictionary where:
- key = name
- value = length of name

## Why I Use Dictionary Comprehension

- To write **shorter code**
- To make code **clean and readable**
- To create dictionaries **quickly**
- To avoid writing long loops

## Important Note

- I use dictionary comprehension for **simple logic**
- For **complex logic**, I should use normal `for` loops

## Summary

- Dictionary comprehension is a short way to create dictionaries
- It uses one line instead of multiple lines
- It can also include conditions
- It makes code clean and pythonic
