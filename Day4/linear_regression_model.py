
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Enter the path of your cleaned CSV file
file_path = r"C:\Users\laiba\Documents\Data Processing and Machine Learning\student_performance_cleaned.csv"

# Load dataset
df = pd.read_csv(file_path)

# Select numerical and categorical features
numerical_features = [
    "math score",
    "reading score",
    "writing score"
]

categorical_features = [
    "gender",
    "race/ethnicity",
    "parental level of education",
    "lunch",
    "test preparation course"
]

# Input features (X)
X = df[numerical_features + categorical_features]

# Target variable (y)
y = df["Average_Score"]

# Split data into training (80%) and testing (20%)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

# Preprocess numerical and categorical features
preprocessor = ColumnTransformer(
    transformers=[
        ("numeric", StandardScaler(), numerical_features),
        ("categorical", OneHotEncoder(handle_unknown="ignore"), categorical_features)
    ]
)

# Create Linear Regression pipeline
model = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", LinearRegression())
])

# Train the model
print("\nTraining Linear Regression Model...")
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model
print("\nModel Evaluation Results")
print("------------------------")

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Absolute Error (MAE):", round(mae, 4))
print("Mean Squared Error (MSE):", round(mse, 4))
print("R2 Score:", round(r2, 4))

# Compare actual and predicted values
results = pd.DataFrame({
    "Actual Score": y_test.values,
    "Predicted Score": y_pred
})

print("\nActual vs Predicted Scores:")
print(results)

# Save results
results.to_csv("actual_vs_predicted.csv", index=False)

print("\nModel training completed successfully!")
print("Prediction results saved in actual_vs_predicted.csv")
