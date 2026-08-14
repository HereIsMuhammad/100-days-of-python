# Day 42: Dictionary Comprehension in Python

print("=== Example 1: Squares using range() ===")
squares = {x: x * x for x in range(1, 6)}
print("Squares dictionary:", squares)


print("\n=== Example 2: Double values from a list ===")
numbers = [1, 2, 3, 4, 5]
double_numbers = {x: x * 2 for x in numbers}
print("Original list:", numbers)
print("Double numbers dictionary:", double_numbers)


print("\n=== Example 3: Even numbers with condition ===")
even_squares = {x: x * x for x in range(1, 11) if x % 2 == 0}
print("Even squares dictionary:", even_squares)


print("\n=== Example 4: Working with strings ===")
names = ["ali", "ahmad", "usman", "hamza"]
name_lengths = {name: len(name) for name in names}
print("Names list:", names)
print("Name lengths dictionary:", name_lengths)


print("\n=== Example 5: Add 10 to each value ===")
numbers2 = [10, 20, 30]
new_dict = {x: x + 10 for x in numbers2}
print("Original list:", numbers2)
print("New dictionary:", new_dict)


