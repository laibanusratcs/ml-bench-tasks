
def calculate_average(students):
    total = 0

    for name, marks in students.items():
        total += marks

    average = total / len(students)
    return average


def count_word_frequency(sentence):
    words = sentence.split()
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


def display_student_record(student):
    print(student)
    print("Name:", student["name"])
    print("Course:", student["course"])


students = {
    "Ali": 85,
    "Sara": 90,
    "Ahmed": 75,
    "Ayesha": 80
}

sentence = "python is easy and python is powerful"

student = {
    "name": "Laiba",
    "roll_number": 101,
    "age": 24,
    "course": "Computer Science"
}

print("Average marks:", calculate_average(students))

print("Word frequency:", count_word_frequency(sentence))

display_student_record(student)

# Average Marks
# students = {
#     "Ali": 85,
#     "Sara": 90,
#     "Ahmed": 75,
#     "Ayesha": 80
# }

# total = 0

# for name, marks in students.items():
#     total += marks

# average = total / len(students)

# print("Average marks:", average)

# Frequency
# sentence = "python is easy and python is powerful"

# words = sentence.split()

# frequency = {}

# for word in words:
#     if word in frequency:
#         frequency[word] += 1
#     else:
#         frequency[word] = 1

# print(frequency)

# Students Record
# student = {
#     "name": "Laiba",
#     "roll_number": 101,
#     "age": 24,
#     "course": "Computer Science"
# }

# print(student)
# print("Name:", student["name"])
# print("Course:", student["course"])