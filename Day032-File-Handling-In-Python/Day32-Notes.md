# Day 32: File Handling in Python

## Introduction
File handling in Python is used to **create, read, write, and append** data in files.
It helps us store data permanently instead of losing it when the program ends.

Python provides the built-in function `open()` to work with files.

## Opening a File
Syntax:
```python
file = open("filename.txt", "mode")
```
Common modes:

1. "r" → Read mode
2. "w" → Write mode (overwrites file)
3. "a" → Append mode (adds data at the end)
4. "r+" → Read and write

## Writing to a File
* We use "w" mode to write data into a file.

Example:
```python
f = open("data.txt", "w")
f.write("Hello, this is my first file!")
f.close()
```
This will create a file (if not exists) and write text into it.

## Reading from a File
* We use "r" mode to read data from a file.

Example:
```python
f = open("data.txt", "r")
content = f.read()
print(content)
f.close()
```
## Appending to a File
* We use "a" mode to add new data without deleting old data.

Example:
```python
f = open("data.txt", "a")
f.write("\nThis is new line added.")
f.close()
```
## Using with Statement (Best Practice)
* The with statement automatically closes the file.

Example:
```
with open("data.txt", "r") as f:
    print(f.read())
```
### Why File Handling is Important?
* To save data permanently
* To read data from files
* To create logs
* To store user records
* To work with large data
