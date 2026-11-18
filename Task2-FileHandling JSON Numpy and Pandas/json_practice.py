
import json

students = [
    {"id": 1, "name": "Ali", "age": 22, "marks": 85},
    {"id": 2, "name": "Sara", "age": 21, "marks": 92}
]

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

with open("students.json", "r") as file:
    students = json.load(file)

for student in students:
    print(student)

for student in students:
    if student["id"] == 1:
        student["marks"] = 95

students.append({
    "id": 3,
    "name": "Ahmed",
    "age": 23,
    "marks": 78
})

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

print("Updated students:", students)
