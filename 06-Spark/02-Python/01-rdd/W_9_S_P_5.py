import imp
from pyspark import SparkContext



def main():
    raw_data = sc.textFile("/path_to_file.csv")
    mapped_data = raw_data.map(lambda x: x.split("\t")[2])
    return mapped_data.countByValue() # replacement for map().reduceByKey()

if __name__ == "__main__":
    sc = SparkContext("local[*]", "CountRatings")
    main()