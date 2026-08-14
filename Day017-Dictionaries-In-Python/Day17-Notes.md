# Day 17: Dictionaries in Python

* A dictionary in Python is a collection of data stored in **key-value pairs**.
* It is used to store related information together in a structured way.

Dictionaries are:
- Unordered
- Mutable (changeable)
- Indexed by keys instead of numbers

## Creating a Dictionary
* A dictionary is created using curly braces `{}` with keys and values.

Example:
```python
student = {
    "name": "Ahmad",
    "age": 20,
    "course": "Python"
}
```
## 1. Accessing Values
* Values are accessed using their keys.

```python
print(student["name"])
print(student["age"])
```
## 2. Modifying Values
* You can change the value of an existing key.

```python
student["age"] = 21
```
## 3. Adding New Key-Value Pairs

```python
student["city"] = "Lahore"
```
## 4. Removing Items

```python
student.pop("course")
```
## 5. Dictionary Methods
* keys() → returns all keys
* values() → returns all values
* items() → returns key-value pairs

```python
print(student.keys())
print(student.values())
print(student.items())
```

## Why Dictionaries Are Useful
* Store structured data
* Represent real-world objects
* Used in APIs and JSON data
* Faster data access using keys
