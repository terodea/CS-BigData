package rdd.wordcount.lower

import org.apache.spark.SparkContext
import org.apache.log4j.Level
import org.apache.log4j.Logger

object WordCountLower extends App {
  /*
   * A word count program that converts word into lower case.
   * Function Chaining also implemented.
   * 
   * */
  Logger.getLogger("org").setLevel(Level.ERROR)
  val sc = new SparkContext("local[*]", "wordcountLower")
  sc.textFile("").
  flatMap(_.split(" ")).
  map(_.toLowerCase()).
  map((_, 1)).reduceByKey(_+_).collect.foreach(println)
}