package dataframes.customers

import org.apache.spark.SparkConf
import org.apache.spark.sql.SparkSession

object PerCustomerOrderCount extends App{
  /*
   * Problem Statement: Count Orders Placed by a customer having order_customer_id > 10000.
   */
  val sparkConf = new SparkConf()
  sparkConf.set("spark.app.name", "CountOfOrderPerCustomer")
  sparkConf.set("spark.master", "local[2]")
  
  val spark = SparkSession.builder()
  .config(sparkConf)
  .getOrCreate()
  
  val ordersDf = spark.read.
  option("header", true).
  option("inferSchema", true).
  csv("/home/akshay/*/CS-BigData/00-Data/Orders.csv")
  
  val ordersCount = ordersDf.repartition(4).where("order_customer_id > 10000").select("order_id", "order_customer_id").groupBy("order_customer_id").count()
  ordersCount.show()
  scala.io.StdIn.readLine()
  spark.stop()
}