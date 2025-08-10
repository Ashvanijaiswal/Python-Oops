from pyspark.sql.functions import *
from pyspark.sql.types import  *
from pyspark.sql import SparkSession
from delta import configure_spark_with_delta_pip


class Bronze():

    def __init__(self):
        self.base_data_dir="/Users/ashvanijaiswal/PycharmProjects/PythonProject/IntuitUPIDataLake/data/"

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
        schema="""InvoiceNumber string, CreatedTime bigint, StoreID string, PosID string, CashierID string,CustomerType string,
        CustomerCardNo string, TotalAmount double, NumberOfItems int, PaymentMethod string, TaxableAmount double,CGST double,
        SGST double, CESS double, DeliveryType string, 
        DeliveryAddress struct<
        AddressLine string, City string, State string, PinCode int, ContactNumber bigint>,
        InvoiceLineItems array<struct<
        ItemCode string,
        ItemDescription string,
        ItemPrice double,
        ItemQty bigint,
        TotalValue double>>"""
        return schema

    def ingest_raw_data(self,spark):


        raw_data= spark.readStream\
            .format("json").schema(self.getSchema())\
            .option("cleanSource", "archive")\
            .option("sourceArchiveDir", f"{self.base_data_dir}/invoice_archive")\
            .load(f"{self.base_data_dir}/invoices.json")
        return raw_data

    def process(self,spark):
        print("Starting bronze pipeline")
        invoiceDF = self.ingest_raw_data(spark)
        streamQuery = (invoiceDF.writeStream. \
                       format("delta").\
                       queryName("bronze_ingestion").\
                       option("checkpointLocation", f"{self.base_data_dir}/checkpoint/invoice_bz").\
                       outputMode("append").\
                       toTable("invoice_bz"))
        print("Done")
        return streamQuery



class Silver():

    def __init__(self):
        self.base_data_dir="/Users/ashvanijaiswal/PycharmProjects/PythonProject/IntuitUPIDataLake/data/"

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

    def readInvoices(self,spark):
        return (
            spark.readStream.table("invoice_bz")
        )

    def explodeInvoiceData(self, raw_data):
        return raw_data.selectExpr("InvoiceNumber", "CreatedTime", "StoreID", "PosID",
                                      "CustomerType", "PaymentMethod", "DeliveryType", "DeliveryAddress.City",
                                      "DeliveryAddress.State","DeliveryAddress.PinCode",
                                      "explode(InvoiceLineItems) as LineItem")

    def flattenInvoice(self,explodedDF):
        return (
                explodedDF.withColumn("ItemCode", expr("LineItem.ItemCode")). \
                withColumn("ItemCode", expr("LineItem.ItemCode")).\
                withColumn("ItemDescription", expr("LineItem.ItemDescription")). \
                withColumn("ItemPrice", expr("LineItem.ItemPrice")). \
                withColumn("ItemQty", expr("LineItem.ItemQty")).\
                withColumn("TotalValue", expr("LineItem.TotalValue")).drop("LineItem")
                )

    def appendIntoDataLake(self,spark, flattenDF):
       return  (flattenDF.writeStream.format("csv").outputMode("append")\
         .queryName("silver_ingestion")\
         .option("checkpointLocation", f"{self.base_data_dir}/checkpoint/invoices") \
         .toTable("invoices"))

    def process(self,spark):
        print("Starting silver pipeline")
        silverDF = self.readInvoices(spark)
        streamQuery = self.appendIntoDataLake(spark, silverDF)
        print("Done")
        return streamQuery


if __name__=="__main__":
    try:
        bronze = Bronze()
        spark = bronze.createSparkSession()
        bronzeSquery = bronze.process(spark)
        bronzeSquery.awaitTermination(timeout=100)
        silver= Silver()
        silverSquery= silver.process(spark)
        silverSquery.awaitTermination(timeout=100)



        spark.sql("SHOW Tables").show()

    finally:
        spark.stop()









