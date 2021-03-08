import pandas as pd
from pandas.tseries.offsets import YearBegin
from pyspark import conf, sql
from pyspark.context import SparkContext
from pyspark.sql.functions import col, pandas_udf, struct, PandasUDFType
from pyspark.sql.types import StructType, StructField, IntegerType, FloatType, StringType
from pyspark.sql import SparkSession
from pyspark import SparkConf, SQLContext
from pyspark.sql.functions import udf


def plus_one(batch_iter):
    return batch_iter + 1

def multiply_two_cols(batch_iter):
    return batch_iter * batch_iter

if __name__ == '__main__':
    spark_conf  = SparkConf()
    spark_conf.set("spark.app.name", "UDF Example")
    spark_conf.set("spark.master", "local[2]")
    sc = SparkContext.getOrCreate(conf=spark_conf)
    spark = SQLContext(sc)


    colsInt = udf(lambda z: plus_one(z), IntegerType())
    spark.udf.register("colsInt", colsInt)
    colsDoubel = udf(lambda x: multiply_two_cols(x), IntegerType())
    spark.udf.register("colsDoubel", colsDoubel)

    x = pd.Series([1,2,3])
    pdf = pd.DataFrame([1,2,3], columns=["x"])
    df  = spark.createDataFrame(pdf)
    _df = df.select(colsInt("x"))
    _df.show()
    df.select(colsDoubel("x")).show()