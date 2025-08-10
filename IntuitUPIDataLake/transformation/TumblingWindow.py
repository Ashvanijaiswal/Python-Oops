from delta import configure_spark_with_delta_pip
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql import SparkSession

class tumbling_window():
    def __int__(self):
        self.base_dir = "/Users/ashvanijaiswal/PycharmProjects/PythonProject/IntuitUPIDataLake/data"

    def createSparkSession(self):
        try:
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

            return spark
        except Exception as e:
            print(f"Error while creating Spark session: {e}")
            raise
    def get_schema(self):
        schema=StructType([StructField("CreatedTime",StringType(),False),
                           StructField("Type",StringType(),False),
                           StructField("Amount",DoubleType(),False),
                           StructField("BrokerCode", StringType(),False)])
        return schema


    def readBronze(self):
        spark = self.createSparkSession()
        return spark.readStream().table("kafka_bz")

    def get_trade(self, kafka_df):
        return (
            kafka_df.select(from_json("value",schema=self.get_schema()).alis("value")).select("value.*")\
            .withColumn("createTime", expr("to_timestamp(CreatedTime, 'yyyy-MM-dd HH:mm:ss')"))\
            .withColumn("Buy", expr("When Type=='BUY' then Amount else 0 end "))\
            .withColumn("Sell", expr("When Type=='SELL' then Amount else 0 end" ))
        )

    def getAggregate(self,trade_df):
        return (
            trade_df.groupBy(window(trade_df.createTime, '15 minutes'))\
            .agg(sum("BUY").alias("totalBuy"))\
            .agg(sum("SELL").alis("totalSell"))\
            .select("window.start","window.end", "TotalBuy", "TotalSell")
        )

    def saveAsTable(self, result_df):
        return (
            result_df.writeStream().queryName("trade-summary")\
            .option("checkpointLocation", f"{self.base_dir}/checkpoint/trade_summary")\
            .outputMode("complete")\
            .toTable("trade_summary")
        )

    def process(self):
        kafka_df=self.readBronze()
        trade_df=self.get_trade(kafka_df)
        result_df=self.getAggregate(trade_df)
        sQuery= self.saveAsTable(result_df)
        return sQuery



