from pyspark.sql.functions import *
from pyspark.sql.types import  *
from pyspark.sql import SparkSession
from delta import configure_spark_with_delta_pip


class InvoiceStream():

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

    def appendIntoDataLake(self,spark, flattenDF):
       return  (flattenDF.writeStream.format("csv").outputMode("append")\
         .option("checkpointLocation", f"{self.base_data_dir}/checkpoint/invoices") \
         .toTable("invoices"))


if __name__=="__main__":
    try:
        ob=InvoiceStream()
        spark=ob.createSparkSession()
        raw_data=ob.ingest_raw_data(spark)
        explodedDF= ob.explodeInvoiceData(raw_data)
        flattenDF = ob.flattenInvoice(explodedDF)
        sQuery= ob.appendIntoDataLake(spark, flattenDF)
        sQuery.stop()


    finally:
        spark.stop()









