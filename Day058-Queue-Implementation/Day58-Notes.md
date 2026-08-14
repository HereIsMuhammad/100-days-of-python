# Day 58: Queue Implementation

## Concept
A **Queue** is a linear data structure that follows the **FIFO (First In, First Out)** principle.

This means:
- The first element added is the first one to be removed.

Example:
Think of a line of people:
- Person joins from the back → enqueue
- Person leaves from the front → dequeue

## Why Use Queue?
Queues are widely used in real-world applications:
- Task scheduling (CPU scheduling)
- Printer queue
- Handling requests in web servers
- Breadth-First Search (BFS) in graphs

## Basic Operations

### 1. Enqueue
Add an element to the rear (end) of the queue.

### 2. Dequeue
Remove an element from the front of the queue.

### 3. Peek (optional)
View the front element without removing it.

## Key Points
- Follows **FIFO**
- First element is always removed first
- Efficient operations using `collections.deque`
- Better than list for queue operations

## Why Use `deque` Instead of List?
- List `pop(0)` is slow (O(n))
- `deque.popleft()` is fast (O(1))
- Optimized for queue operations

## Example Scenario
We will create a Queue class using `collections.deque`:
- enqueue elements
- dequeue elements
- display queue