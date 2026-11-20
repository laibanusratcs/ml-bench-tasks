
import pandas as pd

# Load the CSV dataset
df = pd.read_csv("students.csv")

print("\n========== STUDENT DATASET ==========")
print(df)


# Display basic information
print("\n========== DATASET INFORMATION ==========")

print("First 5 Rows:")
print(df.head())

print("\nLast 5 Rows:")
print(df.tail())

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
df.info()

print("\nMissing Values:")
print(df.isnull().sum())


# Define subject columns
subjects = ["Python", "Mathematics", "Statistics"]

# Handle missing values in subject columns
for subject in subjects:
    df[subject] = pd.to_numeric(df[subject], errors="coerce")
    df[subject] = df[subject].fillna(df[subject].mean())


# Handle missing student names
df["Name"] = df["Name"].fillna("Unknown")


# Calculate average marks for each subject
print("\n========== SUBJECT AVERAGES ==========")

for subject in subjects:
    average = df[subject].mean()
    print(f"Average {subject} Marks: {average:.2f}")


# Calculate each student's average marks
df["Average"] = df[subjects].mean(axis=1)


# Display top 5 performing students
print("\n========== TOP 5 STUDENTS ==========")

top_students = df.sort_values(
    by="Average",
    ascending=False
).head(5)

print(top_students[["Name"] + subjects + ["Average"]])


# Calculate class average
class_average = df["Average"].mean()

print("\nClass Average:", round(class_average, 2))


# Find students scoring below average
print("\n========== STUDENTS BELOW AVERAGE ==========")

below_average = df[df["Average"] < class_average]

if below_average.empty:
    print("No students scored below the class average.")
else:
    print(below_average[["Name"] + subjects + ["Average"]])


# Display total number of students
total_students = len(df)

print("\nTotal Number of Students:", total_students)


# Save processed dataset
df.to_csv("processed_students.csv", index=False)

print("\nProcessed dataset saved successfully!")
