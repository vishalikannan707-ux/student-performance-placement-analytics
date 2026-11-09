-- Add student performance and placement analysis queries here.
USE student_analytics;

SELECT
    department,
    COUNT(*) AS total_students,
    ROUND(AVG(marks), 2) AS average_marks
FROM students
GROUP BY department-- 2. Placement Status Analysis

SELECT
    placement_status,
    COUNT(*) AS total_students
FROM students
GROUP BY placement_status;
ORDER BY average_marks DESC;

-- 3. Overall Placement Percentage

SELECT
    COUNT(*) AS total_students,
    SUM(placement_status = 'Placed') AS placed_students,
    ROUND(
        SUM(placement_status = 'Placed') * 100.0 / COUNT(*),
        2
    ) AS placement_percentage
FROM students; 

-- 4. Attendance vs Placement Analysis

SELECT
    placement_status,
    ROUND(AVG(attendance), 2) AS average_attendance,
    COUNT(*) AS total_students
FROM students
GROUP BY placement_status
ORDER BY average_attendance DESC;

-- 5. Top 10 Performing Students

SELECT
    student_id,
    name,
    department,
    marks,
    attendance,
    study_hours,
    placement_status
FROM students
ORDER BY marks DESC
LIMIT 10;

-- 6. Department-wise Placement Analysis

SELECT
    department,
    COUNT(*) AS total_students,
    SUM(placement_status = 'Placed') AS placed_students,
    SUM(placement_status = 'Not Placed') AS not_placed_students,
    ROUND(
        SUM(placement_status = 'Placed') * 100.0 / COUNT(*),
        2
    ) AS placement_percentage
FROM students
GROUP BY department
ORDER BY placement_percentage DESC;

-- 7. Study Hours vs Placement Analysis

SELECT
    placement_status,
    COUNT(*) AS total_students,
    ROUND(AVG(study_hours), 2) AS average_study_hours,
    ROUND(AVG(marks), 2) AS average_marks
FROM students
GROUP BY placement_status
ORDER BY average_study_hours DESC;