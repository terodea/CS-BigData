from pyspark import SparkConf, SQLContext
from pyspark.sql import SparkSession, group
from pyspark.sql.functions import *
from pyspark.sql.window import Window
import os

def main():
    # invoiceDf = spark.read.option("header", True).option("inferSchema", True).csv(f"{os.environ.get('DATA_PATH')}/WindowData.csv")
    invoiceDf = spark.read\
        .format("csv")\
            .option("header", True)\
                .option("inferSchema", True)\
                    .option("path",f"{os.environ.get('DATA_PATH')}/WindowData.csv")\
                        .load()

    my_window = Window.partitionBy("country").orderBy("weeknum").rowsBetween(Window.unboundedPreceding, Window.currentRow)
    
    invoiceDf.withColumn("RunningTotal", sum("invoicevalue").over(my_window)).show()

if __name__ == '__main__':
    spark_conf = SparkConf()
    spark_conf.set("spark.app.name", "DataFrameRunTimeErrorExample")
    spark_conf.set("spark.master", "local[2]")
    spark = SparkSession.builder.config(conf=spark_conf).getOrCreate()
    main()
    spark.stop()