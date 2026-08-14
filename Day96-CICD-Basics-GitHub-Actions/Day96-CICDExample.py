"""
Day 96: CI/CD Basics with GitHub Actions
This is example application code plus its test file — exactly the kind
of code a CI pipeline (see tests.yml alongside this file) would run
automatically on every push.
"""


def is_prime(n: int) -> bool:
    """Return True if n is a prime number."""
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


if __name__ == "__main__":
    print("Primes up to 30:", [n for n in range(2, 31) if is_prime(n)])
    print("FizzBuzz 1-15:", [fizzbuzz(n) for n in range(1, 16)])
