# Day 16: Sets in Python

# Creating sets
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}

print("Initial fruits set:", fruits)
print("Initial numbers set:", numbers)

# Adding items
fruits.add("orange")
fruits.update(["mango", "grape"])

print("\nAfter adding items:")
print("Fruits:", fruits)

# Removing items
fruits.remove("banana")   # removes banana (error if not found)
fruits.discard("kiwi")    # no error if item does not exist
removed_item = fruits.pop()  # removes a random item

print("\nAfter removing items:")
print("Removed item:", removed_item)
print("Fruits:", fruits)

# Checking membership
print("\nChecking membership:")
print("Is apple in fruits?", "apple" in fruits)
print("Is kiwi in fruits?", "kiwi" in fruits)

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}

print("\nSet operations:")
print("Union:", a | b)
print("Intersection:", a & b)
print("Difference (a - b):", a - b)
print("Symmetric Difference:", a ^ b)

# Useful functions
print("\nUseful functions:")
print("Length of fruits set:", len(fruits))

fruits.clear()
print("Fruits after clear():", fruits)
