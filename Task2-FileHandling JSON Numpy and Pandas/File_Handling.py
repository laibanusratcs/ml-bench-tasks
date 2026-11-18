
from pathlib import Path

file_path = Path("students.txt")

with open(file_path, "w") as file:
    file.write("Ali\n")
    file.write("Sara\n")
    file.write("Ahmed\n")

with open(file_path, "r") as file:
    print(file.read())

with open(file_path, "a") as file:
    file.write("Laiba\n")

with open(file_path, "r") as file:
    lines = file.readlines()

print("Updated records:")
print("".join(lines))
print("Total lines:", len(lines))
