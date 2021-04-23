import os
from pyspark import SparkConf, SparkContext, rdd

def main():
    """
    FASTER
    Task: Assign LogLevel to WARN & ERROR
    """
    try:
        bcast = sc.broadcast(
            {
                "WARN": 1, 
                "ERROR": 0
            }
        )

        # Following is a test file. Recommended to use file greater than 1 GB to see performance improvement.
        bigLog = sc.textFile(f"{os.environ.get('DATA_PATH')}/bigLogTest.txt") 
        return bigLog.map(lambda x: x.split(": ")).map(lambda y: (y[0], y[1])).map(lambda z: (z[0], z[1], bcast.value.get(z[0]))).collect()
    except Exception as e:
        raise e

def slow_main():
    """
    SLOWER: Because join involves shuffling. Shuffling is a heavy Network task.
    Task: Assign LogLevel to WARN & ERROR
    """
    try:
        # Following is a test file. Recommended to use file greater than 1 GB to see performance improvement.
        bigLog = sc.textFile(f"{os.environ.get('DATA_PATH')}/bigLogTest.txt") 
        rdd1 = bigLog.map(lambda x: x.split(": ")).map(lambda y: (y[0], y[1])).map(lambda z: (z[0], z[1]))
        rdd2 = sc.parallelize(
            [
                ("WARN", 1),
                ("ERROR", 0)
            ]
        )
        return rdd1.join(rdd2).collect()
    except Exception as e:
        raise e
if __name__ == '__main__':
    sc = SparkContext('local', 'RDDBroadCastJoinExample')
    print(main())

