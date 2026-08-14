# Day 33: Exception Handling in Python

# Example 1: Simple try-except
try:
    num = int(input("Enter a number: "))
    print("Result:", 10 / num)
except:
    print("Error! Please enter a valid number and not zero.")

print("-" * 40)

# Example 2: Handling specific errors
try:
    num = int(input("Enter another number: "))
    result = 20 / num
    print("Result:", result)
except ValueError:
    print("ValueError: Please enter a number only!")
except ZeroDivisionError:
    print("ZeroDivisionError: You cannot divide by zero!")

print("-" * 40)

# Example 3: Using else and finally
try:
    num = int(input("Enter one more number: "))
    result = 30 / num
except Exception:
    print("Some error occurred!")
else:
    print("No error! Result is:", result)
finally:
    print("This block always runs.")
