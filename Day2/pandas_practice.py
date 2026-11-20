import pandas as pd

# Read CSV file
df = pd.read_csv("students.csv")

# Display all student records
print("Student Records:")
print(df)

# Display first 5 records
print("\nFirst 5 Students:")
print(df.head())

# Display basic information
print("\nDataset Information:")
print(df.info())

# Calculate average marks in each subject
print("\nAverage Marks:")
print(df[["Python", "Mathematics", "Statistics"]].mean())

# Display highest marks in each subject
print("\nHighest Marks:")
print(df[["Python", "Mathematics", "Statistics"]].max())