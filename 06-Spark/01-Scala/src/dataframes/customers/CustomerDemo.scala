package dataframes.customers

import org.apache.spark.SparkConf
import org.apache.spark.sql.SparkSession

object CustomerDemo extends App{
  /*
   * Demo code for spark data frame.
   * Don't use inferSchema in production.
   * 
   * Driver Converts DataFrame code into low level RDD code and send's it to the executor for execution. 
   */
  val sparkConf = new SparkConf()
  sparkConf.set("spark.app.name", "CustomersDf")
  sparkConf.set("spark.master", "local[2]")
  
  val spark = SparkSession.builder()
  .config(sparkConf)
  .getOrCreate()
  
  val ordersDf = spark.read
  .option("header", true)
  .option("inferSchema", true)
  .csv("/home/akshay/*/CS-BigData/00-Data/Orders.csv")
  
  ordersDf.show()
  ordersDf.printSchema()
  spark.stop()
}