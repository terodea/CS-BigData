package dataframes.users

import org.apache.spark.SparkConf
import org.apache.spark.sql.SparkSession

object DataFrameReadParquet extends App{
  /*
   * Default Format is parquet in apache spark.
   */
  val spark_conf = new SparkConf()
  spark_conf.set("spark.app.name", "ReadParquetExample")
  spark_conf.set("spark.master","local[2]")
  
  val spark = SparkSession.builder().config(spark_conf).getOrCreate()
  
  val usersDf = spark.read.option("path", "/home/akshay/*/CS-BigData/00-Data/Users.parquet").load
  usersDf.printSchema()
  usersDf.show(false)
  spark.stop()
}

