# Databricks notebook source
# MAGIC %md
# MAGIC # Call Databricks REST APIs from inside a Notebook
# MAGIC 
# MAGIC This Notebook documents how you can call Databricks' REST APIs from inside of a Notebook itself
# MAGIC 
# MAGIC * You do not have to utilise a PAT to authenticate. Instead, the current user's token held in the `notebookContext` is utilised

# COMMAND ----------

import requests
import json

# COMMAND ----------

notebookContext = dbutils.notebook.entry_point.getDbutils().notebook().getContext()
token = notebookContext.apiToken().get()
host = notebookContext.apiUrl().get()

def build_header():
  header = {
    "Authorization": f"Bearer {token}", 
    # "User-Agent": f"your_user_agent_string:{variables}"
  }
  
  return header


# COMMAND ----------

def list_available_spark_versions():
    """List available Spark (DBR) versions

    Returns:
        json: payload of available Spark/DBR versions
    """
    response = requests.get(
        url = f"{host}/api/2.0/clusters/spark-versions",
        headers = build_header()
    )

    return response.json()

# COMMAND ----------

print(json.dumps(list_available_spark_versions(), indent=2))

# COMMAND ----------

def list_sql_warehouses():
  response = requests.get(
    url = f"{host}/api/2.0/sql/warehouses/",
    headers = build_header()
  )
  
  return response.json()


def get_sql_warehouse(warehouse_id, debug=True):
  url = f"{host}/api/2.0/sql/warehouses/{warehouse_id}"
  if debug:
    url += "?debug=true"
    
  response = requests.get(
    url = url,
    headers = build_header()
  )
  
  return response.json()


def create_sql_warehouse(config_json):
  response = requests.post(
    url = f"{host}/api/2.0/sql/warehouses/",
    headers = build_header(),
    data = config_json
  )
  
  return response.json()


def edit_sql_warehouse(warehouse_id, config_json):
  response = requests.post(
      url = f"{host}/api/2.0/sql/warehouses/{warehouse_id}/edit",
      headers = build_header(),
      data = config_json
  )
  
  return response.json()


def edit_cluster(cluster_id, config_json):
  response = requests.post(
      url = f"{host}/api/2.0/clusters/edit",
      headers = build_header(),
      data = config_json
  )
  
  return response.json()



# COMMAND ----------

warehouses = list_sql_warehouses()
print(json.dumps(warehouses, indent=2))

# COMMAND ----------

for warehouse in warehouses["warehouses"]:
  if warehouse["creator_name"] == "vinny.vijeyakumaar@databricks.com":
    print(json.dumps(warehouse, indent=2))

# COMMAND ----------

config = {
  "name": "vinny-vijeyakumaar-custom-warehouse",
  "cluster_size": "Small",
  "min_num_clusters": 1,
  "max_num_clusters": 4,
  "auto_stop_mins": 15,
  "tags": {
    "custom_tags": [
      {
        "key": "Owner",
        "value": "vinny.vijeyakumaar@databricks.com"
      }
    ]
  },
  "enable_photon": "true",
  "enable_serverless_compute": "false"
}

config_json = json.dumps(config)

# COMMAND ----------

create_sql_warehouse(config_json)

# COMMAND ----------

warehouse_config = get_sql_warehouse("ABCD1234567", True)
print(json.dumps(warehouse_config, indent = 2))

# COMMAND ----------

conn_hostname = warehouse_config["odbc_params"]["hostname"]
conn_path = warehouse_config["odbc_params"]["path"]
print(f"{conn_hostname}{conn_path}")

# COMMAND ----------

from databricks import sql

with sql.connect(
  server_hostname=conn_hostname,
  http_path=conn_path,
  access_token=token
) as connection:
  with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM vinny_vijeyakumaar.retail_suppliers LIMIT 1000")
    

# COMMAND ----------

cluster_id = "ABCD-123456-abcdefg"

cluster_edit = {
  "spark_version": IMAGE_NAME
}
cluster_edit["cluster_id"] = cluster_id
cluster_edit["node_type_id"] = "r5d.large"
cluster_edit["num_workers"] = 4
cluster_edit_json = json.dumps(cluster_edit)

print(cluster_edit_json)

edit_cluster(cluster_id, cluster_edit_json)
