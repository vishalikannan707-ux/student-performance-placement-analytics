"""Dashboard entry point."""

import streamlit as st
import pandas as pd
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = BASE_DIR / "dataset" / "students.csv"
CHART_DIR = BASE_DIR / "outputs" / "charts"

# Page configuration
st.set_page_config(
    page_title="Student Placement Analytics",
    page_icon="🎓",
    layout="wide"
)

# Load dataset
df = pd.read_csv(DATA_PATH)

# Dashboard title
st.title("🎓 Student Performance & Placement Analytics")
st.write("An interactive dashboard to explore student performance and placement insights.")

st.divider()

# Key metrics
total_students = len(df)
placed_students = (df["placement_status"] == "Placed").sum()
not_placed_students = (df["placement_status"] == "Not Placed").sum()
placement_percentage = (placed_students / total_students) * 100

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Students", total_students)
col2.metric("Placed Students", placed_students)
col3.metric("Not Placed", not_placed_students)
col4.metric("Placement Rate", f"{placement_percentage:.2f}%")

st.divider()

# Department filter
st.subheader("Department Analysis")

departments = ["All Departments"] + sorted(df["department"].unique().tolist())

selected_department = st.selectbox(
    "Select Department",
    departments
)

if selected_department == "All Departments":
    filtered_df = df
else:
    filtered_df = df[df["department"] == selected_department]

st.write(f"Showing {len(filtered_df)} students")

st.dataframe(filtered_df, use_container_width=True)

st.divider()

# Display visualizations
st.subheader("Placement Analytics Charts")

chart_files = [
    ("Placement Distribution", "placement_distribution.png"),
    ("Department Average Marks", "department_average_marks.png"),
    ("Department Placement Percentage", "department_placement_percentage.png"),
    ("Attendance vs Placement", "attendance_vs_placement.png"),
    ("Study Hours vs Placement", "study_hours_vs_placement.png")
]

for title, filename in chart_files:
    chart_path = CHART_DIR / filename

    st.subheader(title)

    if chart_path.exists():
        st.image(str(chart_path), use_container_width=True)
    else:
        st.warning(f"Chart not found: {filename}")

st.success("Dashboard loaded successfully!")
