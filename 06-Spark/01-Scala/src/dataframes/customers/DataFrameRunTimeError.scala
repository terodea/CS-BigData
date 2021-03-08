package dataframes.customers

import org.apache.spark.SparkConf
import org.apache.spark.sql.SparkSession

object DataFrameRunTimeError extends App{
  val spark_conf = new SparkConf()
  spark_conf.set("spark.app.name", "RunTimeErrorDataFrame")
  spark_conf.set("spark.master", "local[2]")
  
  val spark = SparkSession.builder().config(spark_conf).getOrCreate()
  val ordersDf = spark.read.option("header", true).option("inferSchema", true).csv("/home/akshay/*/CS-BigData/00-Data/Orders.csv")
  ordersDf.where("order_customer_id > 10000").show()
}