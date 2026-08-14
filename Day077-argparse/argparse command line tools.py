# Day 77: argparse (Command Line Tools)

import argparse

# Create parser
parser = argparse.ArgumentParser(description="Simple CLI calculator")

# Add arguments
parser.add_argument("num1", type=float, help="First number")
parser.add_argument("num2", type=float, help="Second number")
parser.add_argument("--operation", type=str, choices=["add", "sub", "mul", "div"], default="add",
                    help="Operation to perform (add, sub, mul, div)")

# Parse arguments
args = parser.parse_args()

# Perform calculation
if args.operation == "add":
    result = args.num1 + args.num2
elif args.operation == "sub":
    result = args.num1 - args.num2
elif args.operation == "mul":
    result = args.num1 * args.num2
elif args.operation == "div":
    if args.num2 != 0:
        result = args.num1 / args.num2
    else:
        result = "Cannot divide by zero"

print(f"Result: {result}")