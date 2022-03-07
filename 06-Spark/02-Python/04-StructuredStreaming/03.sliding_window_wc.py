from pyspark.sql import SparkSession
from pyspark.sql.functions import split
from pyspark.streaming import StreamingContext
from pyspark.streaming.DStream import reduceByKeyAndWindow

__doc__ = """Find the frequency of each word in the 10 seconds sliding window"""
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
words = lines.flatMap(lambda x: x.split(" ")).map(lambda x: (x, 1)).reduceByKeyAndWindow(
    func=lambda x,y: x+y, invFunc=lambda x,y: x-y, windowDuration=10, slideDuration=2, filterFunc=lambda x: x[1] > 0)

# Generate running word count
wordCounts = words.reduceByKey(lambda x,y: x+y)

query = wordCounts \
    .writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

query.awaitTermination()


"""
nc -lk 9999
structured_network_wordcount.py localhost 9999
"""
