"""Tests for student data loading and processing."""

import pandas as pd
from pathlib import Path

# Load dataset
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = BASE_DIR / "dataset" / "students.csv"

df = pd.read_csv(DATA_PATH)


def test_dataset_has_200_records():
    assert len(df) == 200


def test_dataset_has_9_columns():
    assert len(df.columns) == 9


def test_no_missing_values():
    assert df.isnull().sum().sum() == 0


def test_no_duplicate_records():
    assert df.duplicated().sum() == 0


def test_student_id_is_unique():
    assert df["student_id"].is_unique


def test_marks_are_in_valid_range():
    assert df["marks"].between(0, 100).all()


def test_attendance_is_in_valid_range():
    assert df["attendance"].between(0, 100).all()


def test_placement_status_values():
    valid_status = {"Placed", "Not Placed"}
    assert set(df["placement_status"].unique()).issubset(valid_status)


def test_placement_count():
    assert (df["placement_status"] == "Placed").sum() == 52
