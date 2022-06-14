"""
Neilson IQ Find avg, max time spend of charging per charging id and save to parquet.
"""
from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark.sql.functions import round

class ChargePointsETLJob:
    input_path = 'data/input/electric-chargepoints-2017.csv'
    output_path = 'data/output/chargepoints-2017-analysis'
    dt_ts_format = 'yyyy-MM-dd HH:mm:ss'

    def __init__(self):
        self.spark_session = (SparkSession.builder
                                          .master("local[*]")
                                          .appName("ElectricChargePointsETLJob")
                                          .getOrCreate())

    def extract(self):
        raw_df = self.spark_session.read.option("header", True).option("inferSchema", True).csv(self.input_path).withColumn(
            "startTs", F.unix_timestamp(F.concat(F.col("StartDate"), F.lit(" "), F.col("StartTime")), self.dt_ts_format)).withColumn(
                "endTs", F.unix_timestamp(F.concat(F.col("EndDate"), F.lit(" "), F.col("EndTime")), self.dt_ts_format))
        return raw_df

    def transform(self, df):
        """
        df.withColumn('test', F.concat_ws(" ", "StartDate", "StartTime")).withColumn("test", F.unix_timestamp(F.col("test"), "yyyy-MM-dd HH:mm:ss")).show()
        """
        time_spent = df.withColumn("time_spent", F.round((F.col("endTs") - F.col("startTs"))/3600,2))
        ans = time_spent.groupBy("CPID").agg(
            F.round(F.max(F.col("time_spent")),2).alias("max_duration"), 
            F.round(F.avg(F.col("time_spent")),2).alias("avg_duration")
        ).withColumnRenamed("CPID", "chargepoint_id")
        return ans
    def load(self, df):
        df.write.parquet(f"{self.output_path}")

    def run(self):
        self.load(self.transform(self.extract()))
