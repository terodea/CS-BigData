import os
from pyspark import SparkConf
from pyspark.sql import SparkSession

def main():
    """
    Week12Session24: PivotTable
        +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+ 
        |level|    1|    2|    3|    4|    5|    6|    7|    8|    9|   10|   11|   12|
        +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
        | INFO|29119|28983|29095|29302|28900|29143|29300|28993|29038|29018|23301|28874|
        |ERROR| 4054| 4013| 4122| 4107| 4086| 4059| 3976| 3987| 4161| 4040| 3389| 4106|
        | WARN| 8217| 8266| 8165| 8277| 8403| 8191| 8222| 8381| 8352| 8226| 6616| 8328|
        |FATAL|   94|   72|   70|   83|   60|   78|   98|   80|   81|   92|16797|   94|
        |DEBUG|41961|41734|41652|41869|41785|41774|42085|42147|41433|41936|33366|41749|
        +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
    
    Optimisation:
        +-----+-------+--------+-----+-----+-----+-----+-----+------+---------+-------+--------+--------+
        |level|January|February|March|April|  May| June| July|August|September|October|November|December|
        +-----+-------+--------+-----+-----+-----+-----+-----+------+---------+-------+--------+--------+
        | INFO|  29119|   28983|29095|29302|28900|29143|29300| 28993|    29038|  29018|   23301|   28874|
        |ERROR|   4054|    4013| 4122| 4107| 4086| 4059| 3976|  3987|     4161|   4040|    3389|    4106|
        | WARN|   8217|    8266| 8165| 8277| 8403| 8191| 8222|  8381|     8352|   8226|    6616|    8328|
        |FATAL|     94|      72|   70|   83|   60|   78|   98|    80|       81|     92|   16797|      94|
        |DEBUG|  41961|   41734|41652|41869|41785|41774|42085| 42147|    41433|  41936|   33366|   41749|
        +-----+-------+--------+-----+-----+-----+-----+-----+------+---------+-------+--------+--------+
    """
    try:
        bigLog = spark.read.format("csv").option("header", True).option("path", f"{os.environ.get('DATA_PATH')}/bigLog.txt").load()

        bigLog.createOrReplaceTempView("bigLogTable")

        spark.sql(
            f"""SELECT level, date_format(datetime, 'MMMM') as month, cast(date_format(datetime, 'M') as int) as monthnum FROM bigLogTable"""
        ).groupBy("level").pivot("monthnum").count().show()

        # Optimisation: Display MonthNum as MonthNames
        month_list = [
            "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
        ]
        spark.sql(
            f"""SELECT level, date_format(datetime, 'MMMM') as month FROM bigLogTable"""
        ).groupBy("level").pivot("month", month_list).count().show()

    except Exception as e:
        raise e


if __name__ == '__main__':
    spark_conf = SparkConf()
    spark_conf.set("spark.app.name", "Week12Session24")
    spark_conf.set("spark.main", "local[2]")
    spark = SparkSession.builder.config(conf=spark_conf).getOrCreate()
    main()
    spark.stop()