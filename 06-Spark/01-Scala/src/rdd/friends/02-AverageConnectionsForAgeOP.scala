package rdd.friends

import org.apache.log4j.Level
import org.apache.log4j.Logger
import org.apache.spark.SparkContext

object AverageConnectionsForAgeOP extends App{
  /*
   * Column Name: row_id, name, age, number_of_connections
   * Problem Statement: Find average number of connections for each age, 
   * 										split using named functions , 
   * 										use mapValues instead of map only exception is while reading the CSV 
   * 										and arrange in ascending manner.
   */
  def parseLines(line: String) = {
    val fields = line.split("::")
    val age = fields(2).toInt
    val numFriends = fields(3).toInt
    (age, numFriends)
  }
  Logger.getLogger("org").setLevel(Level.ERROR)
  val sc = new SparkContext("local[*]", "AverageConnectionsForAgesOptimized")
  sc.textFile("/home/akshay/*/CS-BigData/00-Data/FriendsData.csv").
  map(parseLines).mapValues(x => (x,1)).
  reduceByKey((x,y) => (x._1 + y._1, x._2 + y._2)).
  mapValues(x => (x._1 / x._2)).
  sortBy(x => x._2).
  collect.
  foreach(println)
}