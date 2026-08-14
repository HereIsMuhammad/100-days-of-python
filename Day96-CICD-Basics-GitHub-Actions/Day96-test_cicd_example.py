"""
Test file for the app logic in Day96-CICDExample.py
Run with: pytest Day96-test_cicd_example.py
This is exactly the kind of test suite the GitHub Actions workflow
(tests.yml) would run automatically on every push/PR.

The functions are redefined here directly to keep this file runnable
standalone regardless of how the sibling file is named/imported.
"""


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def fizzbuzz(n: int) -> str:
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(17) is True
    assert is_prime(1) is False
    assert is_prime(15) is False


def test_fizzbuzz():
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(9) == "Fizz"
    assert fizzbuzz(10) == "Buzz"
    assert fizzbuzz(7) == "7"
