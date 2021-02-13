package movies

import org.apache.log4j.Level
import org.apache.log4j.Logger
import org.apache.spark.SparkContext

object MovieRatingOptimized extends App{
  /*
   * Problem Statement: Get Count of all ratings, where ratings are from 1-5 (inclusive of both), without using reduceByKey.
   */
  Logger.getLogger("org").setLevel(Level.ERROR)
  val sc = new SparkContext("local[*]", "MovieRatingsOptimized")
  sc.textFile("/home/akshay/xflow/personal/CS-BigData/00-Data/MovieData.data").
  map(x => x.split("\t")(2)).
  countByValue.
  foreach(println)  
}
