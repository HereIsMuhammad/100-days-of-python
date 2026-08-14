"""
Day 95: Code Quality (Linting & Formatting)
This script deliberately contains messy code in a string, then
runs it through `black` and `ruff` (if installed) to show the difference.
"""

import subprocess
import sys

MESSY_CODE = '''import os
import sys
def add(a,b):
    return a+b
def multiply(a, b):
    result=a*b
    return result
x=[1,2,3,4,5]
y = {"a":1,"b":2}
'''


def write_messy_file(path="messy_example.py"):
    with open(path, "w", encoding="utf-8") as f:
        f.write(MESSY_CODE)
    print(f"Wrote messy example to {path}")
    return path


def run_tool(command: list, label: str):
    print(f"\n--- Running: {label} ---")
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        print(result.stdout or "(no output)")
        if result.stderr:
            print(result.stderr)
    except FileNotFoundError:
        print(f"'{command[0]}' is not installed. Install it with: pip install {command[0]}")


def main():
    path = write_messy_file()

    print("\nBefore formatting:\n")
    with open(path) as f:
        print(f.read())

    run_tool(["black", path], "black (formatter)")
    run_tool(["ruff", "check", path, "--fix"], "ruff (linter, auto-fix)")

    print("\nAfter formatting/linting:\n")
    with open(path) as f:
        print(f.read())


if __name__ == "__main__":
    main()
