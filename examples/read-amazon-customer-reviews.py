# Databricks notebook source
# MAGIC %md
# MAGIC # Ingest Amazon Customer Reviews Dataset
# MAGIC 
# MAGIC This notebook demonstrates ingesting the [Amazon Customer Reviews Dataset](https://s3.amazonaws.com/amazon-reviews-pds/readme.html) provided by Amazon into a Delta table
# MAGIC 
# MAGIC Run this Notebook with a cluster that has permissions to access Amazon's public bucket at `s3://amazon-reviews-pds/parquet/`. You can do so with an [instance profile](https://docs.databricks.com/aws/iam/instance-profile-tutorial.html) or with the appropriate [Spark settings](https://docs.databricks.com/storage/amazon-s3.html#global-configuration) on your cluster
# MAGIC 
# MAGIC Alternatively you can connect to S3 in your Notebook by [using AWS keys](https://docs.databricks.com/storage/amazon-s3.html#access-s3-buckets-with-uris-and-aws-keys). Please be sure to store your key in secrets and not reveal them anywhere in plaintext!

# COMMAND ----------

CATALOG = "main" # Use hive_metastore if you don't have Unity Catalog enabled
SCHEMA = "vinny_vijeyakumaar_demo_retail"
S3_PATH_PARQUET = "s3://amazon-reviews-pds/parquet/"
TARGET_TABLE = "raw_amazon_reviews_pds"

dbutils.widgets.removeAll()
dbutils.widgets.text("catalog", CATALOG)
dbutils.widgets.text("schema", SCHEMA)
dbutils.widgets.text("target_table", TARGET_TABLE)

# COMMAND ----------

# MAGIC %sql
# MAGIC USE CATALOG ${catalog};
# MAGIC 
# MAGIC CREATE SCHEMA IF NOT EXISTS ${schema};
# MAGIC USE SCHEMA ${schema};

# COMMAND ----------

display(dbutils.fs.ls(S3_PATH_PARQUET))

# COMMAND ----------

df = spark.read.parquet(S3_PATH_PARQUET)
display(df)

# COMMAND ----------

# Coalesce into a single partition as partitioning tables < 1TB has 
#   no performance benefits with Photon
df = df.repartition(1)
df.write.mode("overwrite").saveAsTable(TARGET_TABLE)

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*)
# MAGIC FROM $target_table
# MAGIC WHERE product_category IN ("Grocery")
# MAGIC --LIMIT 10
# MAGIC ;

# COMMAND ----------
