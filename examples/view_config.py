# Databricks notebook source
# MAGIC %md
# MAGIC # View Notebook & Cluster Configuration
# MAGIC This Notebook demonstrates how to programmatically access Notebook & Cluster configuration and context values

# COMMAND ----------

import json
from pprint import pprint

# COMMAND ----------

# MAGIC %md
# MAGIC ## View Notebook execution context attributes

# COMMAND ----------

print(json.dumps(
   json.loads(
     dbutils.notebook.entry_point.getDbutils().notebook().getContext().toJson()), 
     indent=2
   )
)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Identify Cloud

# COMMAND ----------

# Option 1
cloud = spark.conf.get("spark.databricks.clusterUsageTags.cloudProvider").upper()
print(f"Cloud (using Option 1): {cloud}")

# Option 2
hostname = dbutils.notebook.entry_point.getDbutils().notebook().getContext().browserHostName().get()
cloud = None
if ".gcp.databricks.com" in hostname:
    cloud = "GCP"
elif ".cloud.databricks.com" in hostname:
    cloud = "AWS"
elif ".azuredatabricks.net" in hostname:
    cloud = "AZURE"
print(f"Cloud (using Option 2): {cloud} (determined from hostname {hostname})")


# COMMAND ----------

# MAGIC %md
# MAGIC ## View Cluster configuration

# COMMAND ----------

pprint(spark.sparkContext.getConf().getAll())

# COMMAND ----------

# MAGIC %md
# MAGIC ### Identify if Cluster is running Photon

# COMMAND ----------

import re

CONF_KEYS = ["spark.databricks.clusterUsageTags.runtimeEngine", "spark.databricks.clusterUsageTags.sparkVersion", 
             "spark.databricks.clusterUsageTags.effectiveSparkVersion"]
RE_LOOKUP = "^.*photon.*$"

def is_photon_cluster() -> bool:
  for conf_key in CONF_KEYS:
    try:
      config_val = spark.conf.get(conf_key)
      if(re.search(RE_LOOKUP, config_val, re.IGNORECASE)):
        return True
    except:
      pass
    
  return False

# COMMAND ----------

is_photon_cluster()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Put Cluster configuration into a DataFrame

# COMMAND ----------

from pprint import pprint
conf = spark.sparkContext.getConf().getAll()
conf.sort(key=lambda tup: tup[0])
conf = spark.createDataFrame(conf, ["conf_key", "conf_val"])
conf.createOrReplaceTempView("tvw_spark_conf")
display(conf)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Search for a specific configuration value (DataFrame)

# COMMAND ----------

# Search for a specific value
from pyspark.sql.functions import col

# Regular expressions in PySpark need to be expressed in Java regular expression notation
RE_SEARCH = "(?i)^.*photon.*$"

df_filtered = conf.filter(col("conf_val").rlike(RE_SEARCH))
display(df_filtered)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Search for a specific configuration value (SQL)

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM tvw_spark_conf
# MAGIC WHERE REGEXP_LIKE(conf_val, "(?i)^.*photon.*$")
