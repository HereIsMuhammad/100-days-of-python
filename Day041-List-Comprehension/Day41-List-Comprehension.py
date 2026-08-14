# Day 41: List Comprehension in Python

print("=== Example 1: Squares of numbers ===")
numbers = [1, 2, 3, 4, 5]
squares = [n * n for n in numbers]
print("Numbers:", numbers)
print("Squares:", squares)


print("\n=== Example 2: Using range() ===")
nums = [x for x in range(1, 11)]
print("Numbers from 1 to 10:", nums)


print("\n=== Example 3: Even numbers with condition ===")
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print("Even numbers from 1 to 20:", even_numbers)


print("\n=== Example 4: Working with strings ===")
names = ["ali", "ahmad", "usman", "hamza"]
upper_names = [name.upper() for name in names]
print("Original names:", names)
print("Uppercase names:", upper_names)


print("\n=== Example 5: Add 10 to each number ===")
numbers2 = [5, 10, 15, 20]
new_numbers = [x + 10 for x in numbers2]
print("Original list:", numbers2)
print("After adding 10:", new_numbers)

