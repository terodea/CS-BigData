package transformations

import org.apache.log4j.Level
import org.apache.log4j.Logger
import org.apache.spark.SparkConf
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions.col
import org.apache.spark.sql.functions.monotonically_increasing_id
import org.apache.spark.sql.functions.unix_timestamp
import org.apache.spark.sql.types.DateType

object ListToDataFrame extends App{
  /* Given a scala list convert it to spark dataframe.
   * List((1,"2013-07-25", 11599, "CLOSED"), (2,"2013-07-25", 256, "PENDING_PAYMENT"), (3,"2013-07-25", 11560, "COMPLETE"),(4,"2013-07-25", 8827, "CLOSED"))
   * Perform below mentioned tasks on the dataframe:
   * 1. Convert OrderDate to epoch timestamp (unitimestamp)
   * 2. Create a column with name newid having unique id's.
   * 3. Drop Duplicates: orderdate, customerid
   * 4. Drop Column orderid.
   * 5. Sort on the basis of orderdate.
   */
  Logger.getLogger("org").setLevel(Level.ERROR)
  
  // Setting up initial configurations
  
  val spark_conf = new SparkConf().set("spark.app.name", "ListToDataFrameWithSomeTransformations").set("spark.master", "local[2]")
  val spark = SparkSession.builder().config(spark_conf).getOrCreate()
  
  // Main transformation logic
  val myList = List(
        (1,"2013-07-25", 11599, "CLOSED"), 
        (2,"2013-07-25", 256, "PENDING_PAYMENT"), 
        (3,"2013-07-25", 11560, "COMPLETE"), 
        (4,"2013-07-25", 8827, "CLOSED")
      )
  
  val ordersDf = spark.createDataFrame(myList).toDF("orderid", "orderdate", "customerid", "status")
  
  val newDf = ordersDf.
  withColumn("orderdate", unix_timestamp(col("orderdate").cast(DateType))).
  withColumn("newid", monotonically_increasing_id).
  dropDuplicates("orderdate", "customerid").
  drop("orderid").
  sort("orderdate")
  
  newDf.printSchema()
  newDf.show()
  
  // Stop the spark application.
  spark.stop()
}