
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# 1. Read cleaned dataset
BASE_DIR = Path(__file__).resolve().parent
df = pd.read_csv(BASE_DIR / "cleaned_student_performance.csv")

# Actual subject columns in your dataset
subjects = ["Math_Score", "Reading_Score", "Writing_Score"]

# Check required columns
for column in subjects:
    if column not in df.columns:
        raise ValueError(f"Missing required column: {column}")

# Create student numbers because the dataset has no Name column
if "Name" not in df.columns and "Student_Number" not in df.columns:
    df.insert(0, "Student_Number", range(1, len(df) + 1))

student_id = "Name" if "Name" in df.columns else "Student_Number"

sns.set_style("whitegrid")

# 2. Calculate Average Score
df["Average_Score"] = df[subjects].mean(axis=1).round(2)

# 3. Assign Performance Categories
def performance_category(score):
    if score >= 90:
        return "Excellent"
    elif score >= 80:
        return "Good"
    elif score >= 70:
        return "Average"
    else:
        return "Needs Improvement"

df["Performance"] = df["Average_Score"].apply(performance_category)

# 4. Total Number of Students
total_students = len(df)

print("\n========== STUDENT PERFORMANCE DASHBOARD ==========")

print("\n1. Total Number of Students:")
print(total_students)

# 5. Average Marks for Each Subject
subject_averages = df[subjects].mean()

print("\n2. Average Marks for Each Subject:")
print(subject_averages.round(2))

# 6. Top 5 Performing Students
top_students = df.nlargest(5, "Average_Score")

print("\n3. Top 5 Performing Students:")
print(
    top_students[
        [student_id, "Average_Score", "Performance"]
    ].to_string(index=False)
)

# 7. Students Who Need Improvement
students_needing_improvement = df[
    df["Performance"] == "Needs Improvement"
]

print("\n4. Students Who Need Improvement:")

if students_needing_improvement.empty:
    print("No students need improvement.")
else:
    print(
        students_needing_improvement[
            [student_id, "Average_Score", "Performance"]
        ].to_string(index=False)
    )

# 8. Subject With Highest Class Average
highest_subject = subject_averages.idxmax()
highest_average = subject_averages.max()

print("\n5. Subject With Highest Class Average:")
print(highest_subject)
print("Class Average:", round(highest_average, 2))

# 9. Performance Category Distribution
print("\n6. Performance Category Distribution:")
print(df["Performance"].value_counts())

# Create charts folder
CHART_DIR = BASE_DIR / "dashboard_charts"
CHART_DIR.mkdir(exist_ok=True)

# 10. Visualization 1: Subject Average Marks
plt.figure(figsize=(8, 5))

sns.barplot(
    x=["Math", "Reading", "Writing"],
    y=subject_averages.values
)

plt.title("Average Marks by Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.ylim(0, 100)

plt.tight_layout()
plt.savefig(CHART_DIR / "subject_averages.png")
plt.show()

# 11. Visualization 2: Top 5 Students
plt.figure(figsize=(9, 5))

sns.barplot(
    x=top_students[student_id].astype(str),
    y=top_students["Average_Score"]
)

plt.title("Top 5 Performing Students")
plt.xlabel("Student Number")
plt.ylabel("Average Score")
plt.ylim(0, 100)

plt.tight_layout()
plt.savefig(CHART_DIR / "top_5_students.png")
plt.show()

# 12. Visualization 3: Performance Distribution
plt.figure(figsize=(7, 7))

performance_order = [
    "Excellent", "Good", "Average", "Needs Improvement"
]

performance_counts = (
    df["Performance"]
    .value_counts()
    .reindex(performance_order, fill_value=0)
)

plt.pie(
    performance_counts,
    labels=performance_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Overall Student Performance")

plt.tight_layout()
plt.savefig(CHART_DIR / "performance_distribution.png")
plt.show()

# 13. Visualization 4: Subject Comparison
plt.figure(figsize=(9, 5))

df[subjects].mean().plot(kind="bar")

plt.title("Comparison of Subject Averages")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.ylim(0, 100)

plt.tight_layout()
plt.savefig(CHART_DIR / "subject_comparison.png")
plt.show()

# 14. Visualization 5: Subject Score Distribution
plt.figure(figsize=(9, 5))

sns.boxplot(data=df[subjects])

plt.title("Score Distribution Across Subjects")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.tight_layout()
plt.savefig(CHART_DIR / "subject_boxplot.png")
plt.show()

# 15. Key Insights
print("\n========== KEY INSIGHTS ==========")

print(
    f"1. The dataset contains {total_students} students."
)

print(
    f"2. {highest_subject} has the highest class average "
    f"of {highest_average:.2f}."
)

print(
    f"3. {len(students_needing_improvement)} students "
    "need improvement."
)

print(
    f"4. The highest student average is "
    f"{df['Average_Score'].max():.2f}."
)

print("\nDashboard Analysis Completed Successfully!")

# Save final analysis
df.to_csv(BASE_DIR / "dashboard_analysis.csv", index=False)

print("\nAnalysis saved as dashboard_analysis.csv")
print("Charts saved in dashboard_charts folder.")
