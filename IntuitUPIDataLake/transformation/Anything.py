# from xml.sax.handler import feature_validation
#
# from pyspark.sql.connect.functions import count_distinct
# from pyspark.sql.types import IntegerType, DateType, StringType
#
# parquet --> 3 col (user id , time stamp, activity)
#
# 2nd feature_
# 3rd feb
#
# df =
#
# output: hive table, 3 cols ,
# # uniq users
# # uniq views
# #click throgh rate-- click/views
# # timestamp is null dicard
#
# # 1, 2025-01-01: , click 0
# # 1 , 2025-01-01:, viewa 1
# #1 , 2025-01-01:, viewa 1
# # 2, 2025-01-01:8878, views 1
#
# schmea = StructType([StructField("user_id", IntegerType(), False),
#                      StructField("time", DateType(), False), StructField("action", StringType(),False)])
#
# user_df= spark,read.format("parquet").option("schame").load("path")
#
# output_table= user_df.groupBy("time").agg(count(distinct("user_id")).alias(uniq_user))
#
# df2= user_df.where("status='views'").groupBy("date").agg(count("action").alias("uniq_views"))
#
# -----
#
# user_df.withColumn("is_views", when(col(actions)==viws,1).otherwise(0)).\
#     groupby("date").agg(count(count_distinct(user_id).alias("unq_user"), sum("is_views").alias("#views")))
#
#
# ------