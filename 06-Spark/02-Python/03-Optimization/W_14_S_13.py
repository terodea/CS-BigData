import os
from pyspark import SparkConf
from pyspark.sql import SparkSession

def main():
    """
    Task: Join Orders and Customers data.
    By default structured API's are designed to operate in broadcast join for inner join if one of the dataframe is small.
    We disable the BroadCast join in spark_conf attribute.
    If you observe the TaskTracker UI, you'll find that more than 200 tasks are scheduled.
    Because Structured API's are given 200 tasks by default when shuffling is involved.
    This can be disabled/handled by Admins in Spark Configuration.
    Note: Increase Customers Data as close to 2.5 GB of data.
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
                    .option("path",f"{os.environ.get('DATA_PATH')}/OrdersSmall.csv")\
                        .load()

        ordersDf.join(customerDf, ordersDf.order_customer_id == customerDf.customer_id, "inner").show()
    except Exception:
        raise

if __name__ == '__main__':
    spark_conf = SparkConf()
    spark_conf.set("spark.app.name", "DataFrameBroadCastJoin")
    spark_conf.set("spark.master", "local[2]")
    spark_conf.set("spark.sql.autoBroadcastJoinThreshold", -1) # Disable BroadCast for small data in Structured API
    spark = SparkSession.builder.config(conf=spark_conf).getOrCreate()
    main()