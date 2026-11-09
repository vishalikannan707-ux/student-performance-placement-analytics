# Student Performance Placement Analytics

Project scaffold for exploring student performance and placement data.

## Project structure

```text
dataset/
  students.csv
notebooks/
  exploratory_analysis.ipynb
src/
  __init__.py
  data_loader.py
  data_cleaning.py
  numerical_analysis.py
  sql_connection.py
  sql_operations.py
  visualizations.py
database/
  schema.sql
  insert_data.sql
  analysis_queries.sql
dashboard/
  app.py
outputs/
  charts/
tests/
  test_data.py
.env
.gitignore
requirements.txt
README.md
```

Add the student dataset to `dataset/students.csv`. Keep local configuration in
`.env`; it is excluded from version control.
