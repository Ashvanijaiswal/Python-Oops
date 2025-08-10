from confluent_kafka import Producer
import json
import time

from delta import configure_spark_with_delta_pip
from pyspark.sql.window import Window
from pyspark.sql.functions import *

from pyspark.sql import SparkSession

class KafkaProducer():
    def __init__(self):
        self.topic = "invoices"
        # self.base_dir = "G:\Apache-Spark-and-Databricks-Stream-Processing-in-Lakehouse-main\KafkaProducer\data"
        self.conf = {
            "kafka.sasl.jaas.config": 'org.apache.kafka.common.security.plain.PlainLoginModule required username="OJ52GHVCYGEETXHI" password="iA0WT8bwzz8ghK3vHbml6yWtx7e/53YQQ9+hDCcatbH9MUc7LkWpQDeKWnY1QO/s";',
            "kafka.sasl.mechanism": "PLAIN",
            "kafka.security.protocol": "SASL_SSL",
            "kafka.bootstrap.servers": 'pkc-12576z.us-west2.gcp.confluent.cloud:9092',
            "subscribe": 'invoices',
        }

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

        return spark

    def getSchema(self):
        return """InvoiceNumber string, CreatedTime bigint, StoreID string, PosID string, CashierID string,
                 CustomerType string, CustomerCardNo string, TotalAmount double, NumberOfItems bigint, 
                 PaymentMethod string, TaxableAmount double, CGST double, SGST double, CESS double, 
                 DeliveryType string,
                 DeliveryAddress struct<AddressLine string, City string, ContactNumber string, PinCode string, 
                 State string>,
                 InvoiceLineItems array<struct<ItemCode string, ItemDescription string, 
                     ItemPrice double, ItemQty bigint, TotalValue double>>
             """
    def readInvoices(self, condition):
        from pyspark.sql.functions import expr
        spark=self.createSparkSession()
        return (spark.readStream.format("json").schema(self.getSchema()).
                 load("data/invoices.json"))

    def getKafkaMessage(selfself, df, key):
        return df.selectExpr(f"{key} as key","to_json(struct(*)) as value")

    def sendToKafka(self,kafka_df):
        return (kafka_df.writeStream.format("kafka")
                .option("kafka.bootstrap.servers", self.conf["kafka.bootstrap.servers"])
                .option("kafka.security.protocol", self.conf["kafka.security.protocol"])
                .option("kafka.sasl.mechanism", "PLAIN")
                .option("kafka.sasl.jaas.config",self.conf["kafka.sasl.jaas.config"])
                .option("topic", "invoices")
                .option("checkPointLocation", "data/")
                .start()
                )

    def process(self,condition):

        invoice_df=self.readInvoices("abc")
        kafka_df=self.getKafkaMessage(invoice_df,"StoreID")
        sQuery=self.sendToKafka(kafka_df)
        print("Done")
        return sQuery

if __name__=='__main__':
    ob=KafkaProducer()
    ob.process("abc")