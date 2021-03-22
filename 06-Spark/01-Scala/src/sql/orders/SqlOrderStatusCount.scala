package sql.orders

import org.apache.spark.SparkConf
import org.apache.spark.sql.SparkSession

object SqlOrderStatsCount extends App{
  /*
   *1. Count all order_status.
   *2. Get order_customer_id having closed order_status and their count.  
   */
  val spark_conf = new SparkConf()
  spark_conf.set("spark.app.name", "CountOrderStatus")
  spark_conf.set("spark.master", "local[2]")
  
  val spark = SparkSession.builder().config(spark_conf).getOrCreate()
  
  val ordersDf = spark.read.format("csv").option("header", true).option("inferSchema", true).option("path", "/home/akshay/*/CS-BigData/00-Data/Orders.csv").load()
  
  ordersDf.createOrReplaceTempView("orders")
  spark.sql(
      "SELECT "+
      "order_status, count(order_status) "+
      "FROM orders "+
      "GROUP BY order_status "+
      "ORDER BY count(order_status) DESC;"
      ).show()
  
  spark.sql(
      "SELECT "+
      "order_customer_id, count(order_status) AS total_orders "+
      "FROM orders "+
      "WHERE order_status IN ('CLOSED') GROUP BY order_customer_id ORDER BY total_orders DESC;"
      ).show()
 spark.stop()
}