__doc__ = """Statefull count of non-pair rdd's i.e sum of continuous streams"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import split
from pyspark.streaming import StreamingContext
from pyspark.streaming.DStream import reduceByWindow

spark = SparkSession \
    .builder \
    .appName("StructuredNetworkWordCount") \
    .getOrCreate()

lines = spark \
    .readStream \
    .format("socket") \
    .option("host", "localhost") \
    .option("port", 9999) \
    .load()

ssc = StreamingContext(spark, 10) #batch interval
# defining the checkpoint directory
ssc.checkpoint("/tmp")
# Split the lines into words
words = lines.reduceByWindow(
        func=lambda x,y: int(x)+int(y), 
        invFunc=lambda x,y: int(x)-int(y), 
        windowDuration=10, 
        slideDuration=2
    )

query = words \
    .writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

query.awaitTermination()


"""
nc -lk 9999
structured_network_wordcount.py localhost 9999
"""
