
import csv
import os

FILE_NAME = "students.csv"

FIELDNAMES = [
    "Roll_No",
    "Name",
    "Class",
    "Python",
    "Mathematics",
    "Statistics"
]


# Create CSV file if it doesn't exist
def initialize_file():
    if not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0:
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()


# Read all student records
def read_students():
    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


# Add a new student
def add_student():
    students = read_students()

    roll_no = input("Enter Roll Number: ")

    # Check duplicate roll number
    for student in students:
        if student["Roll_No"] == roll_no:
            print("Student with this Roll Number already exists!")
            return

    name = input("Enter Student Name: ")
    student_class = input("Enter Class: ")

    try:
        python = float(input("Enter Python Marks: "))
        mathematics = float(input("Enter Mathematics Marks: "))
        statistics = float(input("Enter Statistics Marks: "))

        if not all(0 <= mark <= 100 for mark in [python, mathematics, statistics]):
            print("Marks must be between 0 and 100.")
            return

    except ValueError:
        print("Please enter valid numeric marks.")
        return

    new_student = {
        "Roll_No": roll_no,
        "Name": name,
        "Class": student_class,
        "Python": python,
        "Mathematics": mathematics,
        "Statistics": statistics
    }

    students.append(new_student)

    save_students(students)

    print("Student added successfully!")


# View all students
def view_students():
    students = read_students()

    if not students:
        print("No student records found.")
        return

    print("\n========== ALL STUDENTS ==========")

    for student in students:
        print("----------------------------------")
        for key, value in student.items():
            print(f"{key}: {value}")


# Search student by Roll Number
def search_student():
    students = read_students()

    roll_no = input("Enter Roll Number to Search: ")

    for student in students:
        if student["Roll_No"] == roll_no:
            print("\nStudent Found!")
            for key, value in student.items():
                print(f"{key}: {value}")
            return

    print("Student not found!")


# Update student record
def update_student():
    students = read_students()

    roll_no = input("Enter Roll Number to Update: ")

    for student in students:
        if student["Roll_No"] == roll_no:

            print("\nLeave a field empty to keep its existing value.")

            name = input(f"Enter New Name ({student['Name']}): ")
            student_class = input(f"Enter New Class ({student['Class']}): ")

            if name:
                student["Name"] = name

            if student_class:
                student["Class"] = student_class

            for subject in ["Python", "Mathematics", "Statistics"]:
                new_marks = input(
                    f"Enter New {subject} Marks ({student[subject]}): "
                )

                if new_marks:
                    try:
                        marks = float(new_marks)

                        if 0 <= marks <= 100:
                            student[subject] = marks
                        else:
                            print("Marks must be between 0 and 100.")
                            return

                    except ValueError:
                        print("Invalid marks entered.")
                        return

            save_students(students)

            print("Student record updated successfully!")
            return

    print("Student not found!")


# Delete student record
def delete_student():
    students = read_students()

    roll_no = input("Enter Roll Number to Delete: ")

    for student in students:
        if student["Roll_No"] == roll_no:
            students.remove(student)
            save_students(students)

            print("Student deleted successfully!")
            return

    print("Student not found!")


# Save records to CSV file
def save_students(students):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(students)


# Main menu
def main():
    initialize_file()

    while True:
        print("\n========== MENU ==========")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("Exiting Student Record Management System. Goodbye!")
            break

        else:
            print("Invalid choice! Please select 1-6.")


if __name__ == "__main__":
    main()
