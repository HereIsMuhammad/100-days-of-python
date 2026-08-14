# Day 61: Searching Algorithms

## Concept
Searching means finding an element in a data structure (like list).

We study two main searching algorithms:
1. Linear Search
2. Binary Search

## 1. Linear Search

### Definition
Check each element one by one until the target is found.

### Working
- Start from index 0
- Compare each element
- If found → return index
- If not → return -1

### Time Complexity
- Best Case: O(1)
- Worst Case: O(n)

### Use Case
- Works on both sorted and unsorted data

## 2. Binary Search

### Definition
Search in a **sorted list** by dividing it into halves.

### Working
- Find middle element
- If target == middle → found
- If target < middle → search left
- If target > middle → search right

### Time Complexity
- O(log n) → very fast

### Requirement
- List must be **sorted**

## Key Differences

| Feature        | Linear Search | Binary Search |
|---------------|-------------|--------------|
| Data Required | Any list    | Sorted list  |
| Speed         | Slow        | Fast         |
| Complexity    | O(n)        | O(log n)     |

## Why Use Searching?
- Find data quickly
- Used in databases, apps, search engines