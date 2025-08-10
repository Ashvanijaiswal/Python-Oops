from delta import configure_spark_with_delta_pip
from pyspark.sql.functions import *
from pyspark.sql.types import  *
from pyspark.sql import SparkSession


class Utility():

    def createSparkSession(self):
        builder = SparkSession.builder \
            .appName("MyApp") \
            .master("local[*]") \
            .config("spark.driver.port", "4040") \
            .config("spark.driver.bindAddress", "127.0.0.1") \
            .config("spark.driver.host", "127.0.0.1") \
            .config("spark.blockManager.port", "6060") \
            .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
            .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
            .config("spark.jars.packages", "io.delta:delta-core_2.12:2.3.0")

        spark = configure_spark_with_delta_pip(builder).getOrCreate()

    def read_table(self):
        spark=self.createSparkSession()
        spark.sql("select * from invoices").show()



