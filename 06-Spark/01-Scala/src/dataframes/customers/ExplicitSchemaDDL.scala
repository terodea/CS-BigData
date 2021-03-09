package dataframes.customers

import org.apache.spark.SparkConf
import org.apache.spark.sql.SparkSession

object ExplicitSchemaDDL extends App{
  val customers_schema = "orderid Int, orderdate String, customerid Int, status String"
  val spark_conf = new SparkConf()
  spark_conf.set("spark.app.name", "ExplicitSchemaDDL")
  spark_conf.set("spark.master", "local[2]")
  
  val spark = SparkSession.builder().config(spark_conf).getOrCreate()
  val ordersDf = spark.read.format("csv").option("header", true).schema(customers_schema).option("path", "/home/akshay/xflow/personal/CS-BigData/00-Data/Orders.csv").load
  ordersDf.show()
  spark.stop()
  
}