from pyspark import SparkConf, SQLContext
from pyspark.sql import SparkSession

if __name__ == '__main__':
    spark_conf = SparkConf()
    spark_conf.set("spark.app.name", "DataFrameRunTimeErrorExample")
    spark_conf.set("spark.master", "local[2]")

    spark = SparkSession.builder.config(conf=spark_conf).getOrCreate()

    ordersDf = spark.read.option("header", True).option("inferSchema", True).csv("/home/akshay/*/CS-BigData/00-Data/Orders.csv")
    
    ordersDf.where("order_customer_ids > 10000").show() # Funny thing python gives RunTimeError only :P