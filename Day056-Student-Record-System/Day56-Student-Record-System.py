# Day 56: OOP Project – Student Record System

import os

class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"{self.student_id},{self.name},{self.age},{self.grade}"

class StudentManager:
    FILE_NAME = "students.txt"

    def add_student(self, student):
        with open(self.FILE_NAME, "a") as f:
            f.write(str(student) + "\n")
        print(f"Student {student.name} added successfully.")

    def load_students(self):
        students = []
        if os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, "r") as f:
                for line in f:
                    student_id, name, age, grade = line.strip().split(",")
                    students.append(Student(student_id, name, age, grade))
        return students

    def search_student(self, student_id):
        students = self.load_students()
        for s in students:
            if s.student_id == student_id:
                return s
        return None

    def update_student(self, student_id, name=None, age=None, grade=None):
        students = self.load_students()
        updated = False
        with open(self.FILE_NAME, "w") as f:
            for s in students:
                if s.student_id == student_id:
                    s.name = name or s.name
                    s.age = age or s.age
                    s.grade = grade or s.grade
                    updated = True
                f.write(str(s) + "\n")
        if updated:
            print(f"Student {student_id} updated successfully.")
        else:
            print(f"Student {student_id} not found.")

    def delete_student(self, student_id):
        students = self.load_students()
        deleted = False
        with open(self.FILE_NAME, "w") as f:
            for s in students:
                if s.student_id != student_id:
                    f.write(str(s) + "\n")
                else:
                    deleted = True
        if deleted:
            print(f"Student {student_id} deleted successfully.")
        else:
            print(f"Student {student_id} not found.")

# --- Example Usage ---
if __name__ == "__main__":
    manager = StudentManager()

    # Adding students
    s1 = Student("101", "Ahmed", 18, "A")
    s2 = Student("102", "Ali", 17, "B")
    manager.add_student(s1)
    manager.add_student(s2)

    # Searching a student
    student = manager.search_student("101")
    if student:
        print("Found student:", student)
    else:
        print("Student not found")

    # Updating a student
    manager.update_student("102", grade="A+")

    # Deleting a student
    manager.delete_student("101")