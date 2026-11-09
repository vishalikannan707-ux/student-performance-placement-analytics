"""Load student data from the project dataset."""

import numpy as np
import pandas as pd

# 1. Generate reproducible data
np.random.seed(42)

n = 200

names = [
    "Arun", "Priya", "Vijay", "Swetha", "Kavin",
    "Divya", "Rahul", "Meena", "Hari", "Nithya",
    "Ajay", "Keerthi", "Sanjay", "Anu", "Karthik"
]

departments = ["AI&ML", "CSE", "ECE", "EEE", "IT"]

# 2. Create DataFrame
df = pd.DataFrame({
    "student_id": range(1, n + 1),
    "name": [
        np.random.choice(names) + f"_{i}"
        for i in range(1, n + 1)
    ],
    "age": np.random.randint(18, 23, n),
    "gender": np.random.choice(["Male", "Female"], n),
    "department": np.random.choice(departments, n),
    "marks": np.random.randint(35, 101, n),
    "attendance": np.round(
        np.random.uniform(50, 100, n), 2
    ),
    "study_hours": np.round(
        np.random.uniform(1, 10, n), 1
    )
})

# 3. Determine placement status
df["placement_status"] = np.where(
    (df["marks"] >= 65) &
    (df["attendance"] >= 75),
    "Placed",
    "Not Placed"
)

# 4. Export dataset
df.to_csv("dataset/students.csv", index=False)

# 5. Display results
print("Dataset generated successfully!")
print(df.head())
print("\nDataset shape:", df.shape)
print("\nColumns:", df.columns.tolist())
