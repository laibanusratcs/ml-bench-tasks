
students = []

def add_student():

    print("\n    Add Student    ") 

    name = input("Enter student name: ").strip()

    if name == "":
        print("Name cannot be empty.")
        return

    roll_number = input("Enter roll number: ").strip()

    if not roll_number.isdigit():
        print("Roll number must be a number.")
        return

    roll_number = int(roll_number)
    for student in students:
        if student["roll_number"] == roll_number:
            print("This roll number already exists.")
            return

    age = input("Enter age: ").strip()

    if not age.isdigit() or int(age) <= 0:
        print("Please enter a valid age.")
        return

    age = int(age)

    course = input("Enter course: ").strip()

    if course == "":
        print("Course cannot be empty.")
        return

    student = {
        "name": name,
        "roll_number": roll_number,
        "age": age,
        "course": course
    }

    students.append(student)

    print("\nStudent added successfully!")


def view_students():

    print("\n    All Students    ")

    if len(students) == 0:
        print("No student records found.")
        return

    for student in students:
        print("\n                 ")
        print("Name:", student["name"])
        print("Roll Number:", student["roll_number"])
        print("Age:", student["age"])
        print("Course:", student["course"])


def search_student():

    print("\n    Search Student    ")

    roll_number = input("Enter roll number: ").strip()

    if not roll_number.isdigit():
        print("Invalid roll number.")
        return

    roll_number = int(roll_number)

    for student in students:
        if student["roll_number"] == roll_number:

            print("\nStudent Found!")
            print("Name:", student["name"])
            print("Roll Number:", student["roll_number"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            return

    print("Student not found.")



def update_student():

    print("\n    Update Student    ")

    roll_number = input("Enter roll number: ").strip()

    if not roll_number.isdigit():
        print("Invalid roll number.")
        return

    roll_number = int(roll_number)

    for student in students:

        if student["roll_number"] == roll_number:

            print("\nStudent Found!")
            print("Leave a field empty if you don't want to change it.")

            new_name = input("Enter new name: ").strip()

            if new_name != "":
                student["name"] = new_name

            new_age = input("Enter new age: ").strip()

            if new_age != "":
                if new_age.isdigit() and int(new_age) > 0:
                    student["age"] = int(new_age)
                else:
                    print("Invalid age. Keeping old age.")

            new_course = input("Enter new course: ").strip()

            if new_course != "":
                student["course"] = new_course

            print("\nStudent information updated successfully!")
            return

    print("Student not found.")


def delete_student():

    print("\n    Delete Student    ")

    roll_number = input("Enter roll number: ").strip()

    if not roll_number.isdigit():
        print("Invalid roll number.")
        return

    roll_number = int(roll_number)

    for student in students:

        if student["roll_number"] == roll_number:

            students.remove(student)

            print("Student deleted successfully!")
            return

    print("Student not found.")


def total_students():

    print("\nTotal Students:", len(students))


while True:

    print("\n      STUDENT RECORD MANAGEMENT SYSTEM      ")

    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Display Total Students")
    print("7. Exit")

    choice = input("\nEnter your choice: ")

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
        total_students()

    elif choice == "7":
        print("Thank you for using the Student Management System!")
        break

    else:
        print("Invalid choice. Please select from 1 to 7.")
