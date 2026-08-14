# Day 12: Lists in Python

## What is a List?

A **list** in Python is a collection of items stored in a single variable.  
Lists are one of the most commonly used data structures in Python because they are **flexible, ordered, and changeable**.  

Lists can store:
- Numbers
- Strings
- Booleans
- Other lists
- Mixed types (numbers + strings + booleans)

## Why Use Lists?

Lists are useful because they allow you to:
- Store multiple values in one variable.
- Access items by their **index**.
- Modify, add, or remove items dynamically.
- Organize data for processing and calculations.

## Key Features of Lists

| Feature            | Description                                                      |
|------------------- |------------------------------------------------------------------|
| Ordered            | Items have a specific order.                                     |
| Mutable            | Items can be changed, added, or removed.                         |
| Allows Duplicates  | Same value can appear multiple times.                            |
| Can contain mixed types | Numbers, strings, booleans, or even other lists.            |

## Creating a List

You can create lists using **square brackets `[]`**:

```python
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "apple", True]
nested = [1, 2, ["a", "b"]]

# Accessing Items in a List

Items in a list can be accessed using their **index** (position).  

Python uses **zero-based indexing**, which means the first item has index `0`.

