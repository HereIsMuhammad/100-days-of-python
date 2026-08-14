# Day 29: String Formatting in Python 

## What is String Formatting?
String formatting means **inserting variables, numbers, or expressions inside a string** in a clean and readable way.
Instead of writing messy code like this:
```python
"Age is " + str(age)
```
We use string formatting to make our code:
* Cleaner
* Easier to read
* More professional
* Less error-prone
## Why Do We Use String Formatting?
* We use string formatting because:
* It makes output more readable
* It avoids manual type conversion (like str(age))
* It helps in printing reports, logs, messages, bills, results, etc.
* It is very useful in real-world programs (apps, websites, data reports)

Example:
```python
name = "Ahmed"
age = 20
print(f"My name is {name} and I am {age} years old.")
```
Output:
My name is Ahmed and I am 20 years old.

## Ways to Do String Formatting in Python
1. Using + (Concatenation)
```python
"Hello " + name + " your age is " + str(age)
 ```
* Not recommended for big or complex strings.

2. Using str.format()
```python
"My name is {} and I am {} years old.".format(name, age)
```
You can also use indexes or names:
```python
"My name is {n} and I am {a} years old.".format(n=name, a=age)
```
3. Using f-strings
```python
f"My name is {name} and I am {age} years old."
```
### Advantages:
* Short and clean
* Easy to read
* You can put expressions inside {}
Example:
```python
f"Next year I will be {age + 1} years old."
```
## Formatting Numbers
Limit decimal places:
```python
pi = 3.14159
print(f"{pi:.2f}")   # 3.14
```
Add leading zeros:
```python
number = 7
print(f"{number:03}")   # 007
```
Align text:
```python
text = "Python"
print(f"|{text:<10}|")  # Left
print(f"|{text:>10}|")  # Right
print(f"|{text:^10}|")  # Center
```
