# Day 29: String Formatting in Python

# 1. Basic string concatenation

name = "Ahmad"
age = 19

# Using + operator (not recommended for complex formatting)
message1 = "My name is " + name + " and I am " + str(age) + " years old."
print(message1)

# 2. Using commas in print()
print("My name is", name, "and I am", age, "years old.")

# 3. Using str.format()
message2 = "My name is {} and I am {} years old.".format(name, age)
print(message2)

# You can also use indexes
message3 = "My name is {0} and I am {1} years old. {0} likes Python.".format(name, age)
print(message3)

# Or use named placeholders
message4 = "My name is {n} and I am {a} years old.".format(n=name, a=age)
print(message4)

# 4. Using f-strings (Best & Modern Way)
message5 = f"My name is {name} and I am {age} years old."
print(message5)

# You can put expressions inside f-strings
print(f"Next year, I will be {age + 1} years old.")

# 5. Formatting numbers
pi = 3.1415926535

# Limit decimal places
print(f"Value of pi (2 decimal places): {pi:.2f}")
print(f"Value of pi (4 decimal places): {pi:.4f}")

# Padding numbers with zeros
number = 7
print(f"My number is: {number:03}")   # 007

# Aligning text
text = "Python"
print(f"|{text:<10}|  <- Left aligned")
print(f"|{text:>10}|  <- Right aligned")
print(f"|{text:^10}|  <- Center aligned")

# 6. Real-world example
product = "Laptop"
price = 899.99
quantity = 2

total = price * quantity

bill_message = f"""
----- BILL -----
Product : {product}
Price   : ${price:.2f}
Quantity: {quantity}
----------------
Total   : ${total:.2f}
"""

print(bill_message)

