
import pandas as pd
import matplotlib.pyplot as plt

from data_preprocessing import main as preprocess_data

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def main():

    # Step 1: Preprocess the dataset
    print("\nStep 1: Data Preprocessing")
    preprocess_data()

    # Step 2: Load cleaned dataset
    file_path = r"C:\Users\laiba\Documents\Data Processing and Machine Learning\student_performance_cleaned.csv"

    df = pd.read_csv(file_path)

    # Step 3: Select numerical and categorical features
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

    # Input features
    X = df[numerical_features + categorical_features]

    # Target variable
    y = df["Average_Score"]

    # Step 4: Split dataset (80% training, 20% testing)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42
    )

    # Step 5: Preprocess numerical and categorical data
    preprocessor = ColumnTransformer(
        transformers=[
            ("numeric", StandardScaler(), numerical_features),
            ("categorical", OneHotEncoder(handle_unknown="ignore"),
             categorical_features)
        ]
    )

    # Step 6: Create Linear Regression model
    model = Pipeline([
        ("preprocessor", preprocessor),
        ("regressor", LinearRegression())
    ])

    # Step 7: Train the model
    print("\nStep 2: Training Linear Regression Model")
    model.fit(X_train, y_train)

    # Step 8: Make predictions
    y_pred = model.predict(X_test)

    # Step 9: Evaluate the model
    print("\nStep 3: Model Evaluation")

    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print("Mean Absolute Error (MAE):", round(mae, 4))
    print("Mean Squared Error (MSE):", round(mse, 4))
    print("R2 Score:", round(r2, 4))

    # Step 10: Compare actual and predicted scores
    results = pd.DataFrame({
        "Actual Score": y_test.values,
        "Predicted Score": y_pred
    })

    print("\nActual vs Predicted Scores:")
    print(results.round(2))

    # Save prediction results
    results.to_csv("actual_vs_predicted.csv", index=False)

    # Step 11: Visualize predictions
    plt.figure(figsize=(8, 6))

    plt.scatter(y_test, y_pred, label="Predicted Scores")

    minimum = min(y_test.min(), y_pred.min())
    maximum = max(y_test.max(), y_pred.max())

    plt.plot(
        [minimum, maximum],
        [minimum, maximum],
        color="red",
        linestyle="--",
        label="Perfect Prediction"
    )

    plt.xlabel("Actual Average Score")
    plt.ylabel("Predicted Average Score")
    plt.title("Actual vs Predicted Student Scores")
    plt.legend()
    plt.grid(True)

    plt.savefig("actual_vs_predicted.png")
    plt.show()

    print("\nStudent Score Prediction System completed successfully!")
    print("Prediction results saved in actual_vs_predicted.csv")
    print("Graph saved as actual_vs_predicted.png")


if __name__ == "__main__":
    main()
