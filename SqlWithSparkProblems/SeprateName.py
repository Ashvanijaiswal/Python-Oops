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

data=[ ('Ashvani Jaiswal',)
      ,('Vishal Pratap Singh',)
      ,('Michael',)]

schema=StructType([StructField("name", StringType(), False)])
df=spark.createDataFrame(data,schema)
df.show()
df.withColumn("first", split(col("name")," ")[0]).\
    withColumn("sec", split(col("name")," ")[1]).\
    withColumn("lst", split(col("name")," ")[2]).show()
spark.stop()