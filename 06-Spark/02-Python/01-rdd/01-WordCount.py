import sys
from pyspark import SparkContext, SparkConf

if __name__ == '__main__':
    sc = SparkContext('local', "PySpark Word Count Example")
    wordCounts = sc.textFile("/home/akshay/Desktop/client.py"). \
        flatMap(lambda line: line.split(" ")). \
        map(lambda word: (word, 1)). \
        reduceByKey(lambda a, b: a + b)
    wordCounts.saveAsTextFile("/home/akshay/Desktop/out_put")
