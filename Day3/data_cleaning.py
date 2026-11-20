
import pandas as pd

# 1. Load dataset
df = pd.read_csv("StudentsPerformance.csv")

print("Original Dataset:")
print(df.head())

# 2. Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 3. Handle missing values
# Fill missing numerical values with column mean
numeric_columns = ["math score", "reading score", "writing score"]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")
    df[column] = df[column].fillna(df[column].mean())

# Fill missing categorical values
categorical_columns = [
    "gender",
    "race/ethnicity",
    "parental level of education",
    "lunch",
    "test preparation course"
]

for column in categorical_columns:
    df[column] = df[column].fillna("Unknown")

# 4. Remove duplicate records
print("\nDuplicate Records:", df.duplicated().sum())

df = df.drop_duplicates()

# 5. Rename columns
df = df.rename(columns={
    "gender": "Gender",
    "race/ethnicity": "Race_Ethnicity",
    "parental level of education": "Parental_Education",
    "lunch": "Lunch",
    "test preparation course": "Test_Preparation",
    "math score": "Math_Score",
    "reading score": "Reading_Score",
    "writing score": "Writing_Score"
})

# 6. Create a new column for average score
subjects = ["Math_Score", "Reading_Score", "Writing_Score"]

df["Average_Score"] = df[subjects].mean(axis=1)

# 7. Create performance categories
def performance_category(score):
    if score >= 80:
        return "Excellent"
    elif score >= 60:
        return "Good"
    elif score >= 40:
        return "Average"
    else:
        return "Needs Improvement"

df["Performance"] = df["Average_Score"].apply(performance_category)

# 8. Sort students by average score
df = df.sort_values(by="Average_Score", ascending=False)

# 9. Display cleaned dataset
print("\nCleaned Dataset:")
print(df.head())

# 10. Save cleaned dataset
df.to_csv("cleaned_student_performance.csv", index=False)

print("\nData cleaning completed successfully!")
print("Cleaned dataset saved as cleaned_student_performance.csv")
