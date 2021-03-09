package dataframes.customers

import org.apache.spark.SparkConf
import org.apache.spark.SparkContext
import org.apache.spark.sql.SparkSession

object DataFrameStandard extends App{
  val spark_conf = new SparkConf()
  spark_conf.set("spark.app.name", "DataFameStandardBoilerPlate")
  spark_conf.set("spark.master","local[2]")
  
  val spark = SparkSession.builder().config(spark_conf).getOrCreate()
  val ordersDf = spark.read.format("csv").option("header", true).option("inferSchema", true).option("path", "/home/akshay/*/CS-BigData/00-Data/Orders.csv").load
  ordersDf.show()
  ordersDf.printSchema()
  spark.stop()
  
}