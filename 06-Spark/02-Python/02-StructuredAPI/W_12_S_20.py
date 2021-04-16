from pyspark.sql import SparkSession
from pyspark import SparkConf
from pyspark.sql.functions import expr
import os

def main():
    """
    1. Ambiguity Problem: Same column gives ambiguity error.
    2. Null Values Handling.
    """
    try:
        customerDf = spark.read.format("csv")\
            .option("header", True)\
                .option("inferSchema", True)\
                    .option("path",f"{os.environ.get('DATA_PATH')}/Customers.csv")\
                        .load()
        ordersDf = spark.read.format("csv")\
            .option("header", True)\
                .option("inferSchema", True)\
                    .option("path",f"{os.environ.get('DATA_PATH')}/Orders.csv")\
                        .load()
                        
        ordersDf = ordersDf.withColumnRenamed('order_customer_id', 'customer_id')
        
        # 1: Ambiguity: Both ordersDf and customerDf have customer_id as column name in them. Will raise error if customer_id is selected to display.

        # Raise Error:
        # ordersDf.join(customerDf, ordersDf.customer_id == customerDf.customer_id, "outer").select("customer_id")

        ## Solution: Rename The column
        ordersDf = ordersDf.withColumnRenamed("customer_id", "cust_id")
        ordersDf.join(customerDf, ordersDf.cust_id == customerDf.customer_id, "outer")\
            .select("customer_id","order_id", "cust_id").show()

        ## Solution: Drop the columns
        ordersDf = ordersDf.withColumnRenamed("cust_id", "customer_id")
        ordersDf.join(customerDf, ordersDf.customer_id == customerDf.customer_id, "outer")\
            .drop(ordersDf.customer_id)\
                .select("customer_id", "order_id")\
                    .show()

        # 2: Handling Null Values:
        ordersDf.join(customerDf, ordersDf.customer_id == customerDf.customer_id, "outer")\
            .drop(ordersDf.customer_id).sort("order_id")\
                .withColumn("order_id", expr("coalesce(order_id, -1)"))\
                    .show()

    except Exception as e:
        raise e

if __name__ == '__main__':
    spark_conf = SparkConf()
    spark_conf.set("spark.app.name", "Week12Session20")
    spark_conf.set("spark.master", "local[2]")
    spark = SparkSession.builder.config(conf=spark_conf).getOrCreate()
    main()
    spark.stop()
