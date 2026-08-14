# Day 55: Magic Dunder Methods

import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __len__(self):
        # length of vector rounded down to integer
        return int(math.sqrt(self.x ** 2 + self.y ** 2))

# Testing
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(v1)           # Vector(3, 4)
print(v2)           # Vector(1, 2)

v3 = v1 + v2
print(v3)           # Vector(4, 6)

print(len(v3))      # 7 (sqrt(4^2 + 6^2) = 7.21)