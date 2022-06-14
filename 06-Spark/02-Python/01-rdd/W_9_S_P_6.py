import imp
from pyspark import SparkContext

def main():
    raw_data = sc.textFile("/path_to_the_file.csv")
    mapped_data = raw_data.map(lambda x: (x.split(",")[2],(int(x.split(",")[3]),1))) # (33, (600, 1))
    # map(lambda x: (x[0], x[1][0]/x[1][1])) -> mapValues(lambda x: x[0]/x[1])
    return mapped_data.reduceByKey(lambda x,y: (x[0] + y[0], x[1]+y[1])).map(lambda x: (x[0], x[1][0]/x[1][1])).collect()

if __name__ == "__main__":
    sc = SparkContext("local[*]", "AvgConnectionPerAge")
    main()