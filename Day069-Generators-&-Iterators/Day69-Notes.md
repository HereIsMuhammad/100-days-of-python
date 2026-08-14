# Day 69: Generators & Iterators

## Concept
Generators and iterators help handle sequences efficiently without storing all elements in memory.

- **Iterator**: Object that can be iterated using `__iter__()` and `__next__()`.  
- **Generator**: Function that yields values one at a time using `yield`.

## Iterators

### Definition
- Object implementing `__iter__()` and `__next__()`
- Keeps track of current position
- Raises `StopIteration` at the end

### Example
```python
my_list = [1, 2, 3]
it = iter(my_list)
print(next(it))  # 1
print(next(it))  # 2
```
## Generators

### Definition
- Function that uses yield instead of return
- Produces values lazily (one at a time)
- Memory efficient for large sequences
  
#### Syntax
```python
def my_generator():
    yield 1
    yield 2
```
## Advantages
- Saves memory-
- Infinite sequences possible
- Easy to iterate large datasets

### Use Case
* Fibonacci sequence
* Reading large files
* Streaming data
