import os
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import *

def main():
    """
    1.
        StructuredAPI have BroadCast join invoked automatically when a smaller dataset/dataframe is involved.
        One can observe this in SparkUI. (Shuffling won't be allowed)
        However care must be taken if smaller dataset doesn't occupy your executor memory.
    2. 
        Also it's good to specify schema explicitly.
    3. 
        How to handle data greater than executor memory or edge node.
        a) specify --driver-memory 4G (according to your requirement.)
        b) Writing/ Save to disk is the best option as it doesn't require data to be loaded in RAM.
    
    --num-executors
    --driver-memory
    --executor-memory
    --executor-cores
    """
    try:
        orders_schema = StructType(
            fields=[
                StructField("order_id", IntegerType(), True),
                StructField("order_date", TimestampType(), True),
                StructField("order_customer_id", IntegerType(), True),
                StructField("order_status", StringType(), True)
            ]
        )
        orderDf = spark.read.format("csv")\
            .schema(schema=orders_schema)\
                .option("header", True)\
                    .option("path", f"{os.environ.get('DATA_PATH')}/OrdersSmall.csv")\
                        .load()
        customerDf = spark.read.format("csv")\
            .option("header", True)\
                .option("inferSchema", True)\
                    .option("path",f"{os.environ.get('DATA_PATH')}/Customers.csv")\
                        .load()

        customerDf.join(orderDf, orderDf.order_customer_id == customerDf.customer_id).collect()
    except Exception as e:
        raise e

if __name__ == '__main__':
    spark_conf = SparkConf()
    spark_conf.set("spark.app.name", "DataFrameBroadcastJoin")
    spark_conf.set("spark.master", "local[2]")
    spark = SparkSession.builder.config(conf=spark_conf).getOrCreate()
    main()
