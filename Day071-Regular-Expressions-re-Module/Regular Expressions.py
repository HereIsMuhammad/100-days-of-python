# Day 71: Regular Expressions

import re

# Example text
text = "Contact: ahmad123@gmail.com"

# 1. Search for email
pattern = r'[\w\.-]+@[\w\.-]+\.\w+'

match = re.search(pattern, text)

if match:
    print("Email found:", match.group())
else:
    print("No email found")


# 2. Find all numbers
text2 = "Prices are 100, 250 and 300"

numbers = re.findall(r'\d+', text2)
print("Numbers found:", numbers)


# 3. Replace text
text3 = "Hello Ahmad"
new_text = re.sub("Ahmad", "User", text3)
print("Replaced text:", new_text)


# 4. Email Validation Function
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)


# Test validation
email = input("Enter email: ")

if is_valid_email(email):
    print("Valid email")
else:
    print("Invalid email")