from pyspark import SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.window import Window
import os
from pyspark.sql import functions

def main():
    customerDf = spark.read.format("csv").option("header", True).option("inferSchema", True).option(
        "path",f"{os.environ.get('DATA_PATH')}/Customers.csv"
    ).load()
    ordersDf = spark.read.format("csv").option("header", True).option("inferSchema", True).option(
        "path",f"{os.environ.get('DATA_PATH')}/Orders.csv"
    ).load()

    customerDf.join(ordersDf, ordersDf.order_customer_id == customerDf.customer_id,"inner").show()

if __name__ == '__main__':
    spark_conf = SparkConf()
    spark_conf.set("spark.app.name", "Week12Session19")
    spark_conf.set("spark.master", "local[2]")
    spark = SparkSession.builder.config(conf=spark_conf).getOrCreate()
    main()
    spark.stop()
