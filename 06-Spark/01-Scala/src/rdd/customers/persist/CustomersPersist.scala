package rdd.customers.persist

import org.apache.log4j.Level
import org.apache.log4j.Logger
import org.apache.spark.SparkContext
import org.apache.spark.storage.StorageLevel

object CustomersPersist extends App{
  /*
   * Persist Data/ object in Spark
   * persist() supports three high level data caching categories:
   * 1. DISK: In Disk
   * 2. MEMEORY: In Memory
   * 3. OFF-HEAP: Outside JVM
   * 
   * At a low level following are the storage level
   * 1. DISK_ONLY: Caches only in Disk.
   * 2. DISK_ONLY_2: Caches two replicas of data.
   * 3. DISK_ONLY_SER: Serialized Version of data.
   * 4. MEMORY_ONLY
   * 5. MEMEORY_ONLY_2
   * 6. MEMORY_ONLY_SER
   * 7. MEMORY_AND_DISK: If memeory is full, evicted data is stored in disk.
   * 8. MEMEORY_AND_DISK_2:
   * 9. MEMEORY_AND_DISK_SER
   * 10. OFF_HEAP: Stored outside JVM Memory.
   */
  Logger.getLogger("org").setLevel(Level.ERROR)
  val sc = new SparkContext("local[*]", "CustomerPersist")
  val doubledAmount = sc.textFile("/home/akshay/*/CS-BigData/00-Data/CustomerOrders.csv").
  map(x => x.split(",")).
  map(x => (x(0), x(2).toFloat)).
  reduceByKey(_+_).
  filter(x => x._2 > 5000).
  map(x => (x._1, x._2*2)).persist(StorageLevel.MEMORY_AND_DISK)
  doubledAmount.foreach(println)
  print(doubledAmount.count)
  scala.io.StdIn.readLine()
}