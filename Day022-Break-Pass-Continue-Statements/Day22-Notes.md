# Day 22: Loop Control Statements in Python

## Introduction
I learned about **loop control statements** in Python.  
These statements are used to control the flow of loops and change their normal behavior.

The three main loop control statements are:
- `break`
- `continue`
- `pass`

## 1. break Statement

The `break` statement is used to **stop the loop completely** when a specific condition is met.

### Example:
```python
for i in range(1, 11):
    if i == 6:
        break
    print(i)
```
When i becomes 6, the loop stops.

## 2. continue Statement

The `continue` statement is used to skip the current iteration and move to the next one.

### Example:
```python
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
```
Here, number 5 is skipped.

## 3. pass Statement

The `pass` statement is used as a placeholder.
It does nothing but prevents errors when a statement is required syntactically.

### Example:
```python
for i in range(1, 6):
    if i == 3:
        pass
    print(i)
```
The loop runs normally; `pass` does not affect execution.

## 4. break in while Loop

### Example:
```python
x = 1
while x <= 10:
    if x == 7:
        break
    print(x)
    x += 1
```
The loop stops when x becomes 7.

## continue in while Loop

### Example:
```python
y = 0
while y < 10:
    y += 1
    if y % 2 == 0:
        continue
    print(y)
```
Even numbers are skipped.
