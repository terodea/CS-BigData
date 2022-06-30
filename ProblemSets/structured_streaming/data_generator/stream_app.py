from tkinter import E
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, window
from pyspark.sql.types import StructField, StructType, IntegerType, StringType, TimestampType
from pyspark.sql import functions as F

def main():
    try:
        spark = SparkSession.builder.master("local[2]").appName("My Streaming App").getOrCreate()
        lines_df = spark.readStream.format("socket").option("host", "localhost").option("port", "12345").load()
        words_df = lines_df.selectExpr("EXPLODE(SPLIT(value, ' ')) AS word")
        counts_df = words_df.groupBy("word").count()
        word_count_query = counts_df.writeStream.format("console").outputMode("complete").option("checkpointLocation", "check_pt_1").start()
        word_count_query.awaitTermination()
    except Exception as err:
        raise err

if __name__ == "__main__":
    main()
