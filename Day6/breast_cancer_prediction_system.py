import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
# Step 1: Load Dataset
# ==========================================

# Enter your dataset path
dataset_path = r"C:\Users\laiba\Documents\Day6\data.csv"

df = pd.read_csv(dataset_path)

print("\n========== BREAST CANCER PREDICTION SYSTEM ==========")

print("\nDataset Loaded Successfully!")

print("\nDataset Shape:")
print(df.shape)

print("\nFirst Five Rows:")
print(df.head())


# ==========================================
# Step 2: Data Preprocessing
# ==========================================

# Remove unnecessary columns
df = df.drop(columns=["id", "Unnamed: 32"], errors="ignore")

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum().sum())

# Separate features and target
X = df.drop("diagnosis", axis=1)

# Convert diagnosis into numerical values
# Malignant = 1
# Benign = 0

y = df["diagnosis"].str.strip().str.upper().map({
    "M": 1,
    "B": 0
})

if y.isnull().any():
    raise ValueError("Unknown diagnosis labels found.")

# Make sure all features are numeric
X = X.apply(pd.to_numeric, errors="raise")

print("\nFeatures Shape:", X.shape)
print("Target Shape:", y.shape)

print("\nTarget Distribution:")
print(y.value_counts())


# ==========================================
# Step 3: Split Dataset
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining Data:", X_train.shape)
print("Testing Data:", X_test.shape)


# ==========================================
# Step 4: Create Baseline Model
# ==========================================

baseline_model = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression(max_iter=5000))
])

# Train baseline model
baseline_model.fit(X_train, y_train)

# Predict results
baseline_predictions = baseline_model.predict(X_test)


# ==========================================
# Step 5: Baseline Model Evaluation
# ==========================================

def evaluate_model(model_name, actual, predicted):

    print(f"\n========== {model_name} ==========")

    print("Accuracy:",
          accuracy_score(actual, predicted))

    print("Precision:",
          precision_score(actual, predicted))

    print("Recall:",
          recall_score(actual, predicted))

    print("F1 Score:",
          f1_score(actual, predicted))

    print("\nConfusion Matrix:")
    print(confusion_matrix(actual, predicted))

    print("\nClassification Report:")
    print(classification_report(
        actual,
        predicted,
        target_names=["Benign", "Malignant"]
    ))


evaluate_model(
    "BASELINE MODEL",
    y_test,
    baseline_predictions
)


# ==========================================
# Step 6: Hyperparameter Tuning
# ==========================================

print("\n========== GRID SEARCH CV ==========")

param_grid = {
    "model__C": [0.01, 0.1, 1, 10, 100],
    "model__solver": ["liblinear", "lbfgs"],
    "model__penalty": ["l2"]
}

grid_search = GridSearchCV(
    estimator=baseline_model,
    param_grid=param_grid,
    cv=5,
    scoring="recall",
    n_jobs=-1
)

# Find the best model configuration
grid_search.fit(X_train, y_train)

print("\nBest Parameters:")
print(grid_search.best_params_)

print("\nBest Cross Validation Recall:")
print(grid_search.best_score_)


# ==========================================
# Step 7: Tuned Model Evaluation
# ==========================================

best_model = grid_search.best_estimator_

tuned_predictions = best_model.predict(X_test)

evaluate_model(
    "TUNED MODEL",
    y_test,
    tuned_predictions
)


# ==========================================
# Step 8: Compare Both Models
# ==========================================

results = pd.DataFrame({
    "Metric": ["Accuracy", "Precision", "Recall", "F1 Score"],

    "Baseline": [
        accuracy_score(y_test, baseline_predictions),
        precision_score(y_test, baseline_predictions),
        recall_score(y_test, baseline_predictions),
        f1_score(y_test, baseline_predictions)
    ],

    "Tuned": [
        accuracy_score(y_test, tuned_predictions),
        precision_score(y_test, tuned_predictions),
        recall_score(y_test, tuned_predictions),
        f1_score(y_test, tuned_predictions)
    ]
})

print("\n========== FINAL MODEL COMPARISON ==========")
print(results.to_string(index=False))


# ==========================================
# Step 9: Confusion Matrix Heatmap
# ==========================================

cm = confusion_matrix(y_test, tuned_predictions)

plt.figure(figsize=(7, 5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["Benign", "Malignant"],
    yticklabels=["Benign", "Malignant"]
)

plt.title("Breast Cancer Prediction - Tuned Model")
plt.xlabel("Predicted Diagnosis")
plt.ylabel("Actual Diagnosis")

plt.tight_layout()

# Save heatmap
plt.savefig("confusion_matrix.png")

print("\nConfusion Matrix Image Saved Successfully!")

plt.show()


# ==========================================
# Step 10: Sample Prediction
# ==========================================

print("\n========== SAMPLE PREDICTION ==========")

# Select one sample from testing data
sample = X_test.iloc[[0]]

prediction = best_model.predict(sample)

if prediction[0] == 1:
    print("Predicted Result: Malignant")
else:
    print("Predicted Result: Benign")


# ==========================================
# Project Completed
# ==========================================

print("\nBest Model Parameters:")
print(best_model.get_params()["model__C"])
print(best_model.get_params()["model__solver"])

print("\nBreast Cancer Prediction System Completed!")
