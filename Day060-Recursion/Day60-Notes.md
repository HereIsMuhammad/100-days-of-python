# Day 60: Recursion Introduction

## Concept
**Recursion** is a technique where a function **calls itself** to solve a smaller part of the problem.

Key Points:
- **Base Case**: Condition to stop recursion (important to avoid infinite recursion)
- **Recursive Case**: Function calls itself with a smaller input

## Why Use Recursion?
- Simplifies complex problems (divide & conquer)
- Common in algorithms:
  - Factorial calculation
  - Fibonacci numbers
  - Tree and graph traversals
  - Backtracking problems (like maze, N-Queens)

## Example Problems

1. Factorial of n: `n! = n * (n-1)!`
2. Fibonacci sequence: `F(n) = F(n-1) + F(n-2)`

## Key Points
- Always define **base case** first
- Recursive function should reduce problem size
- Excessive recursion can cause **stack overflow**