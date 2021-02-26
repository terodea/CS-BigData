package movies

import org.apache.log4j.Level
import org.apache.log4j.Logger
import org.apache.spark.SparkContext

object MovieRating extends App{
  /*
   * Problem Statement: Get Count of all ratings, where ratings are from 1-5 (inclusive of both).
   */
  Logger.getLogger("org").setLevel(Level.ERROR)
  val sc = new SparkContext("local[*]", "MovieRatings")
  sc.textFile("/home/akshay/*/CS-BigData/00-Data/MovieData.data").
  map(x => (x.split("\t")(2), 1)).
  reduceByKey((x,y) => x+y).
  collect.
  foreach(println)
}