# Day 23: Nested Loops in Python

## Introduction
A **nested loop** is a loop inside another loop.  
Python allows us to place one loop inside another loop to handle repeated tasks within repeated tasks.

Nested loops are commonly used for:
- Pattern printing
- Working with tables
- Multi-dimensional data

## Basic Structure

### for loop inside for loop
```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
