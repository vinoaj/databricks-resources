# Databricks notebook source
import requests
import json

from pyspark.sql.types import StructField, StructType, StringType, FloatType, BooleanType

# COMMAND ----------

# MAGIC %md
# MAGIC To make Databricks API calls from a notebook, instead of having to provide your PAT, you can use the `notebookContext`'s API token

# COMMAND ----------

notebookContext = dbutils.notebook.entry_point.getDbutils().notebook().getContext()
token = notebookContext.apiToken().get()
host = notebookContext.apiUrl().get()

# COMMAND ----------

# DBTITLE 1,Helper functions
def build_header():
  header = {
    "Authorization": f"Bearer {token}", 
    # "User-Agent": "API-client-xxxx"
  }
  
  return header


def list_workspace_users():
  response = requests.get(
    url = f"{host}/api/2.0/preview/scim/v2/Users",
    headers = build_header()
  )
  
  return response.json()


# COMMAND ----------

# DBTITLE 1,Get all Workspace users
workspace_users_json = list_workspace_users()
print(json.dumps(workspace_users_json, indent=2))

# COMMAND ----------

# DBTITLE 1,Convert API response to DataFrame
schema_json_str = """
{
  "fields": [
    {
      "metadata": {},
      "name": "active",
      "nullable": true,
      "type": "boolean"
    },
    {
      "metadata": {},
      "name": "displayName",
      "nullable": true,
      "type": "string"
    },
    {
      "metadata": {},
      "name": "emails",
      "nullable": true,
      "type": {
        "containsNull": true,
        "elementType": {
          "keyType": "string",
          "type": "map",
          "valueContainsNull": true,
          "valueType": "string"
        },
        "type": "array"
      }
    },
    {
      "metadata": {},
      "name": "entitlements",
      "nullable": true,
      "type": {
        "containsNull": true,
        "elementType": {
          "keyType": "string",
          "type": "map",
          "valueContainsNull": true,
          "valueType": "string"
        },
        "type": "array"
      }
    },
    {
      "metadata": {},
      "name": "externalId",
      "nullable": true,
      "type": "string"
    },
    {
      "metadata": {},
      "name": "groups",
      "nullable": true,
      "type": {
        "containsNull": true,
        "elementType": {
          "keyType": "string",
          "type": "map",
          "valueContainsNull": true,
          "valueType": "string"
        },
        "type": "array"
      }
    },
    {
      "metadata": {},
      "name": "id",
      "nullable": true,
      "type": "string"
    },
    {
      "metadata": {},
      "name": "name",
      "nullable": true,
      "type": {
        "keyType": "string",
        "type": "map",
        "valueContainsNull": true,
        "valueType": "string"
      }
    },
    {
      "metadata": {},
      "name": "userName",
      "nullable": true,
      "type": "string"
    }
  ],
  "type": "struct"
}
"""

json_resources = workspace_users_json['Resources']

schema_json = json.loads(schema_json_str)
schema = StructType.fromJson(schema_json)

df = spark.createDataFrame(json_resources, schema)

display(df)

# COMMAND ----------

# Quick workaround to get the schema; needed when creating a new DataFrame on this data
# temp_df = spark.createDataFrame([json_resources[22]])
# print(json.dumps(json.loads(temp_df.schema.json()), indent=2))
