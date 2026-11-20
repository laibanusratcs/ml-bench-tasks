name = input("Enter student name: ")
student_class = input("Enter class: ")

num_subjects = int(input("Enter number of subjects: "))

subjects = {}
total_marks = 0

for i in range(num_subjects):
    subject = input(f"Enter subject {i + 1} name: ")
    
    marks = float(input(f"Enter marks for {subject}: "))

    while marks < 0 or marks > 100:
        print("Marks should be between 0 and 100.")
        marks = float(input(f"Enter marks for {subject}: "))

    subjects[subject] = marks
    total_marks += marks

average = total_marks / num_subjects


if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "F"


print("\n    STUDENT RESULT      ")

print("Student Name:", name)
print("Class:", student_class)

print("\nSubject Marks:")

for subject, marks in subjects.items():
    print(subject, ":", marks)

print("\nTotal Marks:", total_marks)
print("Average Marks:", round(average, 2))
print("Grade:", grade)


