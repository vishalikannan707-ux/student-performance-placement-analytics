"""Database connection helpers."""

import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()


def create_connection():

    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            port=int(os.getenv("DB_PORT", 3306))
        )

        if connection.is_connected():
            print("MySQL connection successful!")
            return connection

    except mysql.connector.Error as error:
        print("MySQL connection failed:", error)

    return None


if __name__ == "__main__":

    connection = create_connection()

    if connection:
        print("Connected Database:", connection.database)
        connection.close()
        print("Connection closed successfully.")
