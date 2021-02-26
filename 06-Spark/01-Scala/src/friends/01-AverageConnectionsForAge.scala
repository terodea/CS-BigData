package friends

import org.apache.log4j.Level
import org.apache.log4j.Logger
import org.apache.spark.SparkContext

object AverageConnectionsForAge extends App{
  /*
   * Column Name: row_id, name, age, number_of_connections
   * Problem Statement: Find average number of connections for each age in ascending manner.
   */
  Logger.getLogger("org").setLevel(Level.ERROR)
  val sc = new SparkContext("local[*]", "AverageConnectionsForAges")
  sc.textFile("/home/akshay/*/CS-BigData/00-Data/FriendsData.csv").
  map(x => x.split("::")).map(x => (x(2).toInt,(x(3).toInt,1))).
  reduceByKey((x,y) => (x._1 + y._1, x._2 + y._2)).
  map(x => (x._1, x._2._1 / x._2._2)).
  sortBy(x => x._1).
  collect.
  foreach(println)
}