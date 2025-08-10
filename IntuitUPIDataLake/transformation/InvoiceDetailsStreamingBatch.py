from pyspark.sql.functions import *
from pyspark.sql.types import  *
from pyspark.sql import SparkSession
from delta import configure_spark_with_delta_pip


class InvoiceStreamAndBatch():

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
        from pyspark.sql.types import (
            StructType, StructField, StringType, LongType, IntegerType, DoubleType, ArrayType
        )

        # Define the schema
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

    def ingest_raw_data(self,spark):
        raw_data= spark.readStream.format("json").schema(self.getSchema()).load(f"{self.base_data_dir}/invoices.json")
        return raw_data

    def explodeInvoiceData(self, raw_data):
        return raw_data.selectExpr("InvoiceNumber", "CreatedTime", "StoreID", "PosID",
                                      "CustomerType", "PaymentMethod", "DeliveryType", "DeliveryAddress.City",
                                      "DeliveryAddress.State","DeliveryAddress.PinCode",
                                      "explode(InvoiceLineItems) as LineItem")

    def flattenInvoice(selfself,explodedDF):
        return (
                explodedDF.withColumn("ItemCode", expr("LineItem.ItemCode")). \
                withColumn("ItemCode", expr("LineItem.ItemCode")).\
                withColumn("ItemDescription", expr("LineItem.ItemDescription")). \
                withColumn("ItemPrice", expr("LineItem.ItemPrice")). \
                withColumn("ItemQty", expr("LineItem.ItemQty")).\
                withColumn("TotalValue", expr("LineItem.TotalValue")).drop("LineItem")
                )

    def appendIntoDataLake(self,spark, flattenDF, trigger="batch"):
        streamQuery=  (flattenDF.writeStream.format("delta").outputMode("append")\
             .option("checkpointLocation", f"{self.base_data_dir}/checkpoint/invoices")\
                       .option("maxFilesPerTrigger", 1)
                       )

        if(trigger == 'batch'):
            return streamQuery.trigger(availableNow = True).toTable("invoices")
        else:
            return streamQuery.trigger(processingTime=trigger).toTable("invoices")




if __name__=="__main__":
    try:
        ob=InvoiceStreamAndBatch()
        spark=ob.createSparkSession()
        raw_data=ob.ingest_raw_data(spark)
        explodedDF= ob.explodeInvoiceData(raw_data)
        flattenDF = ob.flattenInvoice(explodedDF)
        sQuery= ob.appendIntoDataLake(spark, flattenDF)
        sQuery.stop()


    finally:
        spark.stop()









