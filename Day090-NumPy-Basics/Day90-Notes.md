# Day 90: NumPy Basics

## What is NumPy?
NumPy (Numerical Python) is the foundation library for numerical computing
in Python. It provides the `ndarray` — a fast, memory-efficient
multi-dimensional array — plus vectorized math operations that are much
faster than plain Python loops.

## Setup
```bash
pip install numpy
```

## Creating Arrays
```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([[1, 2], [3, 4]])       # 2D array (matrix)

np.zeros((2, 3))     # array of zeros
np.ones((3, 3))      # array of ones
np.arange(0, 10, 2)  # like range(): [0, 2, 4, 6, 8]
np.linspace(0, 1, 5) # 5 evenly spaced numbers between 0 and 1
```

## Array Attributes
```python
a.shape     # dimensions, e.g. (3,)
a.ndim      # number of dimensions
a.dtype     # data type of elements
a.size      # total number of elements
```

## Vectorized Operations (no loops needed!)
```python
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

a + b        # [11, 22, 33]
a * 2        # [2, 4, 6]
a ** 2       # [1, 4, 9]
np.sqrt(a)   # square root of each element
```
This is much faster than looping in pure Python because NumPy runs the
operation in optimized C code under the hood.

## Indexing & Slicing
```python
arr = np.array([10, 20, 30, 40, 50])
arr[0]        # 10
arr[1:4]      # [20, 30, 40]
arr[arr > 25] # [30, 40, 50]  -> boolean/filter indexing
```

## Useful Aggregate Functions
```python
arr.sum()
arr.mean()
arr.max()
arr.min()
arr.std()      # standard deviation
```

## Reshaping
```python
arr = np.arange(6)          # [0 1 2 3 4 5]
matrix = arr.reshape(2, 3)  # [[0 1 2], [3 4 5]]
```

## Summary
NumPy arrays are faster and more memory-efficient than Python lists for
numerical work, and their vectorized operations let you avoid explicit
loops. NumPy is the foundation that Pandas (tomorrow!), Matplotlib, and
most of the data science ecosystem are built on.
