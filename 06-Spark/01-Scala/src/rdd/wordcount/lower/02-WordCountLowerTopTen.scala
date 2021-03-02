package rdd.wordcount.lower

import org.apache.log4j.Logger
import org.apache.log4j.Level
import org.apache.spark.SparkContext

object WordContLowerTopTen extends App {
  Logger.getLogger("org").setLevel(Level.ERROR)
  val sc = new SparkContext("local[*]", "wordcountLowerTopTen")
  sc.textFile("").
  flatMap(_.split(" ")).
  map(_.toLowerCase()). 
  map((_, 1)).
  reduceByKey(_+_).
  map(x => (x._2, x._1)).
  sortByKey(false).
  map(x => (x._2, x._1)).
  collect.
  foreach(println)
}