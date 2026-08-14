# Day 79: Testing with Pytest

## Why Pytest?
`pytest` is a third-party testing framework that's simpler and more powerful
than `unittest`: no classes required, plain `assert` statements, and
excellent plugins.

Install it with:
```bash
pip install pytest
```

## Basic Test
```python
# test_math.py
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
```
Run with:
```bash
pytest
```
Pytest auto-discovers any file named `test_*.py` or `*_test.py` and any
function starting with `test_`.

## Fixtures
Fixtures provide reusable setup code (replacing `setUp`/`tearDown`).
```python
import pytest

@pytest.fixture
def sample_list():
    return [1, 2, 3]

def test_sum(sample_list):
    assert sum(sample_list) == 6
```

## Testing Exceptions
```python
import pytest

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
```

## Parametrize (run one test with many inputs)
```python
import pytest

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_add(a, b, expected):
    assert a + b == expected
```

## `unittest` vs `pytest`
| Feature | unittest | pytest |
|---|---|---|
| Built-in | ✅ | ❌ (pip install) |
| Assertions | `self.assertEqual()` | plain `assert` |
| Setup | `setUp`/`tearDown` | fixtures |
| Parametrized tests | verbose | `@pytest.mark.parametrize` |

## Summary
Pytest reduces boilerplate and its fixture + parametrize system makes tests
easier to write and maintain, which is why it's the most popular testing
tool in the Python ecosystem.
