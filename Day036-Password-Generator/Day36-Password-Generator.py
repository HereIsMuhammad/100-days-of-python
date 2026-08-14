# Day 36: Password Generator

import random
import string

print("=== Password Generator ===")

# Ask user for password length
length = input("Enter password length: ")

# Type casting with error handling
try:
    length = int(length)
except ValueError:
    print("Please enter a valid number!")
    exit()

if length <= 0:
    print("Password length must be greater than 0!")
    exit()

# Characters to use in password
letters = string.ascii_letters      # a-z A-Z
digits = string.digits              # 0-9
symbols = string.punctuation        # special characters

all_characters = letters + digits + symbols

# Generate password
password = ""

for i in range(length):
    password += random.choice(all_characters)

print("\nYour generated password is:")
print(password)
