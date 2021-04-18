from pyspark import SparkConf
from pyspark.sql import SparkSession
import os

def main():
    """
    """
    try:
        # bigLog = spark.read.option("header", True).csv(f"{os.environ.get('DATA_PATH')}/bigLog.txt") ## This work fine too..
        bigLog = spark.read.format("csv")\
            .option("header", True)\
                .option("path", f"{os.environ.get('DATA_PATH')}/bigLog.txt")\
                    .load()
        bigLog.createOrReplaceTempView("bigLogTable")

        spark.sql(
            f"""SELECT level, date_format(datetime, 'MMMM') as month, cast(first(date_format(datetime, 'M')) as int) as monthnum, count(1) as total FROM bigLogTable GROUP BY level, month order by monthnum, level"""
        ).show()

    except Exception as e:
        raise e

if __name__ == "__main__":
    spark_conf = SparkConf()
    spark_conf.set("spark.app.name", "Week12Session23")
    spark_conf.set("spark.main", "local[2]")
    spark = SparkSession.builder.config(conf=spark_conf).getOrCreate()
    main()
    spark.stop()