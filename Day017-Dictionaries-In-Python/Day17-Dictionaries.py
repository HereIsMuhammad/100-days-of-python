# Day 17: Dictionaries in Python

# Creating a dictionary
student = {
    "name": "Ahmad",
    "age": 20,
    "course": "Python"
}

# Accessing values
print("Name:", student["name"])
print("Age:", student["age"])

# Modifying value
student["age"] = 21
print("Updated Age:", student["age"])

# Adding a new key-value pair
student["city"] = "Lahore"
print("After adding city:", student)

# Removing an item
student.pop("course")
print("After removing course:", student)

# Dictionary methods
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
