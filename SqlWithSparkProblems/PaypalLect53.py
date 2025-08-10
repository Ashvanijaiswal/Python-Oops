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

data=[ (1, 'Ankit', 100,10000),
 (2, 'Mohit', 100, 15000),
 (3, 'Vikas', 100, 10000),
 (4, 'Rohit', 100, 5000),
 (5, 'Mudit', 200, 12000),
 (6, 'Agam', 200, 12000),
 (7, 'Sanjay', 200, 9000),
 (8, 'Ashish', 200,5000),
 (9, 'Mukesh',300,6000),
 (10, 'Rakesh',300,7000)]

schema=StructType([StructField("emp_id", IntegerType(), False),
                   StructField("name",StringType(),False),
                   StructField("dept_id",IntegerType(),False),
                   StructField("salary",IntegerType(),False),
                   ])
df=spark.createDataFrame(data,schema)
df.withColumn("total", sum("salary").over(Window.orderBy("emp_id").\
                                          rowsBetween(Window.unboundedPreceding,Window.unboundedFollowing))).\
    withColumn("dept_sum", sum("salary").\
               over(Window.partitionBy("dept_id").orderBy("dept_id"))).\
    withColumn("dept_cnt",count("emp_id").over(Window.partitionBy("dept_id").orderBy("dept_id"))).\
    withColumn("total-dept", col("total")-col("dept_sum")).\
    withColumn("dept_avg",col("dept_sum")/col("dept_cnt")).\
    withColumn("total_cnt", count("emp_id").over(Window.orderBy(lit(1)))).\
    withColumn("company_avg",(col("total")-col("dept_sum"))/(col("total_cnt")-col("dept_cnt"))).\
    where("dept_avg<company_avg").show()

spark.stop()


