# Day 78: Unit Testing with `unittest`

## Why Test?
Tests prove your code works as expected and catch bugs early — especially
important before refactoring or adding new features.

## The `unittest` Module (built into Python)
- Create a class that inherits from `unittest.TestCase`.
- Each test is a method starting with `test_`.
- Use assertion methods like `assertEqual`, `assertTrue`, `assertRaises`.

```python
import unittest

def add(a, b):
    return a + b

class TestMathFunctions(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)

if __name__ == "__main__":
    unittest.main()
```

## Common Assertions
| Method | Checks |
|---|---|
| `assertEqual(a, b)` | a == b |
| `assertNotEqual(a, b)` | a != b |
| `assertTrue(x)` | bool(x) is True |
| `assertFalse(x)` | bool(x) is False |
| `assertIsNone(x)` | x is None |
| `assertIn(a, b)` | a in b |
| `assertRaises(Error)` | code raises Error |

## `setUp` and `tearDown`
Run before/after **every** test method — great for preparing test data.
```python
class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = {"balance": 100}

    def test_balance(self):
        self.assertEqual(self.account["balance"], 100)
```

## Running Tests
```bash
python -m unittest test_file.py
python -m unittest discover      # auto-discover all test_*.py files
```

## Summary
`unittest` is Python's built-in testing framework, inspired by JUnit. It's
verbose but requires no installation. Tomorrow we'll see `pytest`, a more
modern and concise alternative.
