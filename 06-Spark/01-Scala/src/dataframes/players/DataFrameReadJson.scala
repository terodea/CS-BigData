package dataframes.players

import org.apache.spark.SparkConf
import org.apache.spark.sql.SparkSession

object DataFrameReadJson extends App{
  val spark_conf = new SparkConf()
  spark_conf.set("spark.app.name", "ReadJsonDataFrame")
  spark_conf.set("spark.master", "local[2]")
  
  val spark = SparkSession.builder().config(spark_conf).getOrCreate()
  val playersDf = spark.read.format("json").option("path", "/home/akshay/*/CS-BigData/00-Data/Players.json").load
  playersDf.show()
  playersDf.printSchema()
}