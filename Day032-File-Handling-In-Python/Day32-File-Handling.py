# Day 32: File Handling in Python

# 1. Writing to a file
f = open("myfile.txt", "w")
f.write("Hello! This is Day 32 File Handling in Python.\n")
f.write("We are learning how to write into files.\n")
f.close()

print("Data written to file successfully!")

# 2. Reading from a file
f = open("myfile.txt", "r")
content = f.read()
print("\nReading from file:")
print(content)
f.close()

# 3. Appending to a file
f = open("myfile.txt", "a")
f.write("This line is added using append mode.\n")
f.close()

print("\nNew line appended to file!")

# 4. Reading again using 'with' statement
print("\nReading file again using 'with' statement:")
with open("myfile.txt", "r") as f:
    print(f.read())
