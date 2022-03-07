from pyspark import SparkContext
from pyspark.streaming import StreamingContext
__doc__ = """Word count of continuously in-coming stream of data, i.e word count of all the rdd's in micro batches. i.e being statefull"""
# define the update function
def updateTotalCount(currentCount, countState):
    if countState is None:
       countState = 0
    return sum(currentCount, countState)

# create spark and streaming contexts
sc = SparkContext("local[*]", "StreamWordCounter")
ssc = StreamingContext(sc, 10) #batch interval

# defining the checkpoint directory
ssc.checkpoint("/tmp")

# read text from input socket
text = ssc.socketTextStream("localhost", 9999)

# count words
countStream = text.flatMap(lambda line: line.split(" "))\
                   .map(lambda word: (word, 1))\
                   .reduceByKey(lambda a, b: a + b)

# update total count for each key
wordCounts = countStream.updateStateByKey(updateTotalCount)

query = wordCounts \
    .writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

query.awaitTermination()

"""
nc -lk 9999
statefull_stream_wc.py localhost 9999
"""