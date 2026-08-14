# Day 60: Recursion

# Factorial using recursion
def factorial(n):
    if n == 0 or n == 1:  # base case
        return 1
    return n * factorial(n-1)  # recursive call

# Fibonacci using recursion
def fibonacci(n):
    if n == 0:  # base case
        return 0
    elif n == 1:  # base case
        return 1
    return fibonacci(n-1) + fibonacci(n-2)  # recursive call

# Testing
n = 5
print(f"Factorial of {n} is {factorial(n)}")

fib_terms = 6
print(f"First {fib_terms} Fibonacci numbers:")
for i in range(fib_terms):
    print(fibonacci(i), end=" ")