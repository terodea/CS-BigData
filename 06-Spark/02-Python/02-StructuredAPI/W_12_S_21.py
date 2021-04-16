from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark import SparkConf
import os


def main():
    """
    Week12Session21
    """
    try:
        pass
    except Exception as e:
        raise e


if __name__ == '__main__':
    spark_conf = SparkConf()
    spark_conf.set("spark.app.name", "Week12Session21")
    spark_conf.set("spark.master", "local[2]")
    spark = SparkSession.builder.config(conf=spark_conf).getOrCreate()
    main()
    spark.stop()
