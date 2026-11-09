-- Define the database schema here.

-- Create the database
CREATE DATABASE IF NOT EXISTS student_analytics;

-- Select the database
USE student_analytics;

-- Create students table
CREATE TABLE IF NOT EXISTS students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(20),
    department VARCHAR(50),
    marks INT,
    attendance DECIMAL(5,2),
    study_hours DECIMAL(4,1),
    placement_status VARCHAR(30)
);
