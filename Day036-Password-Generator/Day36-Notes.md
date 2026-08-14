# Day 36: Mini Project – Password Generator

## Introduction
In this project, we create a **Password Generator** using Python.
The program generates a **random and strong password** based on the length given by the user.

## Concepts Used

- Variables
- Input and Output
- Type casting (int)
- if conditions
- for loop
- random module
- string module
- Basic error handling (try / except)

## How the Program Workss

1. The program asks the user to enter the password length.
2. The input is converted into an integer using `int()`.
3. If the user enters wrong input, the program shows an error message.
4. The program uses:
   - Letters (a-z, A-Z)
   - Digits (0-9)
   - Symbols (!, @, #, etc.)
5. All these characters are combined.
6. A loop runs for the given length and randomly picks characters.
7. Finally, the generated password is printed.

## Important Modules Used

- random → to select random characters
- string → to get letters, digits, and symbols easily

Examples:
- string.ascii_letters → a-z and A-Z
- string.digits → 0-9
- string.punctuation → special symbols

## Why This Project Is Useful

- Helps understand random module
- Practices loops and conditions
- Teaches how to work with strings
- Real-world useful project
- Improves logic building

## Summary

- User gives password length
- Program generates a random password
- Uses letters, numbers, and symbols
- Uses loop and random.choice()
- Simple and useful mini project
