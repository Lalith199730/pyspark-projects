# PySpark Projects

A collection of real-world data engineering pipelines built with PySpark.

## Project 1 — Employee Data Pipeline

### What it does
- Reads raw employee CSV data
- Removes bad records (salary = 0)
- Adds salary band column (High, Mid, Low)
- Writes clean data as Parquet partitioned by department

### Tech stack
- PySpark
- Python
- Parquet

### How to run
1. Install PySpark: `pip install pyspark`
2. Add your `employees.csv` file
3. Run: `python employee_pipeline.py`

### What I learned
- Building end-to-end PySpark pipelines
- Data cleaning with filter and withColumn
- Writing optimised Parquet output with partitioning
