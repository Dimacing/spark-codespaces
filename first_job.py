from pyspark.sql import SparkSession, functions as F

spark = (
    SparkSession.builder
    .appName("first-job")
    .master("local[*]")
    .getOrCreate()
)

orders = spark.range(0, 2_000_000).select(
    (F.col("id") % 5).alias("city_id"),
    (F.col("id") % 1000).alias("amount"),
)

result = orders.groupBy("city_id").agg(F.sum("amount").alias("revenue")).orderBy("city_id")
result.show()

input("Spark UI открыт на порту 4040. Нажмите Enter, чтобы завершить работу...")
spark.stop()
