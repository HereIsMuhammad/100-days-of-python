# Day 39: Variable Scope (Local & Global) in Python

## Introduction
In Python, **scope** means the area of the program where a variable can be used.  
Not every variable can be accessed everywhere. Some variables work only inside a function, and some work in the whole program.

In this lesson, I learn:
- What is scope?
- Local variables
- Global variables
- Difference between local and global variables
- Using global keyword

## 1. What is Scope?
Scope defines **where a variable can be accessed** in a program.
There are two main types I study:
- Local Scope
- Global Scope

## 2. Local Variables
A **local variable** is created **inside a function**.  
It can only be used **inside that function**.

Example:
```python
def my_function():
    x = 10   # local variable
    print("Inside function:", x)

my_function()
# print(x)  # This will give an error because x is local
```
### Explanation:

* x is created inside the function.
* You can use x only inside my_function().
* Outside the function, x does not exist.

## 3. Global Variables
A global variable is created outside all functions.
It can be used anywhere in the program.

Example:
```python
y = 20   # global variable
def show():
    print("Inside function:", y)

show()
print("Outside function:", y)
```
### Explanation:

* y is defined outside the function.
* It can be accessed both inside and outside the function.

## 4. Local vs Global Variable with Same Name
If a variable has the same name inside and outside a function, Python treats them as different variables.

Example:
```python
x = 5   # global variable

def test():
    x = 10  # local variable
    print("Inside function:", x)

test()
print("Outside function:", x)
```
Output:
Inside function: 10
Outside function: 5

### Explanation:

* Inside the function, Python uses the local x.
* Outside, Python uses the global x.

## 5. Using the global Keyword
If you want to change a global variable inside a function, you must use the global keyword.

Example:
```python
count = 0  # global variable

def increase():
    global count
    count = count + 1
    print("Inside function:", count)

increase()
print("Outside function:", count)
```

### Explanation:

global count tells Python to use the global variable, not create a new local one.
Now the function can modify the global variable.

## 6. Why Scope is Important?
1. It helps avoid variable name conflicts.
2. It makes code more organized and safe.
3. It prevents accidental changes to important variables.

### Summary
* Local variables work only inside a function.
* Global variables work in the whole program.
* If a variable name is same, local and global are treated separately.
* Use the global keyword to modify a global variable inside a function.
* Scope helps keep code clean and safe.

