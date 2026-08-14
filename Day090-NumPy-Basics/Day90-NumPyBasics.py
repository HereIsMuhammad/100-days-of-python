"""
Day 90: NumPy Basics
Requires: pip install numpy
"""

import numpy as np


def array_creation_demo():
    print("--- Array Creation ---")
    a = np.array([1, 2, 3, 4, 5])
    print("1D array:", a)

    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    print("2D array:\n", matrix)

    print("zeros(2,3):\n", np.zeros((2, 3)))
    print("arange(0,10,2):", np.arange(0, 10, 2))
    print("linspace(0,1,5):", np.linspace(0, 1, 5))


def attributes_demo():
    print("\n--- Attributes ---")
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    print("shape:", matrix.shape)
    print("ndim:", matrix.ndim)
    print("dtype:", matrix.dtype)
    print("size:", matrix.size)


def vectorized_ops_demo():
    print("\n--- Vectorized Operations ---")
    a = np.array([1, 2, 3])
    b = np.array([10, 20, 30])

    print("a + b =", a + b)
    print("a * 2 =", a * 2)
    print("a ** 2 =", a ** 2)
    print("sqrt(a) =", np.sqrt(a))


def indexing_demo():
    print("\n--- Indexing & Filtering ---")
    arr = np.array([10, 20, 30, 40, 50])
    print("arr[1:4] =", arr[1:4])
    print("arr[arr > 25] =", arr[arr > 25])


def aggregate_demo():
    print("\n--- Aggregates ---")
    scores = np.array([85, 92, 78, 90, 88])
    print("sum:", scores.sum())
    print("mean:", scores.mean())
    print("max:", scores.max())
    print("min:", scores.min())
    print("std:", round(scores.std(), 2))


def reshape_demo():
    print("\n--- Reshape ---")
    arr = np.arange(6)
    print("original:", arr)
    print("reshaped (2,3):\n", arr.reshape(2, 3))


if __name__ == "__main__":
    array_creation_demo()
    attributes_demo()
    vectorized_ops_demo()
    indexing_demo()
    aggregate_demo()
    reshape_demo()
