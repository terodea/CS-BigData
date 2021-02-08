package wordcount

import org.apache.spark.SparkContext
import org.apache.log4j.Logger
import org.apache.log4j.Level

object WordCount extends App{
  Logger.getLogger("org").setLevel(Level.ERROR)
  val sc = new SparkContext("local[*]","wordcount")
  val input = sc.textFile("/home/akshay/Desktop/client.py")
  val words = input.flatMap(x => x.split(" "))
  val wordMap = words.map(x=> (x,1))
  val finalCount = wordMap.reduceByKey((a,b) => a+b)
  finalCount.collect.foreach(println)
}