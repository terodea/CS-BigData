from pyspark import SparkConf, broadcast
from pyspark import sql
from pyspark.sql import SparkSession
from pyspark.sql.functions import broadcast
import os

def main():
    """
    Avoiding Shuffling for inner join (Shuffle, merge, join) using broadcast.
    Let's consider three node Spark Cluster. Key 1 resides in Node 1 for ordersDf and Node 2 for customersDf, etc. for this
    situation data has to be shuffled and then merged. Avoid this by broadcast.
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

        ordersDf.join(broadcast(customerDf), ordersDf.order_customer_id == customerDf.customer_id, "inner").show()

    except Exception as e:
        raise e

if __name__ == '__main__':
    spark_conf = SparkConf()
    spark_conf.set("spark.app.name", "Week12Session22")
    spark_conf.set("spark.master", "local[2]")
    spark = SparkSession.builder.config(conf=spark_conf).getOrCreate()
    main()
    spark.stop()