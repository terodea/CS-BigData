package transformations

import org.apache.log4j.Logger
import org.apache.log4j.Level
import org.apache.spark.SparkConf
import org.apache.spark.sql.SparkSession

object NewOrders extends App{
  /*
   * 
   */
  Logger.getLogger("org").setLevel(Level.ERROR)
  
  val myregex = """^(\S+) (\S+)\t(\S+)\,(\S+)""".r
  case class Orders(order_id:Int, customer_id:Int, order_status:String)
  def parser(line: String) ={
    line match{
      case myregex(order_id, data, customer_id, order_status) => Orders(order_id.toInt, customer_id.toInt, order_status)
    }
  }
  
  val spark_conf = new SparkConf()
  spark_conf.set("spark.app.name", "NewOrdersTransformation")
  spark_conf.set("spark.master", "local[2]")
  
  val spark = SparkSession.builder().config(spark_conf).getOrCreate()
  
  val lines = spark.sparkContext.textFile("/home/akshay/personal/CS-BigData/00-Data/OrdersNew.csv")
  
  import spark.implicits._
  
  val orderDS = lines.map(parser).toDS().cache()
  orderDS.printSchema()
  orderDS.select("order_id").show()
  orderDS.groupBy("order_status").count().show()
  spark.stop()
  
}
