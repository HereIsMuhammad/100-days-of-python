# Day 69: Generators & Iterators

# Fibonacci Generator
def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


# Using the generator
n_terms = 10
fib_gen = fibonacci(n_terms)

print(f"First {n_terms} Fibonacci numbers:")
for num in fib_gen:
    print(num, end=" ")

print("\n")

# Example of iterator using __iter__ and __next__
class MyIterator:
    def __init__(self, limit):
        self.current = 0
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            val = self.current
            self.current += 1
            return val
        else:
            raise StopIteration


it_obj = MyIterator(5)
print("Iterator Example:")
for i in it_obj:
    print(i, end=" ")