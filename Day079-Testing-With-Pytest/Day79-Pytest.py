"""
Day 79: Testing with Pytest
Run with:  pytest Day79-Pytest.py
(pytest must be installed: pip install pytest)
"""

import pytest


def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


@pytest.fixture
def numbers():
    return [1, 2, 3, 4, 5]


def test_add():
    assert add(2, 3) == 5


def test_sum_fixture(numbers):
    assert sum(numbers) == 15


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300),
])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected
