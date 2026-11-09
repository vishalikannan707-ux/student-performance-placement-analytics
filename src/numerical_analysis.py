"""Numerical analysis for student performance and placement data."""

import numpy as np
import pandas as pd

from data_cleaning import clean_data


def analyze_student_performance(df):

    # Clean the dataset
    df = clean_data(df)

    # Convert marks into a NumPy array
    marks = df["marks"].to_numpy()

    # Basic statistical analysis
    mean_marks = np.mean(marks)
    median_marks = np.median(marks)
    highest_marks = np.max(marks)
    lowest_marks = np.min(marks)
    standard_deviation = np.std(marks)

    # Count students above and below average
    above_average = np.sum(marks > mean_marks)
    below_average = np.sum(marks < mean_marks)

    # Placement analysis using NumPy
    placed_count = np.sum(df["placement_status"].to_numpy() == "Placed")
    not_placed_count = np.sum(
        df["placement_status"].to_numpy() == "Not Placed"
    )

    # Department-wise average marks
    department_analysis = df.groupby("department")["marks"].mean()

    # Display results
    print("\n========== STUDENT PERFORMANCE ANALYSIS ==========")

    print("\nMARKS STATISTICS")
    print(f"Average Marks: {mean_marks:.2f}")
    print(f"Median Marks: {median_marks:.2f}")
    print(f"Highest Marks: {highest_marks}")
    print(f"Lowest Marks: {lowest_marks}")
    print(f"Standard Deviation: {standard_deviation:.2f}")

    print("\nSTUDENT PERFORMANCE")
    print(f"Students Above Average: {above_average}")
    print(f"Students Below Average: {below_average}")

    print("\nPLACEMENT ANALYSIS")
    print(f"Placed Students: {placed_count}")
    print(f"Not Placed Students: {not_placed_count}")

    print("\nDEPARTMENT-WISE AVERAGE MARKS")
    print(department_analysis.round(2))

    return {
        "mean_marks": mean_marks,
        "median_marks": median_marks,
        "highest_marks": highest_marks,
        "lowest_marks": lowest_marks,
        "standard_deviation": standard_deviation,
        "above_average": above_average,
        "below_average": below_average,
        "placed_count": placed_count,
        "not_placed_count": not_placed_count,
        "department_analysis": department_analysis
    }


if __name__ == "__main__":

    # Load dataset
    df = pd.read_csv("dataset/students.csv")

    # Perform analysis
    results = analyze_student_performance(df)
