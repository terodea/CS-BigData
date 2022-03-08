from pyspark.sql import SparkSession

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

# Split the lines into words
words = lines.flatMap(lambda x: x.split(" ")).map(lambda x: (x, 1))

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
