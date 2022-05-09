from pyspark import SparkConf, SQLContext
from pyspark.sql import SparkSession, group
from pyspark.sql.functions import *
import os

def main():
    """
    Grouping Aggregrates
    1. Column Object Expression
    2. String Object Expression
    3. SparkSQL
    """
    # 1. Column Object Expression
    DATA_PATH = "/Users/akshayterode/Desktop/DEV/CS-BigData/00-Data"
    invoiceDf = spark.read.option("header", True).option("inferSchema", True).csv(f"{DATA_PATH}/OrderData.csv")
    invoiceDf.groupBy("Country", "InvoiceNo").agg(
        sum("Quantity").alias("TotalQuantity"), round(sum(expr("Quantity * UnitPrice")),2).alias("InvoiceValue")
    ).show()

    # 2. String Object Expression
    invoiceDf.groupBy("Country", "InvoiceNo").agg(
        expr("sum(Quantity) as TotalQuantity"), expr("sum(Quantity * UnitPrice) as InvoiceValue")
    ).show()

    # 3. SparkSQL
    invoiceDf.createOrReplaceTempView("sales")
    spark.sql(f"""SELECT 
        Country, InvoiceNo, sum(Quantity) as TotalQuantity, sum(Quantity * UnitPrice) as InvoiceValue 
        FROM sales 
        GROUP BY Country, InvoiceNo;"""
    ).show()
    
if __name__ == '__main__':
    spark_conf = SparkConf()
    spark_conf.set("spark.app.name", "DataFrameRunTimeErrorExample")
    spark_conf.set("spark.master", "local[2]")
    spark = SparkSession.builder.config(conf=spark_conf).getOrCreate()
    main()
    spark.stop()
