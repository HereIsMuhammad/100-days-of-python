# Day 13: Lists in Python

# Creating different types of lists
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "apple", True]
nested = [1, 2, ["a", "b"]]

# Accessing items
print(fruits[0])   # apple
print(fruits[1])   # banana
print(fruits[-1])  # cherry (last item)

# Modifying items
numbers[2] = 99
print("Modified numbers:", numbers)

# Adding items
fruits.append("orange")    # add at the end
fruits.insert(1, "mango")  # add at index 1
print("Fruits after adding:", fruits)

# Removing items
fruits.remove("banana")  # remove by value
fruits.pop()             # remove last item
print("Fruits after removing:", fruits)

# Useful functions
print("Length of numbers list:", len(numbers))
numbers.sort()
print("Sorted numbers:", numbers)
numbers.reverse()
print("Reversed numbers:", numbers)

