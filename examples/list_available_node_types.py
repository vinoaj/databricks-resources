# Databricks notebook source
# MAGIC %md
# MAGIC # List available node types
# MAGIC - This notebook retrieves the available node types in your workspace
# MAGIC - The last cell is an example of how you can query this data to determine which types are relevant for utilising Photon *and* Delta Cache

# COMMAND ----------

import json
import requests

from pyspark.sql.types import StructType

# COMMAND ----------

# DBTITLE 1,Get context info for API calls
notebookContext = dbutils.notebook.entry_point.getDbutils().notebook().getContext()
token = notebookContext.apiToken().get()
host = notebookContext.apiUrl().get()

# COMMAND ----------

# DBTITLE 1,Helper functions
def build_header():
  header = {
    "Authorization": f"Bearer {token}", 
    "User-Agent": f"vm-types; vinny-vijeyakumaar"
  }
  
  return header


# COMMAND ----------

# MAGIC %md
# MAGIC ## Get possible node types on a Workspace > `tvw_node_types`
# MAGIC - Use Databricks' `clusters/list-node-types` API call to determine available node types in the current Databricks workspace

# COMMAND ----------

url = f"{host}/api/2.0/clusters/list-node-types"
valid_node_types = requests.get(url=url, headers=build_header()).json()
display(valid_node_types)

node_types = valid_node_types['node_types']
for node in node_types:
  del node['node_info']

# COMMAND ----------

# DBTITLE 1,Convert API response to DataFrame and temporary view
schema_json_str = '{"fields":[{"metadata":{},"name":"category","nullable":true,"type":"string"},{"metadata":{},"name":"description","nullable":true,"type":"string"},{"metadata":{},"name":"display_order","nullable":true,"type":"long"},{"metadata":{},"name":"instance_type_id","nullable":true,"type":"string"},{"metadata":{},"name":"is_deprecated","nullable":true,"type":"boolean"},{"metadata":{},"name":"is_encrypted_in_transit","nullable":true,"type":"boolean"},{"metadata":{},"name":"is_graviton","nullable":true,"type":"boolean"},{"metadata":{},"name":"is_hidden","nullable":true,"type":"boolean"},{"metadata":{},"name":"is_io_cache_enabled","nullable":true,"type":"boolean"},{"metadata":{},"name":"memory_mb","nullable":true,"type":"long"},{"metadata":{},"name":"node_instance_type","nullable":true,"type":{"keyType":"string","type":"map","valueContainsNull":true,"valueType":"string"}},{"metadata":{},"name":"node_type_id","nullable":true,"type":"string"},{"metadata":{},"name":"num_cores","nullable":true,"type":"double"},{"metadata":{},"name":"num_gpus","nullable":true,"type":"long"},{"metadata":{},"name":"photon_driver_capable","nullable":true,"type":"boolean"},{"metadata":{},"name":"photon_worker_capable","nullable":true,"type":"boolean"},{"metadata":{},"name":"require_fabric_manager","nullable":true,"type":"boolean"},{"metadata":{},"name":"support_cluster_tags","nullable":true,"type":"boolean"},{"metadata":{},"name":"support_ebs_volumes","nullable":true,"type":"boolean"},{"metadata":{},"name":"support_port_forwarding","nullable":true,"type":"boolean"}],"type":"struct"}'

schema_json = json.loads(schema_json_str)
schema = StructType.fromJson(schema_json)

df = spark.createDataFrame(valid_node_types['node_types'], schema)
df.createOrReplaceTempView("tvw_node_types")
display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Sample queries

# COMMAND ----------

# DBTITLE 1,Node types that support Photon + Delta Cache
# MAGIC %sql
# MAGIC SELECT * EXCEPT (display_order, is_deprecated, is_graviton, is_hidden)
# MAGIC FROM tvw_node_types
# MAGIC WHERE 1=1
# MAGIC   AND is_deprecated = "false"
# MAGIC   AND is_io_cache_enabled = "true"
# MAGIC   AND photon_driver_capable = "true"
# MAGIC ORDER BY instance_type_id
