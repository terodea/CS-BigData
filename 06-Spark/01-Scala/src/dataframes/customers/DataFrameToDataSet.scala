package dataframes.customers


import org.apache.spark.SparkConf
import org.apache.spark.sql.SparkSession
import java.sql.Date
import org.apache.spark.sql.Row
import org.apache.spark.sql.Dataset
import java.sql.Timestamp

case class OrdersData (order_id: Int, order_date: String, order_customer_id: Integer, order_status: String)

object DataFrameToDataSet extends App{
  val spark_conf = new SparkConf()
  spark_conf.set("spark.app.name", "DataFrameToDataSetConversion")
  spark_conf.set("spark.master", "local[2]")
  
  val spark = SparkSession.builder().config(spark_conf).getOrCreate()
  val ordersDf: Dataset[Row] = spark.read.option("header", true).option("inferSchema", true).csv("/home/akshay/*/CS-BigData/00-Data/Orders.csv")
  
  import spark.implicits._
  val ordersDs = ordersDf.as[OrdersData]
  ordersDs.filter(x => x.order_id < 10).show()
  // ordersDs.filter(x => x.order_ids < 100) // Gives CompileTimeError
}