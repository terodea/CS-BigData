package dataframes.players

import org.apache.spark.SparkConf
import org.apache.spark.sql.SparkSession

object ReadMalFormedJson extends App{
  /*
   * Malformed Json can be handled using three read modes:
   * 1. PERMISSIVE: default, set all fields to null when it encounters a corrupted record.
   * 2. DROPMALFORMED: Will ignore the malformed record.
   * 3. FAILFAST: Raise Exception for malformed string.
   */
  val spark_conf = new SparkConf()
  spark_conf.set("spark.app.name", "ReadMalformedJson")
  spark_conf.set("spark.master", "local[2]")
  
  val spark = SparkSession.builder().config(spark_conf).getOrCreate()
  
  val playersDf = spark.read.format("json").option("path", "/home/akshay/*/CS-BigData/00-Data/PlayersMalformed.json")
  playersDf.load.show(false) // Json Read Mode: PERMISSIVE
  
  playersDf.option("mode", "DROPMALFORMED").load.show() // Json Read Mode: DROPMALFORMED
  /*
   * Below JSON Read Mode will raise an Exception.
   */
  playersDf.option("mode", "FAILFAST").load.show() // Json Read Mode: FAILFAST 
}