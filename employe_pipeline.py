from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

spark = SparkSession.builder \
    .appName("EmployeePipeline") \
    .getOrCreate()

df = spark.read.csv("employees.csv",
                     header=True,
                     inferSchema=True)

df_clean = df.filter(col("salary") > 0) \
             .withColumn("salary_band",
                 when(col("salary") >= 90000, "High")
                 .when(col("salary") >= 65000, "Mid")
                 .otherwise("Low")
             )

df_clean.write.mode("overwrite") \
              .partitionBy("department") \
              .parquet("output/employees/")

print("Pipeline complete!")
