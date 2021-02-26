package customers.cache

import org.apache.log4j.Level
import org.apache.log4j.Logger
import org.apache.spark.SparkContext

object CustomerCached extends App{
  /*
   * Caching Object/ data in Apache Spark.
   * open localhost:4040, you should see
   * two jobs 
   * 1. foreach println job
   * 2. count job (gets cached data)
   * 
   */
  Logger.getLogger("org").setLevel(Level.ERROR)
  val sc = new SparkContext("local[*]", "customersCached")
  val doubledAmount = sc.textFile("/home/akshay/*/CS-BigData/00-Data/CustomerOrders.csv").
  map(x => x.split(",")).
  map(x => (x(0), x(2).toFloat)).
  reduceByKey(_+_).
  filter(x => x._2 > 5000).map(x => (x._1, x._2*2)).cache()
  
  doubledAmount.foreach(println)
  println(doubledAmount.count)
  scala.io.StdIn.readLine()
}