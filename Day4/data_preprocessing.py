
import pandas as pd

def main():

    # Enter your CSV file path
    file_path = r"C:\Users\laiba\Documents\Data Processing and Machine Learning\StudentsPerformance.csv"

    # Load dataset
    df = pd.read_csv(file_path)

    print("\nOriginal Dataset:")
    print(df.head())

    # Check missing values
    print("\nMissing Values:")
    print(df.isnull().sum())

    # Remove duplicate records
    df = df.drop_duplicates()

    # Clean column names
    df.columns = df.columns.str.strip().str.lower()

    # Subject columns
    subjects = ["math score", "reading score", "writing score"]

    # Convert subject scores into numeric values
    for subject in subjects:
        df[subject] = pd.to_numeric(df[subject], errors="coerce")

        # Fill missing values with median
        df[subject] = df[subject].fillna(df[subject].median())

    # Calculate average score
    df["Average_Score"] = df[subjects].mean(axis=1)

    # Create performance categories
    def get_performance(score):
        if score >= 90:
            return "Excellent"
        elif score >= 80:
            return "Good"
        elif score >= 70:
            return "Average"
        else:
            return "Needs Improvement"

    df["Performance"] = df["Average_Score"].apply(get_performance)

    # Save cleaned dataset
    output_file = r"C:\Users\laiba\Documents\Data Processing and Machine Learning\student_performance_cleaned.csv"

    df.to_csv(output_file, index=False)

    print("\nCleaned Dataset:")
    print(df.head())

    print("\nPreprocessing completed successfully!")
    print("Saved file:", output_file)


if __name__ == "__main__":
    main()
