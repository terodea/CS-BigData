from pyspark import SparkConf, SQLContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from datetime import datetime
import pyspark.sql.functions as F
from pyspark.sql.types import DateType
from pyspark.sql.window import Window



def main():
    column_list = ["Year", "Month"]
    INPUT_PATH = "/Users/akshayterode/Desktop/DEV/CS-BigData/Case Studies/Equities/ingest/data/202101_202112_NIFTY50.csv"
    df = spark.read.option("header", True).option("inferSchema", True).csv(INPUT_PATH)
    func = F.udf(lambda x: datetime.strptime(x, "%d-%b-%Y"), DateType())
    date_df = df.withColumn("dateTs", func(F.col("Date"))).withColumn("Year", F.year(F.col("dateTs"))).withColumn("Month", F.month(F.col("dateTs")))

    windowSpec  = Window.partitionBy(*column_list).orderBy("dateTs")
    row_no_df = date_df.withColumn("row_no", row_number().over(windowSpec))
    min_max_day = row_no_df.groupBy("Year","Month").agg(F.max(F.col("row_no")).alias("maxWorkingDay"), F.min("row_no").alias("minWorkingDay"))
    open_df =  min_max_day.join(row_no_df, ((row_no_df.Year == min_max_day.Year) & (row_no_df.Month == min_max_day.Month) & ((row_no_df.row_no == min_max_day.minWorkingDay))), "left").select(min_max_day.Year, min_max_day.Month, "Open")
    close_df =  min_max_day.join(row_no_df, ((row_no_df.Year == min_max_day.Year) & (row_no_df.Month == min_max_day.Month) & ((row_no_df.row_no == min_max_day.maxWorkingDay))), "left").select(min_max_day.Year, min_max_day.Month, "Close")

    open_df.join(close_df, ((open_df.Year == close_df.Year) & (open_df.Month == close_df.Month)), "inner").select(open_df.Year, open_df.Month, "Open", "Close").withColumn("ChangeOverMonth", F.round(((F.col("Close") - (F.col("Open")))/F.col("Close"))*100,2)).show()
    
if __name__ == "__main__":
    spark_conf = SparkConf()
    spark_conf.set("spark.app.name", "DataFrameRunTimeErrorExample")
    spark_conf.set("spark.master", "local[2]")
    spark = SparkSession.builder.config(conf=spark_conf).getOrCreate()
    main()
    spark.stop()