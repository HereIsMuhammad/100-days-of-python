# Day 15: Tuples in Python

# Creating tuples
numbers = (1, 2, 3, 4, 5)
fruits = ("apple", "banana", "cherry")
mixed = (1, "apple", True)

# Accessing tuple items
print(numbers[0])
print(fruits[1])
print(fruits[-1])

# Looping through a tuple
for fruit in fruits:
    print(fruit)

# Tuple length
print("Length of numbers tuple:", len(numbers))

# Tuple slicing
print(numbers[1:4])

# Checking item existence
print("apple" in fruits)
print("mango" in fruits)

# Tuple with one item 
single_item = (10,)
print(type(single_item))

# Nested tuple
nested = (1, 2, (3, 4))
print(nested[2][0])
