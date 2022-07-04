from pyspark.sql import Trigger, SparkSession
from pyspark.sql.functions import from_json
spark = SparkSession.builder.master("local[2]").appName("My Streaming App").getOrCreate()

raw_data = spark.readStream.format("kafka").option("kafka.bootstrap.servers", value=[]).option("subscribe", "topic").load()
parsed_data = raw_data.selectExpr("cast((value as string) as json)").select(from_json("json", schema=[]).as("data")).select("data.*")
query = parsed_data.writeStream.option("checkpointLocation", "/checkpoint").partitionBy("date").format("parquet").start("/parquetTable")