import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

# Step 1: Load Iris Dataset

file_path = r"C:\Users\laiba\Documents\Day5\Iris.csv"

df = pd.read_csv(file_path)

print("\nOriginal Dataset:")
print(df.head())


# Step 2: Explore Dataset

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nFlower Species:")
print(df["Species"].value_counts())

print("\nMissing Values:")
print(df.isnull().sum())


# Step 3: Prepare Dataset

# Remove Id column because it is not useful for prediction
df = df.drop(columns=["Id"], errors="ignore")

# Remove rows with missing values
df = df.dropna()

# Separate input features and target
X = df.drop(columns=["Species"])
y = df["Species"]


# Step 4: Split Dataset

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining Data:", X_train.shape)
print("Testing Data:", X_test.shape)


# Step 5: Feature Scaling

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# Step 6: Train Logistic Regression

logistic_model = LogisticRegression(max_iter=1000)

logistic_model.fit(X_train_scaled, y_train)

print("\nLogistic Regression Model Trained Successfully!")


# Step 7: Make Predictions

y_pred = logistic_model.predict(X_test_scaled)


# Step 8: Evaluate Logistic Regression

accuracy = accuracy_score(y_test, y_pred)

precision = precision_score(
    y_test, y_pred, average="weighted"
)

recall = recall_score(
    y_test, y_pred, average="weighted"
)

f1 = f1_score(
    y_test, y_pred, average="weighted"
)

print("\n========== LOGISTIC REGRESSION ==========")

print(f"Accuracy:  {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
print(f"F1-Score:  {f1:.4f}")


# Step 9: Classification Report

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# Step 10: Confusion Matrix

cm = confusion_matrix(
    y_test,
    y_pred,
    labels=logistic_model.classes_
)

plt.figure(figsize=(7, 5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=logistic_model.classes_,
    yticklabels=logistic_model.classes_
)

plt.title("Iris - Logistic Regression Confusion Matrix")
plt.xlabel("Predicted Species")
plt.ylabel("Actual Species")

plt.tight_layout()

plt.savefig("iris_confusion_matrix.png")

plt.show()


# Step 11: Actual vs Predicted Values

results = pd.DataFrame({
    "Actual": y_test,
    "Predicted": y_pred
})

print("\n========== SAMPLE PREDICTIONS ==========")
print(results.head(10))


# Step 12: Bonus - Train Decision Tree

tree_model = DecisionTreeClassifier(random_state=42)

tree_model.fit(X_train, y_train)

tree_pred = tree_model.predict(X_test)


# Step 13: Evaluate Decision Tree

tree_accuracy = accuracy_score(y_test, tree_pred)

tree_precision = precision_score(
    y_test, tree_pred, average="weighted"
)

tree_recall = recall_score(
    y_test, tree_pred, average="weighted"
)

tree_f1 = f1_score(
    y_test, tree_pred, average="weighted"
)

print("\n========== DECISION TREE ==========")

print(f"Accuracy:  {tree_accuracy:.4f}")
print(f"Precision: {tree_precision:.4f}")
print(f"Recall:    {tree_recall:.4f}")
print(f"F1-Score:  {tree_f1:.4f}")


# Step 14: Compare Both Models

comparison = pd.DataFrame({
    "Metric": ["Accuracy", "Precision", "Recall", "F1-Score"],

    "Logistic Regression": [
        accuracy,
        precision,
        recall,
        f1
    ],

    "Decision Tree": [
        tree_accuracy,
        tree_precision,
        tree_recall,
        tree_f1
    ]
})

print("\n========== MODEL COMPARISON ==========")
print(comparison.to_string(index=False))


# Step 15: Visualize Model Comparison

comparison.set_index("Metric").plot(
    kind="bar",
    figsize=(9, 5)
)

plt.title("Logistic Regression vs Decision Tree")
plt.ylabel("Performance Score")
plt.ylim(0, 1.1)
plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig("model_comparison.png")

plt.show()

