from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql import Window, SparkSession

spark = SparkSession.builder \
    .appName("MyApp") \
    .master("local[*]") \
    .config("spark.driver.port", "4040") \
    .config("spark.driver.bindAddress", "127.0.0.1") \
    .config("spark.driver.host", "127.0.0.1") \
    .config("spark.blockManager.port", "6060")\
    .getOrCreate()

data=[ ('IND', 'SL','IND'),
       ('SL','AUS','AUS'),
       ('SA','ENG','ENG'),
       ('ENG','NZ','NZ'),
       ('AUS',"IND",'IND')]


schema=StructType([StructField("team1", StringType(), False),
                   StructField("team2",StringType(),False),
                   StructField("winner",StringType(),False)])
df=spark.createDataFrame(data,schema)
df2=df.union(df.select("team2","team1","winner"))

df3= df2.withColumn("is_win", when(col("team1")==col("winner"),1).otherwise(0))
(df3.groupby("team1").agg(sum("is_win").alias("no_of_wins"),
                         count("team1").alias("total_matches"),
                         (count("team1")-sum("is_win")).alias("no_of_lost")).show())
spark.stop()
