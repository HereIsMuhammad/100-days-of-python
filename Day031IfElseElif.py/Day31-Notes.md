# Day 31: If, Elif, Else in Python

## Topic
Today I practiced **conditional statements** in Python using:
- if
- elif (else if)
- else

These are used to make decisions in a program.


##  What is if / elif / else?

- `if` checks the first condition.
- `elif` checks another condition if the previous one is false.
- `else` runs when all conditions are false.

### Example:

```python
marks = 75

if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
else:
    print("Fail")
```