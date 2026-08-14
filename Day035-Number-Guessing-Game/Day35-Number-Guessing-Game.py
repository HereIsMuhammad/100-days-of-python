# Day 35: Number Guessing Game

import random

print("=== Welcome to Number Guessing Game ===")
print("I am thinking of a number between 1 and 100.")

secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = input("Enter your guess (or type 'q' to quit): ")

    if guess.lower() == "q":
        print("You quit the game. The number was:", secret_number)
        break

    # convert input to integer
    try:
        guess = int(guess)
    except ValueError:
        print("Please enter a valid number!")
        continue

    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number correctly.")
        print("The number was:", secret_number)
        print("Total attempts:", attempts)
        break
