# Day 61: Searching Algorithms

# Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Binary Search
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Testing 
arr = [10, 20, 30, 40, 50]

# Linear Search
result = linear_search(arr, 30)
print("Linear Search Result:", result)

# Binary Search (sorted list required)
result = binary_search(arr, 40)
print("Binary Search Result:", result)