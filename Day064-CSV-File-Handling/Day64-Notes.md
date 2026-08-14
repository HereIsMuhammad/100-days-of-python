# Day 64: CSV File Handling

## Concept
CSV (Comma Separated Values) files are used to store tabular data like Excel.

Python provides a built-in `csv` module to read and write CSV files.

## What is CSV?
- Data stored in rows and columns
- Values separated by commas
- Easy to use and widely supported

Example:
Name,Age,Marks  
Ali,20,85  
Ahmad,21,90  

## CSV Module

### Import
import csv

## Writing CSV File

### Concept
- Create a file
- Write rows using csv.writer()

### Steps
1. Open file in write mode
2. Create writer object
3. Write data using writerow()

## Reading CSV File

### Concept
- Read data row by row

### Steps
1. Open file in read mode
2. Create reader object
3. Loop through rows

## Use Case
- Store student records
- Sales data
- Reports and logs

## Why Use CSV?
- Simple and lightweight
- Works with Excel and databases
- Easy data exchange format