from pyspark import SparkConf, SQLContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import os

def main():
    """
    Simple Aggregrators
    """
    invoiceDf = spark.read.\
        option("header", True)\
            .option("inferSchema", True)\
                .csv(f"{os.environ.get('DATA_PATH')}/OrderData.csv")
                
    # Column Object Expression
    invoiceDf.select(
        count("*").alias("RowCount"), sum("Quantity").alias("TotalQuantity"), avg("UnitPrice").alias("AvgPrice"), countDistinct("InvoiceNo").alias("CountDistinct")
    ).show()

    # String Expression
    invoiceDf.selectExpr(
        "count(*) as RowCount",
        "sum(Quantity) as TotalQuantity",
        "avg(UnitPrice) as AvgPrice",
        "count(Distinct(InvoiceNo)) as CountDistint"
    ).show()

    invoiceDf.selectExpr(
        "count(StockCode) as RowCount",
        "sum(Quantity) as TotalQuantity",
        "avg(UnitPrice) as AvgPrice",
        "count(Distinct(InvoiceNo)) as CountDistint"
    ).show()

    # SQL Version

    invoiceDf.createOrReplaceTempView("sales")
    """
    Query to be used when values are needed in nearest two precision points.
    SELECT 
    COUNT(*) as RowCount, CAST(SUM(Quantity) AS DECIMAL(10,2)) as QuantitySum, 
    CAST(AVG(UnitPrice) AS DECIMAL(10,2)) as AvgUnitPrice, COUNT(DISTINCT(InvoiceNo)) as DistinctInvoiceNo 
    FROM sales;
    """
    spark.sql(
        "SELECT COUNT(*) AS RowCount, SUM(Quantity) AS QuantitySum, AVG(UnitPrice) AS AvgUnitPrice, COUNT(DISTINCT(InvoiceNo)) AS DistinctInvoiceNo FROM sales;"
    ).show()

if __name__ == '__main__':
    spark_conf = SparkConf()
    spark_conf.set("spark.app.name", "DataFrameRunTimeErrorExample")
    spark_conf.set("spark.master", "local[2]")
    spark = SparkSession.builder.config(conf=spark_conf).getOrCreate()
    main()
    spark.stop()