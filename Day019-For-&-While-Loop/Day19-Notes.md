# Day 19: Loops in Python

## Introduction

Loops are used in Python to repeat a block of code.  
Instead of writing the same code again and again, loops help us run code multiple times in a simple and clean way. 

## What is a Loop?

A loop allows a program to execute a block of code repeatedly based on a condition or a collection of values.

Python mainly has two basic loops:
1. While Loop
2. For Loop

## While Loop

A **while loop** runs as long as a given condition is `True`.

### Syntax
```python
while condition:
    code to execute
```
### Example 
```python
num = 5
while num == 5:
    print(5)
    break
```
### Explanation

* The condition num == 5 is True
* The number 5 is printed
* Break stops the loop immediately

## For Loop

A **for loop** is used to loop through a sequence like a list.

### Syntax
```python
for variable in sequence:
    code to execute
```
### Example
```python
for n in [1, 2, 3]:
    print(n)
```
### Explanation

* The loop takes numbers from the list one by one
* Each number is printed on a new line
* The loop ends when the list finishes
### Summary
* Loops help repeat code
* While loop depends on a condition
* For loop works with a sequence (like a list)
