# Day 20: Increment and Decrement in Python Loops

Loops are used to repeat a block of code multiple times.  

## Increment

Increment means **increasing a value step by step**.

### Increment in `for` loop
The `range()` function automatically increases the value.

Example:
- `range(1, 6)` starts from 1 and goes up to 5
- Each step increases by 1 (default)

### Increment in `while` loop
In a while loop, increment must be written manually.

Example logic:
- Start with a value
- Print it
- Increase it using `+ 1`

If increment is not written, the loop will run forever.


## Decrement

Decrement means **decreasing a value step by step**.

### Decrement in `for` loop
To decrement, `range()` uses a negative step.

Example:
- `range(5, 0, -1)`
- Starts from 5
- Decreases by 1 each time
- Stops before 0

### Decrement in `while` loop
In a while loop, decrement is written manually.

Example logic:
- Start from a higher number
- Print it
- Decrease it using `- 1`


## Summary

- Increment increases the value
- Decrement decreases the value
- `for` loop handles increment/decrement automatically
- `while` loop needs manual control
