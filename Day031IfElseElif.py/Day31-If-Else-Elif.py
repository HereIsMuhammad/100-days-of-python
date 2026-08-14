# Day 31: If, Elif, Else Practice

print("1. Check Positive / Negative / Zero")
print("2. Check Even / Odd")
print("3. Grade System")
print("4. Simple Calculator")
print("5. Age Eligibility Check")

choice = int(input("Enter your choice (1-5): "))

if choice == 1:
    num = int(input("Enter a number: "))

    if num > 0:
        print("The number is Positive.")
    elif num < 0:
        print("The number is Negative.")
    else:
        print("The number is Zero.")

elif choice == 2:
    num = int(input("Enter a number: "))

    if num % 2 == 0:
        print("The number is Even.")
    else:
        print("The number is Odd.")

elif choice == 3:
    marks = int(input("Enter your marks (0-100): "))

    if marks >= 90:
        print("Grade: A+")
    elif marks >= 80:
        print("Grade: A")
    elif marks >= 70:
        print("Grade: B")
    elif marks >= 60:
        print("Grade: C")
    elif marks >= 50:
        print("Grade: D")
    else:
        print("Grade: F (Fail)")

elif choice == 4:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("Choose operation: +  -  *  /")
    op = input("Enter operator: ")

    if op == "+":
        print("Result:", a + b)
    elif op == "-":
        print("Result:", a - b)
    elif op == "*":
        print("Result:", a * b)
    elif op == "/":
        if b != 0:
            print("Result:", a / b)
        else:
            print("Error: Division by zero!")
    else:
        print("Invalid operator!")

elif choice == 5:
    age = int(input("Enter your age: "))

    if age >= 18:
        print("You are eligible.")
    else:
        print("You are not eligible.")

else:
    print("Invalid choice!")
