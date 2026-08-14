# Day 66: SQLite Basics

import sqlite3

# Connect to database (creates file if not exists)
conn = sqlite3.connect("students.db")

# Create cursor
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    marks INTEGER
)
""")

print("Table created successfully!")

# Insert data
cursor.execute("INSERT INTO students (name, age, marks) VALUES (?, ?, ?)", ("Ali", 20, 85))
cursor.execute("INSERT INTO students (name, age, marks) VALUES (?, ?, ?)", ("Ahmad", 21, 90))
cursor.execute("INSERT INTO students (name, age, marks) VALUES (?, ?, ?)", ("Sara", 19, 88))

# Save changes
conn.commit()
print("Data inserted successfully!")

# Fetch data
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

print("\nStudent Records:")
for row in rows:
    print(row)

# Close connection
conn.close()