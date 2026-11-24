import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

# Step 1: Load Dataset
# Provide the location of your downloaded CSV file

file_path = r"C:\Users\laiba\Documents\Day5\breast_cancer_dataset.csv"

df = pd.read_csv(file_path)

print("\nOriginal Dataset:")
print(df.head())


# Step 2: Explore Dataset

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDiagnosis Distribution:")
print(df["diagnosis"].value_counts())


# Step 3: Data Preprocessing

# Remove unnecessary columns
df = df.drop(columns=["id", "Unnamed: 32"], errors="ignore")

# Remove rows with missing target values
df = df.dropna(subset=["diagnosis"])

# Separate features and target
X = df.drop(columns=["diagnosis"])
y = df["diagnosis"]

# Convert diagnosis into numerical values
# B = 0 (Benign), M = 1 (Malignant)
y = y.map({"B": 0, "M": 1})


# Step 4: Split Dataset into Training and Testing Sets

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

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# Step 6: Train Logistic Regression Model

model = LogisticRegression(max_iter=2000)

model.fit(X_train, y_train)

print("\nLogistic Regression Model Trained Successfully!")


# Step 7: Make Predictions

y_pred = model.predict(X_test)


# Step 8: Evaluate Model Performance

accuracy = accuracy_score(y_test, y_pred)

precision = precision_score(y_test, y_pred)

recall = recall_score(y_test, y_pred)

f1 = f1_score(y_test, y_pred)

print("\n========== MODEL EVALUATION ==========")

print(f"Accuracy:  {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
print(f"F1-Score:  {f1:.4f}")


# Step 9: Classification Report

print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred,
    target_names=["Benign", "Malignant"]
))


# Step 10: Generate Confusion Matrix

cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(7, 5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["Benign", "Malignant"],
    yticklabels=["Benign", "Malignant"]
)

plt.title("Breast Cancer Confusion Matrix")
plt.xlabel("Predicted Diagnosis")
plt.ylabel("Actual Diagnosis")

plt.tight_layout()

plt.savefig("confusion_matrix.png")

plt.show()


# Step 11: Compare Actual and Predicted Values

results = pd.DataFrame({
    "Actual": y_test.map({0: "Benign", 1: "Malignant"}),
    "Predicted": pd.Series(y_pred, index=y_test.index).map({
        0: "Benign",
        1: "Malignant"
    })
})

print("\n========== SAMPLE PREDICTIONS ==========")
print(results.head(10))

print("\nClassification Practice Completed!")
