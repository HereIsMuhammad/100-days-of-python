# Day 35: Mini Project – Number Guessing Game

## Introduction
In this mini project, we create a simple **Number Guessing Game** using Python.
The computer chooses a random number, and the user tries to guess it.

The program tells the user whether the guess is:
- Too high
- Too low
- Or correct

## Concepts Used

- Variables
- Input and Output
- While loop
- If, elif, else conditions
- random module
- Type casting (int)
- try and except (for error handling)

## How the Game Works

1. The program generates a random number between 1 and 100.
2. The user enters a guess.
3. The program checks:
   - If the guess is smaller → prints "Too low"
   - If the guess is bigger → prints "Too high"
   - If the guess is correct → prints "You won"
4. The game continues until the user guesses correctly or quits.
5. The program also counts how many attempts the user made.

## Why This Project Is Useful

- It improves logic building
- It practices loops and conditions
- It uses real user input
- It uses a built-in module (random)
- It is a complete beginner-friendly project

## Summary

- random.randint() is used to generate a random number
- while loop is used to keep the game running
- if-elif-else is used to compare the guess
- try-except is used to avoid crashing on wrong input
- This is a simple but powerful practice project
