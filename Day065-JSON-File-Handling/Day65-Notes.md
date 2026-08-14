# Day 65: JSON File Handling

## Concept
JSON (JavaScript Object Notation) is used to store and exchange data.

Python provides a built-in `json` module to work with JSON files.

## What is JSON?
- Data stored in key-value format
- Similar to Python dictionaries
- Lightweight and widely used in APIs

Example:
{
  "name": "Ahmed",
  "age": 21,
  "is_student": true
}

## JSON Module

### Import
import json

## Writing JSON File

### Concept
- Convert Python dictionary into JSON
- Save into file using json.dump()

### Steps
1. Create dictionary
2. Open file in write mode
3. Use json.dump()

## Reading JSON File

### Concept
- Load JSON data into Python dictionary

### Steps
1. Open file in read mode
2. Use json.load()

## Use Case
- Store settings/config
- Save user preferences
- Data exchange in APIs

## Why Use JSON?
- Easy to read and write
- Lightweight format
- Works with almost all programming languages