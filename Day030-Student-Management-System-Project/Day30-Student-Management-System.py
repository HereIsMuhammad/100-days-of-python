# Day 30: Student Management System 

students = []  # List to store all student records

# Function to add a new student
def add_student():
    name = input("Enter student name: ")
    rollNo = input("Enter student roll no: ")
    age = input("Enter student age: ")
    student_class = input("Enter student class: ")

    # Create student record as dictionary
    student = {
        "name": name,
        "age": age,
        "class": student_class,
        "roll no": rollNo
    }

    # Add student to the list
    students.append(student)
    print("Student added successfully!\n")


# Function to view all students
def view_students():
    if len(students) == 0:
        print("No students found.\n")
        return

    print("\nList of Students:")
    for i, student in enumerate(students, start=1):
        print(f"{i}. Name: {student['name']}, Age: {student['age']}, Class: {student['class']}, Roll No: {student['roll no']}")
    print()


# Function to search a student by roll number
def search_student():
    rollNo = input("Enter student roll no to search: ")

    found = False
    for student in students:
        if student["roll no"].lower() == rollNo.lower():
            print(f"Student Found: Name: {student['name']}, Age: {student['age']}, Class: {student['class']}, Roll No: {student['roll no']}\n")
            found = True
            break

    if not found:
        print("Student not found.\n")


# Function to delete a student by roll number
def delete_student():
    rollNo = input("Enter student roll no to delete: ")

    for student in students:
        if student["roll no"].lower() == rollNo.lower():
            students.remove(student)
            print("Student deleted successfully!\n")
            return

    print("Student not found.\n")


# Function to show menu
def show_menu():
    print("====== Student Management System ======")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")


# Main program loop
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")
