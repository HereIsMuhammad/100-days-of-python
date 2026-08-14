# Day 70: Context Managers

# Example 1: File handling using context manager
with open("sample.txt", "w") as file:
    file.write("Hello, Ahmad!\n")
    file.write("Context manager example for file handling.")

print("File written successfully using 'with'!")

# Reading file
with open("sample.txt", "r") as file:
    content = file.read()
    print("\nFile Content:")
    print(content)


# Example 2: Custom context manager using class
class MyContext:
    def __enter__(self):
        print("Entering context...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context...")
        if exc_type:
            print(f"Exception caught: {exc_val}")
        return True  # suppress exception if any


with MyContext() as ctx:
    print("Inside the context")
    # Uncomment below to test exception handling
    # x = 1 / 0