package customers

import org.apache.spark.SparkContext
import org.apache.log4j.Level
import org.apache.log4j.Logger

object TopTenShopoholicCustomers extends App{
  /* Problem Statement: Find out top 10 customers who spend the max.
   * 
   */
  Logger.getLogger("org").setLevel(Level.ERROR)
  val sc = new SparkContext("local[*]", "wordcountLower")
  sc.textFile("/home/akshay/*/CS-BigData/00-Data/CustomerOrders.csv").map(x => (x.split(","))).map(x => (x(0), x(2).toFloat)).reduceByKey((x,y) => x+y).sortBy(x => x._2).collect.foreach(println)
  
}