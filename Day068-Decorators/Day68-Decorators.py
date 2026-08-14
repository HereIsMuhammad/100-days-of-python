# Day 68: Decorators

# Logging Decorator
def log_decorator(func):
    def wrapper():
        print("Function is starting...")
        func()
        print("Function has ended.")
    return wrapper

# Using decorator
@log_decorator
def say_hello():
    print("Hello, Ahmad!")

# Another example
@log_decorator
def do_work():
    print("Doing some work...")

# Run
say_hello()
print()
do_work()