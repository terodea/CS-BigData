package wordcount.lower

import org.apache.log4j.Logger
import org.apache.log4j.Level
import org.apache.spark.SparkContext

object WordCountLowerTopTenOptimized extends App {
  Logger.getLogger("org").setLevel(Level.ERROR)
  val sc = new SparkContext("local[*]", "wordcountLowerTopTen")
  sc.textFile("").
  flatMap(_.split(" ")).
  map(_.toLowerCase()). 
  map((_, 1)).
  reduceByKey(_+_).
  sortBy(x => x._2)
  .collect.
  foreach(println)
}