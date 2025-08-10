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

data=[  (20,20),
        (20,20),
        (20,21),
        (23,22),
        (22,23),
        (21,20)
       ]

schema=StructType([StructField('X',IntegerType(),False),
                   StructField("Y", IntegerType(),False)])

df=spark.createDataFrame(data,schema)
df2=df.withColumn("row_nm",row_number().over(Window.orderBy("X")))
df2.alias("l").join(df2.alias("r"),(col("l.X")==col("r.Y") )& (col("r.X")==col("l.Y")),"inner").\
    where("l.X<=r.X").select("l.X","r.Y").distinct().show()

spark.stop()