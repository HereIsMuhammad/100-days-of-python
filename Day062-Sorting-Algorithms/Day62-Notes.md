# Day 62: Sorting Algorithms

## Concept
Sorting means arranging elements in a specific order (ascending or descending).

I study three basic sorting algorithms:
1. Bubble Sort
2. Selection Sort
3. Insertion Sort

## 1. Bubble Sort

### Definition
Repeatedly swap adjacent elements if they are in the wrong order.

### Working
- Compare adjacent elements
- Swap if left > right
- Repeat for all elements
- Largest element moves to the end in each pass

### Time Complexity
- Best Case: O(n)
- Worst Case: O(n²)

### Use Case
- Simple but inefficient for large data

## 2. Selection Sort

### Definition
Find the smallest element and place it at the correct position.

### Working
- Find minimum element in list
- Swap with first element
- Move to next position and repeat

### Time Complexity
- O(n²) (all cases)

### Use Case
- Fewer swaps compared to Bubble Sort

## 3. Insertion Sort

### Definition
Insert each element into its correct position in a sorted part of the list.

### Working
- Start from second element
- Compare with previous elements
- Shift elements and insert at correct position

### Time Complexity
- Best Case: O(n)
- Worst Case: O(n²)

### Use Case
- Efficient for small or nearly sorted data

## Key Differences

| Feature        | Bubble Sort | Selection Sort | Insertion Sort |
|---------------|------------|----------------|----------------|
| Method        | Swap       | Select Min     | Insert         |
| Complexity    | O(n²)      | O(n²)          | O(n²)          |
| Best Case     | O(n)       | O(n²)          | O(n)           |
| Stable        | Yes        | No             | Yes            |

## Why Use Sorting?
- Organize data
- Improve searching efficiency
- Used in databases and real-world applications