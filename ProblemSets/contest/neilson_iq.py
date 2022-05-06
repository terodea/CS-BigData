"""
Neilson IQ avg, max, test and save to parquet.
"""
from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark.sql.functions import round

class ChargePointsETLJob:
    input_path = 'data/input/electric-chargepoints-2017.csv'
    output_path = 'data/output/chargepoints-2017-analysis'

    def __init__(self):
        self.spark_session = (SparkSession.builder
                                          .master("local[*]")
                                          .appName("ElectricChargePointsETLJob")
                                          .getOrCreate())

    def extract(self):
        raw_df = self.spark_session.read.option("header", True).option("inferSchema", True).csv(self.input_path).withColumn("StartTimeTs", F.to_timestamp("StartTime"))
        end_raw_df = raw_df.withColumn("EndTimeTs", F.to_timestamp("EndTime"))
        return end_raw_df

    def transform(self, df):
        max_duration_df = df.withColumn("max_duration", (F.col("StartTimeTs").cast("long") - F.col("EndTimeTs").cast("long"))/3600)
        avg_duration_df = max_duration_df.groupBy("CPID").agg(
            round(max("max_duration"),2).alias("max_duration"), 
            round(F.avg("max_duration"),2).alias("avg_duration")
            ).withColumnRenamed("CPID", "chargepoint_id")
        return avg_duration_df.select("avg_duration", "chargepoint_id", "max_duration").compute()
    def load(self, df):
        df.write.parquet(f"{self.output_path}")

    def run(self):
        self.load(self.transform(self.extract()))
