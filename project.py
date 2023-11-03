import sqlite3
import os

# Function to create a SQLite database and attendance table
def create_database():
    connection = sqlite3.connect("attendance.db")
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            present INTEGER
        )
    ''')
    connection.commit()
    connection.close()

# Function to add a new student to the database
def add_student(name):
    connection = sqlite3.connect("attendance.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO students (name, present) VALUES (?, ?)", (name, 0))
    connection.commit()
    connection.close()

# Function to mark a student as present
def mark_present(student_id):
    connection = sqlite3.connect("attendance.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE students SET present = 1 WHERE id = ?", (student_id,))
    connection.commit()
    connection.close()

# Function to display the attendance list
def show_attendance():
    connection = sqlite3.connect("attendance.db")
    cursor = connection.cursor()
    cursor.execute("SELECT id, name, present FROM students")
    students = cursor.fetchall()
    connection.close()

    print("Attendance List:")
    for student in students:
        status = "Present" if student[2] == 1 else "Absent"
        print(f"{student[0]}. {student[1]} - {status}")

if __name__ == "__main__":
    create_database()

    while True:
        print("\nAttendance Tracker Menu:")
        print("1. Add a student")
        print("2. Mark a student as present")
        print("3. Show attendance list")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter the student's name: ")
            add_student(name)
        elif choice == "2":
            student_id = input("Enter the student's ID to mark as present(ID is the serial number in which the students have been added): ")
            mark_present(int(student_id))
        elif choice == "3":
            show_attendance()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")
