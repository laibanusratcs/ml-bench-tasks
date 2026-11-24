
# ==========================================
# Day 6 - Coding Practice
# Model Evaluation and Hyperparameter Tuning
# ==========================================

import pandas as pd

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)


# ==========================================
# Step 1: Load and Explore Dataset
# ==========================================

# Give the path of your dataset here
dataset_path = r"C:\Users\laiba\Documents\Day6\data.csv"

# Read CSV file
df = pd.read_csv(dataset_path)

print("\n========== DATASET EXPLORATION ==========")

# Display first 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# Display dataset information
print("\nDataset Information:")
df.info()

# Display statistical summary
print("\nStatistical Description:")
print(df.describe())

# Remove unnecessary columns
df = df.drop(columns=["id", "Unnamed: 32"], errors="ignore")

# Check target distribution
print("\nTarget Distribution:")
print(df["diagnosis"].value_counts())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum().sum())


# ==========================================
# Step 2: Prepare Data
# ==========================================

# Separate features and target
X = df.drop("diagnosis", axis=1)

y = df["diagnosis"].str.strip().str.upper().map({
    "M": 1,
    "B": 0
})

# Check whether target conversion was successful
if y.isnull().any():
    raise ValueError("Unknown target labels found. Check diagnosis column.")

# 1 = Malignant
# 0 = Benign

print("\nFeatures Shape:", X.shape)
print("Target Shape:", y.shape)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# ==========================================
# Step 3: Build Baseline Model
# ==========================================

# Create a pipeline for scaling and Logistic Regression
baseline_model = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression(max_iter=5000))
])

# Train the model
baseline_model.fit(X_train, y_train)

# Make predictions
baseline_predictions = baseline_model.predict(X_test)


# ==========================================
# Step 4: Evaluate Baseline Model
# ==========================================

print("\n========== BASELINE MODEL RESULTS ==========")

print("Accuracy:",
      accuracy_score(y_test, baseline_predictions))

print("Precision:",
      precision_score(y_test, baseline_predictions))

print("Recall:",
      recall_score(y_test, baseline_predictions))

print("F1 Score:",
      f1_score(y_test, baseline_predictions))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, baseline_predictions))

print("\nClassification Report:")
print(classification_report(
    y_test,
    baseline_predictions,
    target_names=["Benign", "Malignant"]
))


# ==========================================
# Step 5: Hyperparameter Tuning
# ==========================================

print("\n========== HYPERPARAMETER TUNING ==========")

# Different parameter combinations to test
param_grid = {
    "model__C": [0.01, 0.1, 1, 10, 100],
    "model__solver": ["liblinear", "lbfgs"],
    "model__penalty": ["l2"]
}

# Create GridSearchCV
grid_search = GridSearchCV(
    estimator=baseline_model,
    param_grid=param_grid,
    cv=5,
    scoring="recall",
    n_jobs=-1
)

# Train and search for the best parameters
grid_search.fit(X_train, y_train)

# Display best parameters
print("\nBest Parameters:")
print(grid_search.best_params_)

print("\nBest Cross Validation Recall:")
print(grid_search.best_score_)


# ==========================================
# Step 6: Evaluate Tuned Model
# ==========================================

best_model = grid_search.best_estimator_

tuned_predictions = best_model.predict(X_test)

print("\n========== TUNED MODEL RESULTS ==========")

print("Accuracy:",
      accuracy_score(y_test, tuned_predictions))

print("Precision:",
      precision_score(y_test, tuned_predictions))

print("Recall:",
      recall_score(y_test, tuned_predictions))

print("F1 Score:",
      f1_score(y_test, tuned_predictions))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, tuned_predictions))


# ==========================================
# Step 7: Compare Both Models
# ==========================================

comparison = pd.DataFrame({
    "Metric": ["Accuracy", "Precision", "Recall", "F1 Score"],

    "Baseline Model": [
        accuracy_score(y_test, baseline_predictions),
        precision_score(y_test, baseline_predictions),
        recall_score(y_test, baseline_predictions),
        f1_score(y_test, baseline_predictions)
    ],

    "Tuned Model": [
        accuracy_score(y_test, tuned_predictions),
        precision_score(y_test, tuned_predictions),
        recall_score(y_test, tuned_predictions),
        f1_score(y_test, tuned_predictions)
    ]
})

print("\n========== MODEL COMPARISON ==========")
print(comparison.to_string(index=False))

print("\nCoding Practice Completed Successfully!")
