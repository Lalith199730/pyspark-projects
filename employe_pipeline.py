# 1. Create SparkSession
spark = SparkSession.builder.appName("Revise").getOrCreate()

# 2. Read CSV
df = spark.read.csv("employees.csv", header=True, inferSchema=True)

# 3. Clean (filter out bad rows)
df_clean = df.filter(col("salary") > 0)

# 4. Add column (salary band)
df_clean = df_clean.withColumn(
    "salary_band",
    when(col("salary") > 70000, "High")
    .when(col("salary") > 40000, "Mid")
    .otherwise("Low")
)

# 5. Group by department
df_grouped = df_clean.groupBy("department").agg(
    avg("salary").alias("avg_salary"),
    count("*").alias("employee_count")
)

# 6. Write Parquet
df_clean.write.mode("overwrite").parquet("output/clean_employees/")
df_grouped.write.mode("overwrite").parquet("output/department_summary/")

print("Pipeline completed!")
