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

data=[(1,	"Alice",	6000,	"HR"),
      (2,	"Bob"	   , 7000,	"HR"),
      (3,	"Charlie",8000	,"IT"),
      (4,	"David",	7500,	"IT"  ),
      (5,	"Eve"	   , 6000	,"IT"),
      (6,	"Frank",	9000	,"Sales"),
      (7,	"Grace",	8500	,"Sales")]

schema=StructType([StructField("id", IntegerType(), False),
                   StructField("Name",StringType(),False),
                   StructField("Salary",IntegerType(),False),
                   StructField("dept",StringType(),False)])

df=spark.createDataFrame(data,schema)

dept_wise_max_sal=df.groupby("dept").agg(max("Salary").alias("max_sal"))

dept_wise_max_sal.alias("l").join(df.alias("r"),dept_wise_max_sal.dept==df.dept,"inner").where(expr("Salary<max_sal")).groupby("r.dept").\
    agg(max("r.Salary").alias("second_sal")).show()

spark.stop()