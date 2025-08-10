from delta import configure_spark_with_delta_pip
from pyspark.sql.types import StructField, LongType, DoubleType, IntegerType
from pyspark.sql.window import Window
from pyspark.sql.functions import *

from pyspark.sql import SparkSession

class StreamingAggregate:
    def __init__(self):
        self.topic = "invoices"
        self.base_dir = "/Users/ashvanijaiswal/PycharmProjects/PythonProject/IntuitUPIDataLake/data"
        self.conf = {
            "kafka.sasl.jaas.config": 'org.apache.kafka.common.security.plain.PlainLoginModule required username="OJ52GHVCYGEETXHI" password="iA0WT8bwzz8ghK3vHbml6yWtx7e/53YQQ9+hDCcatbH9MUc7LkWpQDeKWnY1QO/s";',
            "kafka.sasl.mechanism": "PLAIN",
            "kafka.security.protocol" : "SASL_SSL",
            "kafka.bootstrap.servers": 'pkc-12576z.us-west2.gcp.confluent.cloud:9092',
            "subscribe": 'invoices',
            }

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


    def getSchema(self):
        try:

            schema = StructType([
                StructField("InvoiceNumber", StringType(), True),
                StructField("CreatedTime", LongType(), True),
                StructField("StoreID", StringType(), True),
                StructField("PosID", StringType(), True),
                StructField("CashierID", StringType(), True),
                StructField("CustomerType", StringType(), True),
                StructField("CustomerCardNo", StringType(), True),
                StructField("TotalAmount", DoubleType(), True),
                StructField("NumberOfItems", IntegerType(), True),
                StructField("PaymentMethod", StringType(), True),
                StructField("TaxableAmount", DoubleType(), True),
                StructField("CGST", DoubleType(), True),
                StructField("SGST", DoubleType(), True),
                StructField("CESS", DoubleType(), True),
                StructField("DeliveryType", StringType(), True),
                StructField("DeliveryAddress", StructType([
                    StructField("AddressLine", StringType(), True),
                    StructField("City", StringType(), True),
                    StructField("State", StringType(), True),
                    StructField("PinCode", IntegerType(), True),
                    StructField("ContactNumber", LongType(), True)
                ]), True),
                StructField("InvoiceLineItems", ArrayType(
                    StructType([
                        StructField("ItemCode", StringType(), True),
                        StructField("ItemDescription", StringType(), True),
                        StructField("ItemPrice", DoubleType(), True),
                        StructField("ItemQty", LongType(), True),
                        StructField("TotalValue", DoubleType(), True)
                    ])
                ), True)
            ])
            return schema
        except Exception as e:
            print(f"Error while creating schema: {e}")
            raise

    def readDataFromKafka(self, spark, startingTimestamp = 1):
        try:
            df = spark \
                .readStream \
                .format("kafka") \
                .option("kafka.bootstrap.servers", "pkc-12576z.us-west2.gcp.confluent.cloud:9092")\
                .option("kafka.security.protocol","SASL_SSL" )\
                .option("kafka.sasl.mechanism", "PLAIN")\
                .option("kafka.sasl.jaas.config","org.apache.kafka.common.security.plain.PlainLoginModule required username='OJ52GHVCYGEETXHI' password='iA0WT8bwzz8ghK3vHbml6yWtx7e/53YQQ9+hDCcatbH9MUc7LkWpQDeKWnY1QO/s';")\
                .option("topic", "invoices")\
                .option("maxoffsetsPerTrigger", 10) \
                .option("startingTimestamp" , startingTimestamp)\
                .load()
            return df
        except Exception as e:
            print(f"Error while reading data from Kafka: {e}")
            raise

    def getInvoices(self, kafka_df):
        try:

            return  (kafka_df.select(kafka_df.key.cast("string").alias("key"),
                                     from_json(kafka_df.value.cast("string").alias("value"), self.getSchema()),
                                 "topic", "timestamp"))
        except Exception as e:
            print(f"Error while parsing invoices: {e}")
            raise


def process(self, spark, startingTime = 1):
    try:

        print("starting bronze ingestion ...")
        kafka_df = self.readDataFromKafka(spark, startingTime)
        invoices_df = self.getInvoices(kafka_df)
        sQuery = (invoices_df.writeStream.format("delta") \
                  .queryName("invoices bronze")
                  .option("checkpointLocation",self.base_dir/"invoice_bz" )\
                  .outputMode("append")\
                  .toTable("invoices_bz"))
        return sQuery
    except Exception as e:
        print(f"Error during bronze ingestion process: {e}")
        raise

class GoldAggregate():

    def __init__(self):
        self.base_dir="/Users/ashvanijaiswal/PycharmProjects/PythonProject/IntuitUPIDataLake/data"

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

    def readInvoiceDataFromTable(self,spark):
        try:
            return spark.readStream.table("invoices_bz")
        except Exception as e:
            print(f"Error while reading data from table: {e}")
            raise

    def getAggregates(self, invoice_df):
        try:
            return invoice_df.groupBy("CustomerCardNo").agg(
                sum("TotalAmount").alias("TotalAmount"),
                sum(expr("TotalAmount * 0.02")).alias("rewards")
            )
        except Exception as e:
            print(f"Error while calculating aggregates: {e}")
            raise

    # complete mode is used state store to get aggregated results but problem is if large data came then state store size
    # would be more and that cause performance issue.
    # complete mode - complete data will be loaded into table
    # def saveResult(self, customer_df):
    #     streamQuery = customer_df.writeStream.format("delta").\
    #         queryName("gold-ingestion").\
    #         option("checkpointLocation", self.base_dir/"customers").\
    #         outputMode("complete").\
    #         toTable("customers")
    #
    #     return streamQuery

    def upsert(self, customer_df, batch_id):
        try:
            customer_df.createOrReplaceTempView("customer_rewards")
            merge_stmt = """
                        MERGE INTO CUSTOMERS c
                        USING customer_rewards cr
                        ON c.CustomerCardNo = cr.CustomerCardNo
                        WHEN MATCHED THEN
                        UPDATE SET c.totalAmount = cr.totalAmount, c.totalPoint = cr.totalPoint,c.last_used=cr.last_used
                        WHEN NOT MATCHED THEN
                        INSERT *
                    """
            customer_df._jdf.sparkSession().sql(merge_stmt)
        except Exception as e:
            print(f"Error during upsert: {e}")
            raise

    #   when we don't want statstore to store aggregation
    # def upsertStatelessAggr(self, customer_df, batch_id):
    #     aggregated_df = self.getAggregates(customer_df)
    #     aggregated_df.createOrReplaceTempView("customer_rewards")
    #     merge_stmt = """
    #                 MERGE INTO CUSTOMERS c
    #                 USING customer_rewards cr
    #                 on c.CustomerCardNo= cr.CustomerCardNo
    #                 WHEN MATCHED THEN
    #                 UPDATE SET c.totalAmount=cr.totalAmount+c.totalAmount, c.totalPoint=cr.totalPoint+c.totalPoint
    #                 WHEN NOT MATCHED THEN
    #                 INSERT *
    #                 """
    #     customer_df._jdf.sparkSession().sql(merge_stmt)


    # update mode - only modified and newly added records will be loaded into table
    def saveResult(self, customer_df):
        try:
            streamQuery = customer_df.writeStream.format("delta") \
                .queryName("gold-ingestion") \
                .option("checkpointLocation", f"{self.base_dir}/customers") \
                .outputMode("update") \
                .foreachBatch(self.upsert) \
                .start()
            return streamQuery
        except Exception as e:
            print(f"Error while saving results: {e}")
            raise

    def process(self, spark, startingTimestamp = 1):
        try:
            print("Starting Gold ingestion ...")
            invoice_df = self.readInvoiceDataFromTable(spark)
            aggregated_df = self.getAggregates(invoice_df)
            sQuery = self.saveResult(aggregated_df)
            return sQuery
        except Exception as e:
            print(f"Error during Gold ingestion process: {e}")
            raise



if __name__ == "__main__":
    try:
        invoice_consumer  = StreamingAggregate()
        spark = invoice_consumer.createSparkSession()
        bz_sQuery=invoice_consumer.process(spark)
        customer_rewards= GoldAggregate()
        gold_sQuery = customer_rewards.process(spark)
        bz_sQuery.stop()
        gold_sQuery.stop()
    finally:
        spark.stop()



