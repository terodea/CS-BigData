__doc__ = """Find top 10 customers who shopped the most."""
from re import A
from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext


def main():
    raw_data = sc.textFile("/path/to_the_file/file.csv")
    mapped_data = raw_data.map(lambda x: (x.split(",")[0], float(x.split(",")[2])))
    ans = mapped_data.reduceByKey(lambda x,y: x+y).sortBy(lambda x: x[1])
    print_ans = ans.collect
    print_ans.foreach(print)
if __name__ == "__main__":
    sc = SparkContext("local[*]", "TopCustomers")
    main()