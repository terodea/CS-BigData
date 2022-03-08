__doc__ = """"""
from pyspark import SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split

def main():
    lines = spark \
    .readStream \
    .format("socket") \
    .option("host", "localhost") \
    .option("port", 9999) \
    .load()


    words = lines.select(
        explode(
            split(lines.value, " ")
        ).alias("word")
    )

    # Generate running word count
    wordCounts = words.groupBy("word").count()

    query = wordCounts \
    .writeStream \
    .outputMode("complete") \
    .format("console") \
    .option("checkpointLocation", "/tmp") \
    .start()

    query.awaitTermination()

if __name__ == "__main__":
    spark_conf = SparkConf()
    spark_conf.set("spark.app.name", "Structured Streaming")
    spark_conf.set("spark.main", "local[2]")
    spark = SparkSession.builder.config(conf=spark_conf).getOrCreate()
    main()
