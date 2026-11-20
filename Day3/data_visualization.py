
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load cleaned dataset
df = pd.read_csv(r"C:\Users\laiba\Documents\Task3-Data Cleaning and Visualization\cleaned_student_performance.csv")

# Create charts folder
os.makedirs("charts", exist_ok=True)

sns.set_theme(style="whitegrid")

subjects = ["Math_Score", "Reading_Score", "Writing_Score"]

# 1. Bar Chart: Average marks by subject
subject_averages = df[subjects].mean()

plt.figure(figsize=(8, 5))
sns.barplot(x=subject_averages.index, y=subject_averages.values)

plt.title("Average Marks by Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.savefig("charts/average_marks.png")
plt.show()

# 2. Histogram: Average score distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["Average_Score"], bins=10, kde=True)

plt.title("Distribution of Average Scores")
plt.xlabel("Average Score")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("charts/average_score_histogram.png")
plt.show()

# 3. Scatter Plot: Math vs Reading
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x="Math_Score",
    y="Reading_Score"
)

plt.title("Math Score vs Reading Score")
plt.xlabel("Math Score")
plt.ylabel("Reading Score")
plt.tight_layout()
plt.savefig("charts/math_vs_reading.png")
plt.show()

# 4. Pie Chart: Performance categories
performance_counts = df["Performance"].value_counts()

plt.figure(figsize=(7, 7))
plt.pie(
    performance_counts,
    labels=performance_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Student Performance Categories")
plt.tight_layout()
plt.savefig("charts/performance_pie_chart.png")
plt.show()

# 5. Boxplot: All subjects
plt.figure(figsize=(8, 5))

sns.boxplot(data=df[subjects])

plt.title("Score Distribution by Subject")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.tight_layout()
plt.savefig("charts/subject_boxplot.png")
plt.show()

print("All visualizations created successfully!")
print("Check the charts folder for PNG files.")
