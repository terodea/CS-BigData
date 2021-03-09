package dataframes.customers

import org.apache.spark.SparkConf
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.types.IntegerType
import org.apache.spark.sql.types.StringType
import org.apache.spark.sql.types.StructField
import org.apache.spark.sql.types.StructType

object ExplicitSchema extends App{
  /*
   * Provide spark data types in Programmatic Explicit schema definition.
   */
  val spark_conf = new SparkConf()
  spark_conf.set("spark.app.name", "ExplicitSchema")
  spark_conf.set("spark.master", "local[2]")
  
  val spark = SparkSession.builder().config(spark_conf).getOrCreate()
  val customers_schema = StructType(List(StructField("orderid", IntegerType),StructField("orderdate", StringType),StructField("customerid", IntegerType),StructField("status", StringType)))
  val ordersDf = spark.read.format("csv").option("header", true).schema(customers_schema).option("path", "/home/akshay/xflow/personal/CS-BigData/00-Data/Orders.csv").load
  ordersDf.show()
  spark.stop()
}