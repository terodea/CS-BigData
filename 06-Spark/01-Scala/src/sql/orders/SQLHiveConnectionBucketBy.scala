package sql.orders

import org.apache.spark.SparkConf
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.SaveMode

object SQLHiveConnectionBucketBy extends App{
  
  val spark_conf = new SparkConf()
  spark_conf.set("spark.app.name", "SparkHiveBucketBy")
  spark_conf.set("spark.master", "local[2]")
  
  val spark = SparkSession.builder().config(spark_conf).enableHiveSupport().getOrCreate()
  
  val ordersDf = spark.read.format("csv")
  .option("header", true)
  .option("inferSchema", true)
  .option("path", "/home/akshay/xflow/personal/CS-BigData/00-Data/Orders.csv").load()
  
  spark.sql("create database if not exists retail")
  
  ordersDf.write.format("csv")
  .mode(SaveMode.Overwrite)
  .bucketBy(4,"order_customer_id")
  .sortBy("order_customer_id")
  .saveAsTable("retail.orders")
  
  spark.catalog.listTables("retail").show()
  spark.close()
}