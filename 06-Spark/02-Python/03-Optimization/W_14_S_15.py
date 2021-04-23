import os
from pyspark.sql import SparkSession
from pyspark import SparkConf


def main():
    """
    """
    try:
        # WIll be added soon
        pass
    except Exception as e:
        raise e

if __name__ == '__main__':
    spark_conf = SparkConf()
    spark_conf.set("spark.app.name", "RepartitionVsCoalesce")
    spark_conf.set("spark.master", "local[2]")
    spark = SparkSession.builder.config(conf=spark_conf).getOrCreate()
    main()
