"""Database operations for student analytics."""

import pandas as pd

from sql_connection import create_connection


def insert_student_data():

    # Load CSV dataset
    df = pd.read_csv("dataset/students.csv")

    connection = create_connection()

    if connection is None:
        print("Database connection unavailable.")
        return

    cursor = connection.cursor()

    # SQL INSERT query
    query = """
        INSERT INTO students
        (student_id, name, age, gender, department,
         marks, attendance, study_hours, placement_status)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    try:
        # Convert DataFrame into records
        records = [
            tuple(row)
            for row in df.itertuples(index=False, name=None)
        ]

        # Insert all records
        cursor.executemany(query, records)

        connection.commit()

        print("Student records inserted successfully!")
        print("Total records inserted:", cursor.rowcount)

    except Exception as error:
        connection.rollback()
        print("Data insertion failed:", error)

    finally:
        cursor.close()
        connection.close()
        print("Database connection closed.")


if __name__ == "__main__":
    insert_student_data()
