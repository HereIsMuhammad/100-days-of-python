# Day 34: Modules & Import in Python

# 1. Importing the whole math module
import math

print("Using math module:")
print("Square root of 16:", math.sqrt(16))
print("Value of pi:", math.pi)

print("-" * 40)

# 2. Importing specific function from math module
from math import sqrt

print("Using sqrt function directly:")
print("Square root of 25:", sqrt(25))

print("-" * 40)

# 3. Importing module with alias
import math as m

print("Using math module with alias:")
print("Square root of 36:", m.sqrt(36))

print("-" * 40)

# 4. Using random module
import random

print("Using random module:")
print("Random number between 1 and 10:", random.randint(1, 10))
print("Random number between 50 and 100:", random.randint(50, 100))

print("-" * 40)

# 5. Using datetime module
import datetime

now = datetime.datetime.now()
print("Current date and time:", now)
