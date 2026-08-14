# Day 40: Lambda Functions in Python

print("=== Example 1: Simple Lambda Function ===")
add = lambda a, b: a + b
print("Add 5 + 3 =", add(5, 3))


print("\n=== Example 2: Lambda with One Argument ===")
square = lambda x: x * x
print("Square of 4 =", square(4))


print("\n=== Example 3: Lambda with map() ===")
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print("Original numbers:", numbers)
print("Doubled numbers:", doubled)


print("\n=== Example 4: Lambda with filter() ===")
numbers2 = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers2))
print("Original numbers:", numbers2)
print("Even numbers:", even_numbers)


print("\n=== Example 5: Lambda with sorted() ===")
pairs = [(1, 3), (4, 1), (2, 2), (5, 0)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print("Original pairs:", pairs)
print("Sorted by second value:", sorted_pairs)


print("\n=== End of Day 40 ===")
