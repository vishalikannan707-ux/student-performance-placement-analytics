# Student Performance & Placement Analytics

An end-to-end data analytics project that explores student academic performance, attendance, study habits, and placement outcomes using Python, Pandas, NumPy, MySQL, Matplotlib, and Streamlit.

## Project Overview

The Student Performance & Placement Analytics project analyzes a dataset of 200 students to understand academic performance and placement trends.

It combines Python-based data processing, SQL analysis, data visualization, and an interactive Streamlit dashboard to turn raw student data into meaningful insights.

## Objectives

- Analyze student academic performance.
- Understand department-wise performance.
- Compare placement and non-placement outcomes.
- Explore the relationship between attendance and placement.
- Analyze study hours and academic results.
- Present insights through an interactive dashboard.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming |
| NumPy | Numerical analysis |
| Pandas | Data manipulation and cleaning |
| MySQL | Database management |
| SQL | Data analysis and queries |
| Matplotlib | Data visualization |
| Streamlit | Interactive dashboard |
| Pytest | Automated testing |
| Git & GitHub | Version control |

## Project Structure

```text
student-placement-analytics/
│
├── dataset/
│   └── students.csv
│
├── notebooks/
│   └── exploratory_analysis.ipynb
│
├── src/
│   ├── data_loader.py
│   ├── data_cleaning.py
│   ├── numerical_analysis.py
│   ├── sql_connection.py
│   ├── sql_operations.py
│   └── visualizations.py
│
├── database/
│   ├── schema.sql
│   ├── insert_data.sql
│   └── analysis_queries.sql
│
├── dashboard/
│   └── app.py
│
├── outputs/
│   └── charts/
│
├── tests/
│   └── test_data.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Dataset Information

The project uses a synthetic dataset containing 200 student records and 9 columns.

| Column | Description |
|---|---|
| student_id | Unique student ID |
| name | Student name |
| age | Student age |
| gender | Student gender |
| department | Academic department |
| marks | Academic marks |
| attendance | Attendance percentage |
| study_hours | Average study hours |
| placement_status | Placement outcome |

**Note:** This is a synthetic dataset created for educational and analytical purposes. Placement status is generated using the project rule of marks ≥ 65 and attendance ≥ 75.

## Key Analysis Results

| Metric | Result |
|---|---:|
| Total students | 200 |
| Placed students | 52 |
| Not placed students | 148 |
| Overall placement percentage | 26% |
| Average marks | 66.14 |
| Highest marks | 100 |

### Key Insights

- EEE recorded the highest department-wise placement percentage at 38.10%.
- IT recorded the lowest department-wise placement percentage at 20.41%.
- Placed students had average attendance of 87.11%, compared with 72.19% for students who were not placed.
- The placed group had average marks of 83.56, compared with 60.02 for the not-placed group.

These results describe patterns in the synthetic dataset and do not establish real-world causation.

## Data Visualizations

The project generates five visualizations:

1. Placement distribution
2. Department-wise average marks
3. Department-wise placement percentage
4. Attendance vs placement
5. Study hours vs placement

Charts are available in `outputs/charts/`.

## Interactive Dashboard

The Streamlit dashboard provides:

- Total student count
- Placed and not-placed student metrics
- Overall placement percentage
- Department filter
- Student data table
- Five analytical visualizations

## Installation & Execution

### 1. Clone the repository

```bash
git clone https://github.com/vishalikannan707-ux/student-performance-placement-analytics.git
cd student-performance-placement-analytics
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run the Streamlit dashboard

```bash
streamlit run dashboard/app.py
```

### 6. Run automated tests

```bash
python -m pytest tests/test_data.py -v
```

## MySQL Configuration

To use the MySQL integration:

1. Install and start MySQL Server.
2. Open MySQL Workbench.
3. Execute `database/schema.sql`.
4. Create a local `.env` file with your database configuration.

Example `.env`:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=student_analytics
DB_PORT=3306
```

5. Run the database integration scripts as needed.

**Security:** Never upload your actual `.env` file or database password to GitHub.

## Testing

Automated tests are written using Pytest.

Current test coverage includes:

- Dataset record count
- Dataset column count
- Missing values
- Duplicate records
- Unique student IDs
- Valid marks range
- Valid attendance range
- Valid placement status
- Placement count

**Latest test result: 9 passed.**

## Future Improvements

- Add advanced exploratory data analysis.
- Introduce machine learning models for placement prediction.
- Improve dashboard interactivity.
- Deploy the dashboard online.

## Author

AI & ML Engineering Student

**GitHub:** [vishalikannan707-ux](https://github.com/vishalikannan707-ux)

---

If you find this project useful, feel free to explore the repository and its analysis.
