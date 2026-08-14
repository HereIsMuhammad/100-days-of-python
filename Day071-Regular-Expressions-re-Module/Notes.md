# Day 71: Regular Expressions (re module)

## Concept
Regular Expressions (Regex) are used to search, match, and manipulate text using patterns.

Python provides the built-in `re` module for regex operations.

## What is Regex?
- A sequence of characters that defines a search pattern  
- Used for validation, searching, and text processing  

## Common Patterns

| Pattern | Meaning              |
|--------|---------------------|
| .      | Any character       |
| \d     | Digit (0-9)         |
| \w     | Word character      |
| \s     | Whitespace          |
| ^      | Start of string     |
| $      | End of string       |
| *      | 0 or more times     |
| +      | 1 or more times     |

## re Module Functions

- re.search() → find pattern anywhere  
- re.match() → match at beginning  
- re.findall() → find all matches  
- re.sub() → replace text  

## Email Validation Concept

- Check if email follows pattern:
  username@domain.com

Pattern example:
^[\w\.-]+@[\w\.-]+\.\w+$

## Use Cases
- Form validation  
- Data cleaning  
- Search engines  
- Log analysis  

## Why Use Regex?
- Powerful text processing  
- Saves time  
- Handles complex patterns easily  