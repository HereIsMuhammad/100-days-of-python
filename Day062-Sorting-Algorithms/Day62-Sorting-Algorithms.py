# Day 62: Sorting Algorithms

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


# Testing
arr = [64, 34, 25, 12, 22, 11, 90]

print("Original:", arr)

print("Bubble Sort:", bubble_sort(arr.copy()))
print("Selection Sort:", selection_sort(arr.copy()))
print("Insertion Sort:", insertion_sort(arr.copy()))