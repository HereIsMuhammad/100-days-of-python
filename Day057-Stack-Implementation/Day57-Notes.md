# Day 57: Stack Implementation

## Concept
A **Stack** is a linear data structure that follows the **LIFO (Last In, First Out)** principle.

This means:
- The last element added is the first one to be removed.

Example:
Think of a stack of plates:
- You put a plate on top → push
- You remove the top plate → pop

## Why Use Stack?
Stacks are used in many real-world applications:
- Undo/Redo operations
- Browser history (back button)
- Function calls (call stack)
- Expression evaluation

## Basic Operations

### 1. Push
Add an element to the top of the stack.

### 2. Pop
Remove the top element from the stack.

### 3. Peek (optional)
View the top element without removing it.

## Key Points
- Follows **LIFO**
- Only top element is accessible
- Can be implemented using Python list
- Efficient for adding/removing elements from top

## Stack Using List
Python lists can act as a stack:
- `append()` → push
- `pop()` → pop

## Example Scenario
We will create a simple Stack class:
- push elements
- pop elements
- display stack