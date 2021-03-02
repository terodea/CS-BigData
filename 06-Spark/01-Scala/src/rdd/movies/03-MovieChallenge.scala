package rdd.movies

import org.apache.log4j.Logger
import org.apache.log4j.Level
import org.apache.spark.SparkContext

object MovieChallenge extends App{
  /*
   * Problem Statement:Find movies with average rating greater than 3.5 having at least 10 ratings. 
   */
  Logger.getLogger("org").setLevel(Level.ERROR)
  val sc = new SparkContext("local[*]", "MovieRatings")
  val movieRatings = sc.textFile("/home/akshay/*/CS-BigData/00-Data/MovieData.data").map(x => {
    val fields = x.split("\t")
    (fields(1), fields(2)) // [(101, 3),(101,4), (101,4.5)]
  }).mapValues(x => (x.toFloat, 1.0)). // [(101, (3,1)),(101,(4,1)), (101,(4.5,1))]
  reduceByKey((x,y) => (x._1 + y._1, x._2+ y._2)). // [(101, (11.5, 3.0))]
  filter(x => x._2._2 > 10).
  mapValues(x => x._1 / x._2). // [(101, (3.83))]
  filter(x => x._2 > 3.0)
  // movieRatings.collect.foreach(println)
  val movieName = sc.textFile("/home/akshay/*/CS-BigData/00-Data/Movies.dat").map(x => {
    val fields = x.split("::")
    (fields(0), fields(1))
  }) // [(101,Toy Story (1995)), (102,Toy Story (1996))]
  val movieWithRatings = movieName.join(movieRatings).map(x => x._2._1) //[(101, (Toy Story (1995), 3.83))]
  movieWithRatings.collect.foreach(println)
  scala.io.StdIn.readLine()
}