# Day 14: Lists Practice

# Creating lists
numbers = [10, 20, 30, 40, 50]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "python", True]

print("Initial Lists:")
print(numbers)
print(fruits)
print(mixed)

print("\n--- Accessing Items ---")
print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])
print("Last fruit:", fruits[-1])

print("\n--- Modifying Items ---")
numbers[2] = 99
print("Modified numbers:", numbers)

print("\n--- Adding Items ---")
fruits.append("orange")
fruits.insert(1, "mango")
print("Fruits after adding:", fruits)

print("\n--- Removing Items ---")
fruits.remove("banana")
fruits.pop()
print("Fruits after removing:", fruits)

print("\n--- List Length ---")
print("Length of fruits list:", len(fruits))

print("\n--- Checking Item Existence ---")
if "apple" in fruits:
    print("Apple is in the list")

print("\n--- Sorting and Reversing ---")
numbers.sort()
print("Sorted numbers:", numbers)

numbers.reverse()
print("Reversed numbers:", numbers)

