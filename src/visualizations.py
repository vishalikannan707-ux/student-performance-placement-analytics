"""Visualization helpers for student analytics."""

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Load cleaned student dataset
df = pd.read_csv("dataset/students.csv")

# Create output folder
output_dir = Path("outputs/charts")
output_dir.mkdir(parents=True, exist_ok=True)

# 1. Placement Distribution
placement_counts = df["placement_status"].value_counts()

plt.figure(figsize=(7, 5))
placement_counts.plot(
    kind="bar",
    color=["skyblue", "orange"],
    edgecolor="black"
)
plt.title("Student Placement Distribution")
plt.xlabel("Placement Status")
plt.ylabel("Number of Students")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(output_dir / "placement_distribution.png")
plt.show()

print("Chart 1 saved successfully!")



# 2. Department-wise Average Marks

department_avg = df.groupby("department")["marks"].mean().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
department_avg.plot(
    kind="bar",
    color="teal",
    edgecolor="black"
)

plt.title("Department-wise Average Marks")
plt.xlabel("Department")
plt.ylabel("Average Marks")
plt.xticks(rotation=0)
plt.ylim(0, 100)
plt.tight_layout()

plt.savefig(output_dir / "department_average_marks.png")
plt.show()

print("Chart 2 saved successfully!")



# 3. Department-wise Placement Percentage

department_placement = (
    df.assign(is_placed=(df["placement_status"] == "Placed").astype(int))
    .groupby("department")["is_placed"]
    .mean() * 100
)

department_placement = department_placement.sort_values(ascending=False)

plt.figure(figsize=(8, 5))

department_placement.plot(
    kind="bar",
    color="mediumpurple",
    edgecolor="black"
)

plt.title("Department-wise Placement Percentage")
plt.xlabel("Department")
plt.ylabel("Placement Percentage (%)")
plt.xticks(rotation=0)
plt.ylim(0, 100)
plt.tight_layout()

plt.savefig(output_dir / "department_placement_percentage.png")
plt.show()

print("Chart 3 saved successfully!")


# 4. Attendance vs Placement

attendance_avg = df.groupby("placement_status")["attendance"].mean()

plt.figure(figsize=(7, 5))

attendance_avg.plot(
    kind="bar",
    color="cornflowerblue",
    edgecolor="black"
)

plt.title("Average Attendance vs Placement Status")
plt.xlabel("Placement Status")
plt.ylabel("Average Attendance (%)")
plt.xticks(rotation=0)
plt.ylim(0, 100)
plt.tight_layout()

plt.savefig(output_dir / "attendance_vs_placement.png")
plt.show()

print("Chart 4 saved successfully!")


# 5. Study Hours vs Placement

study_hours_avg = df.groupby("placement_status")["study_hours"].mean()

plt.figure(figsize=(7, 5))

study_hours_avg.plot(
    kind="bar",
    color="orange",
    edgecolor="black"
)

plt.title("Average Study Hours vs Placement Status")
plt.xlabel("Placement Status")
plt.ylabel("Average Study Hours")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(output_dir / "study_hours_vs_placement.png")
plt.show()

print("Chart 5 saved successfully!")
