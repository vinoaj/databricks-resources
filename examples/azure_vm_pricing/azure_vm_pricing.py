# Databricks notebook source
# MAGIC %md
# MAGIC # Querying Azure Pricing Data
# MAGIC This notebook demonstrates a number of Databricks Notebook features:
# MAGIC - Ability to paramaterize SQL queries via `dbutils.widgets()` variables
# MAGIC - Working with Unity Catalog managed tables
# MAGIC - Querying and storing data from the Azure pricing API
# MAGIC 
# MAGIC **Note**: the below examples assume the use of tables managed by Unity Catalog. Hence they are usually created and accessed by a `<catalog>.<schema>.<table>` naming hierarchy. If you are not using Unity Catalog, you will need to modify the below statements using a `<schema>.<table>` naming convention

# COMMAND ----------

CATALOG = "vinny_vijeyakumaar"
SCHEMA = "consumption_planning"

dbutils.widgets.removeAll()
dbutils.widgets.text("UCCatalog", CATALOG)
dbutils.widgets.text("UCSchema", SCHEMA)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Reading materialised data
# MAGIC - Below is the materialised data, and how to query it for relevant information 
# MAGIC - To replicate the ETL pattern in your environment, please see the <a target="_parent" href="#notebook/837191481135802/command/5470662638995">`ETL` section</a> instead

# COMMAND ----------

# MAGIC %sql
# MAGIC USE CATALOG $UCCatalog;
# MAGIC USE SCHEMA $UCSchema;
# MAGIC 
# MAGIC SHOW TABLES IN $UCSchema;

# COMMAND ----------

# MAGIC %md
# MAGIC ### DBU pricing

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Get DBU pricing for your region
# MAGIC SELECT *
# MAGIC FROM azure_dbu_pricing
# MAGIC WHERE armRegionName = "australiaeast"

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Another DBU pricing example
# MAGIC SELECT *
# MAGIC FROM azure_dbu_pricing
# MAGIC WHERE 1=1
# MAGIC   AND armRegionName IN ("australiaeast")
# MAGIC   AND tier = "Premium"
# MAGIC   AND meterName LIKE "%Photon%"

# COMMAND ----------

# MAGIC %md
# MAGIC ### Which Instance types does Azure Databricks support?

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Available node types for your Azure Databricks Workspace
# MAGIC SELECT *
# MAGIC FROM azure_node_types

# COMMAND ----------

# MAGIC %md
# MAGIC ### DBUs per hour by Instance type

# COMMAND ----------

# MAGIC %sql
# MAGIC -- DBUs per hour based on Instance type
# MAGIC -- If (armSkuName == NULL) it means there is an instance type that Databricks supports that is not
# MAGIC --   listed on Azure's pricing page
# MAGIC SELECT *
# MAGIC FROM azure_dbus_per_hr_by_instance_type
# MAGIC ORDER BY armSkuName

# COMMAND ----------

# MAGIC %md
# MAGIC ### Azure VM pricing

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Azure VM pricing (includes assumptions on 70%, 80%, 90% spot) for all possible Databricks node types
# MAGIC SELECT * 
# MAGIC FROM azure_vm_pricing_silver
# MAGIC WHERE armRegionName = "australiaeast"
# MAGIC ORDER BY armSkuName

# COMMAND ----------

# MAGIC %md
# MAGIC ### Putting it all together: VM pricing & DBUs per hour

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Putting VM pricing and DBUs/hour information together
# MAGIC SELECT p.armRegionName, p.armSkuName, p.productName, di.dbus_per_hour, p.currencyCode
# MAGIC   , p.retailPrice, p.spot70pct, p.spot80pct, p.spot90pct
# MAGIC   , p.* EXCEPT (armRegionName, armSkuName, productName, currencyCode, retailPrice, spot70pct, spot80pct, spot90pct)
# MAGIC   , di.* EXCEPT (dbus_per_hour, armSkuName)
# MAGIC FROM azure_vm_pricing_silver p
# MAGIC LEFT JOIN azure_dbus_per_hr_by_instance_type di
# MAGIC   ON p.armSkuName = di.armSkuName
# MAGIC WHERE p.armRegionName = "australiaeast"
# MAGIC ORDER BY di.armSkuName

# COMMAND ----------

# MAGIC %md
# MAGIC ### Putting it all together: the kitchen sink

# COMMAND ----------

# Pivot SKUs to columns
df = spark.sql(f"""
  SELECT *
  FROM {getArgument("UCCatalog")}.{getArgument("UCSchema")}.azure_dbu_pricing
  WHERE 1=1
    AND armRegionName IN ("australiaeast")
    AND tier = "Premium"
    AND meterName LIKE "%Photon%"
""")

dfp = df.toPandas()
dfp = dfp.pivot(index="armRegionName", columns="meterName", values="unitPrice")
dfp.columns = [col.replace(" ", "_") for col in dfp.columns]
dfp.reset_index(inplace=True)

df_dbus = spark.createDataFrame(dfp).createOrReplaceTempView("tvw_dbus_pivot")
display(df_dbus)

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Putting VM pricing, DBUs/hour, and $DBU information together
# MAGIC SELECT p.armRegionName, p.armSkuName, p.productName, di.dbus_per_hour, p.currencyCode
# MAGIC   , p.retailPrice, p.spot70pct, p.spot80pct, p.spot90pct
# MAGIC   , dp.* EXCEPT (armRegionName)
# MAGIC   , p.* EXCEPT (armRegionName, armSkuName, productName, currencyCode, retailPrice, spot70pct, spot80pct, spot90pct)
# MAGIC   , di.* EXCEPT (dbus_per_hour, armSkuName)
# MAGIC FROM azure_vm_pricing_silver p
# MAGIC LEFT JOIN azure_dbus_per_hr_by_instance_type di 
# MAGIC   ON p.armSkuName = di.armSkuName
# MAGIC INNER JOIN tvw_dbus_pivot dp
# MAGIC   ON p.armRegionName = dp.armRegionName
# MAGIC WHERE p.armRegionName = "australiaeast"
# MAGIC ORDER BY di.armSkuName

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC ## ETL

# COMMAND ----------

!pip install bs4

# COMMAND ----------

import json
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode
from pyspark.sql.functions import expr
from pyspark.sql.types import StructField, StructType, StringType, FloatType, BooleanType

# COMMAND ----------

URL_PRICING = "https://azure.microsoft.com/en-au/pricing/details/databricks/"
RETAIL_PRICE_ENDPOINT = "https://prices.azure.com/api/retail/prices"
AZURE_API_FILTER_DBUS = "serviceName eq 'Azure Databricks'"
AZURE_API_FILTER_VMS = "serviceName eq 'Virtual Machines'"

AZURE_PRICE_ITEMS_SCHEMA = StructType([
  StructField('currencyCode', StringType(), True),
  StructField('tierMinimumUnits', FloatType(), True),
  StructField('retailPrice', FloatType(), True),
  StructField('unitPrice', FloatType(), True),
  StructField('armRegionName', StringType(), True),
  StructField('location', StringType(), True),
  StructField('effectiveStartDate', StringType(), True),
  StructField('meterId', StringType(), True),
  StructField('meterName', StringType(), True),
  StructField('productId', StringType(), True),
  StructField('skuId', StringType(), True),
  StructField('availabilityId', StringType(), True),
  StructField('productName', StringType(), True),
  StructField('skuName', StringType(), True),
  StructField('serviceName', StringType(), True),
  StructField('serviceId', StringType(), True),
  StructField('serviceFamily', StringType(), True),
  StructField('unitOfMeasure', StringType(), True),
  StructField('type', StringType(), True),
  StructField('isPrimaryMeterRegion', BooleanType(), True),
  StructField('armSkuName', StringType(), True),
])

notebookContext = dbutils.notebook.entry_point.getDbutils().notebook().getContext()
token = notebookContext.apiToken().get()
host = notebookContext.apiUrl().get()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Helper Functions

# COMMAND ----------

def get_azure_prices(currency_code:str="USD", filter:str=""):
  params = {
    "api-version": "2021-10-01-preview",
    "currencyCode": currency_code,
    "$filter": filter
  }

  url = f"{RETAIL_PRICE_ENDPOINT}?{urlencode(params)}"
  print(f"Fetching results from {url}")

  items = []

  price_data = requests.get(url).json()
  items = items + price_data["Items"]

  while "NextPageLink" in price_data and price_data["NextPageLink"] is not None:
    price_data = requests.get(price_data["NextPageLink"]).json()
    items = items + price_data["Items"]

  print(f"{len(items)} items fetched")
  return items


def build_header():
  header = {
    "Authorization": f"Bearer {token}", 
    "User-Agent": f"azure-pricing; vinny-vijeyakumaar"
  }
  
  return header


# COMMAND ----------

# MAGIC %md
# MAGIC ### Get Azure Databricks DBU pricing > `azure_dbu_pricing`

# COMMAND ----------

items = get_azure_prices("USD", AZURE_API_FILTER_DBUS)
df = spark.createDataFrame(items, AZURE_PRICE_ITEMS_SCHEMA)
df.createOrReplaceTempView("tvw_azure_pricing")
display(df)

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE $UCCatalog.$UCSchema.azure_dbu_pricing 
# MAGIC AS
# MAGIC   SELECT armRegionName, meterName
# MAGIC     , CASE
# MAGIC         WHEN CONTAINS(meterName, 'Standard') THEN 'Standard'
# MAGIC         WHEN CONTAINS(meterName, 'Premium') THEN 'Premium'
# MAGIC         ELSE 'Unknown'
# MAGIC       END AS tier
# MAGIC     , unitPrice, unitOfMeasure
# MAGIC     , * EXCEPT(armRegionName, meterName, unitPrice, unitOfMeasure) 
# MAGIC   FROM tvw_azure_pricing;
# MAGIC 
# MAGIC 
# MAGIC SELECT * FROM $UCCatalog.$UCSchema.azure_dbu_pricing
# MAGIC ORDER BY armRegionName, tier, meterName;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Get possible node types on a Azure Databricks Workspace > `azure_node_types`
# MAGIC - Azure Databricks' pricing page doesn't always have all possible instance types listed
# MAGIC - Therefore we use Databricks' `clusters/list-node-types` API call to determine available node types in the current Azure Databricks workspace

# COMMAND ----------

url = f"{host}/api/2.0/clusters/list-node-types"
valid_node_types = requests.get(url=url, headers=build_header()).json()
display(valid_node_types)

node_types = valid_node_types['node_types']
for node in node_types:
  del node['node_info']

# COMMAND ----------

# Quick workaround to get the schema; needed when creating a new DataFrame on this data
# temp_df = spark.createDataFrame([node_types[0]])
# temp_df.schema.json()

# COMMAND ----------

schema_json_str = '{"fields":[{"metadata":{},"name":"category","nullable":true,"type":"string"},{"metadata":{},"name":"description","nullable":true,"type":"string"},{"metadata":{},"name":"display_order","nullable":true,"type":"long"},{"metadata":{},"name":"instance_type_id","nullable":true,"type":"string"},{"metadata":{},"name":"is_deprecated","nullable":true,"type":"boolean"},{"metadata":{},"name":"is_encrypted_in_transit","nullable":true,"type":"boolean"},{"metadata":{},"name":"is_graviton","nullable":true,"type":"boolean"},{"metadata":{},"name":"is_hidden","nullable":true,"type":"boolean"},{"metadata":{},"name":"is_io_cache_enabled","nullable":true,"type":"boolean"},{"metadata":{},"name":"memory_mb","nullable":true,"type":"long"},{"metadata":{},"name":"node_instance_type","nullable":true,"type":{"keyType":"string","type":"map","valueContainsNull":true,"valueType":"string"}},{"metadata":{},"name":"node_type_id","nullable":true,"type":"string"},{"metadata":{},"name":"num_cores","nullable":true,"type":"double"},{"metadata":{},"name":"num_gpus","nullable":true,"type":"long"},{"metadata":{},"name":"photon_driver_capable","nullable":true,"type":"boolean"},{"metadata":{},"name":"photon_worker_capable","nullable":true,"type":"boolean"},{"metadata":{},"name":"require_fabric_manager","nullable":true,"type":"boolean"},{"metadata":{},"name":"support_cluster_tags","nullable":true,"type":"boolean"},{"metadata":{},"name":"support_ebs_volumes","nullable":true,"type":"boolean"},{"metadata":{},"name":"support_port_forwarding","nullable":true,"type":"boolean"}],"type":"struct"}'

schema_json = json.loads(schema_json_str)
schema = StructType.fromJson(schema_json)

df = spark.createDataFrame(valid_node_types['node_types'], schema)
df.createOrReplaceTempView("tvw_azure_node_types")
display(df)

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE $UCCatalog.$UCSchema.azure_node_types
# MAGIC SELECT category, description, num_cores, memory_mb
# MAGIC   , * EXCEPT (category, description, num_cores, memory_mb, node_instance_type)
# MAGIC FROM tvw_azure_node_types;
# MAGIC 
# MAGIC SELECT * FROM $UCCatalog.$UCSchema.azure_node_types
# MAGIC ORDER BY category, description;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Get Azure VM pricing > `azure_vm_pricing` > `azure_vm_pricing_silver`

# COMMAND ----------

items = get_azure_prices("USD", AZURE_API_FILTER_VMS)
df = spark.createDataFrame(items, AZURE_PRICE_ITEMS_SCHEMA)
df.createOrReplaceTempView("tvw_azure_vm_pricing")
display(df)

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE $UCCatalog.$UCSchema.azure_vm_pricing
# MAGIC SELECT armRegionName, armSkuName, meterName, skuName, productName, retailPrice, unitPrice, unitOfMeasure
# MAGIC   , * EXCEPT (armRegionName, armSkuName, meterName, skuName, productName, retailPrice
# MAGIC               , unitPrice, unitOfMeasure)
# MAGIC FROM tvw_azure_vm_pricing;
# MAGIC 
# MAGIC SELECT *
# MAGIC FROM $UCCatalog.$UCSchema.azure_vm_pricing
# MAGIC ORDER BY armRegionName, meterName;

# COMMAND ----------

# MAGIC %md
# MAGIC #### `azure_vm_pricing_silver`
# MAGIC **Filtering** down raw VM pricing data to
# MAGIC - Only VMs supported by Databricks
# MAGIC - Non-Windows VMs
# MAGIC - Non-Low-Priority VMs
# MAGIC - Non-Spot (we'll calculate spot rates separately)
# MAGIC - SKUs classified as `Consumption` 
# MAGIC 
# MAGIC **Enrichment**:
# MAGIC - Spot pricing scenarios for 70%, 80%, 90% spot savings on `retailPrice`

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE $UCCatalog.$UCSchema.azure_vm_pricing_silver
# MAGIC AS
# MAGIC   WITH filtered AS (
# MAGIC     SELECT np.*
# MAGIC     FROM $UCCatalog.$UCSchema.azure_vm_pricing np
# MAGIC       INNER JOIN $UCCatalog.$UCSchema.azure_node_types nt
# MAGIC       ON np.armSkuName = nt.description
# MAGIC     WHERE 1=1
# MAGIC       AND productName NOT LIKE "%Windows%"
# MAGIC       AND skuName NOT LIKE "%Low Priority%"
# MAGIC       -- Excluding because later we'll create spot saving scenarios based on 70%, 80%, 90% assumptions
# MAGIC       AND skuName NOT LIKE "%Spot%"
# MAGIC       AND np.type IN ("Consumption")
# MAGIC   )
# MAGIC   SELECT armRegionName, armSkuName, productName, currencyCode, retailPrice
# MAGIC     , ROUND(retailPrice * (1 - 0.70), 3) AS spot70pct
# MAGIC     , ROUND(retailPrice * (1 - 0.80), 3) AS spot80pct
# MAGIC     , ROUND(retailPrice * (1 - 0.90), 3) AS spot90pct
# MAGIC     , * EXCEPT (armRegionName, armSkuName, productName, currencyCode, retailPrice)
# MAGIC   FROM filtered;
# MAGIC 
# MAGIC SELECT * FROM $UCCatalog.$UCSchema.azure_vm_pricing_silver
# MAGIC ORDER BY armRegionName, armSkuName

# COMMAND ----------

# MAGIC %md
# MAGIC ### Get DBUs per hour per Instance type > `azure_dbus_per_hr_by_instance_type`
# MAGIC - This information isn't available via either Azure's or Databricks' APIs
# MAGIC - So instead we'll infer this data from the pricing page
# MAGIC - Currently only looks at DBUs/hr per Instance

# COMMAND ----------

html = requests.get(URL_PRICING).text
soup = BeautifulSoup(html, "html.parser")
pricing_tables = soup.select("div.databricks-table table.data-table__table--pricing")

columns = ["instance", "vcpus", "ram", "dbus_per_hour"]
vals = []

for table in pricing_tables:
  headings = table.select("tr:first-of-type th")
  if headings[0].string != "Instance":
    continue
    
  rows = table.select("tr")[1:]
  for row in rows:
    tds = row.select("td")
    instance = tds[0].string.strip()
    vcpus = tds[1].string.strip()
    ram = tds[2].string.strip()
    dbus_per_hr = tds[3].string.strip()
    
    vals.append((instance, vcpus, ram, dbus_per_hr))

# Remove duplicate rows
vals = list(set(vals))

df = spark.createDataFrame(vals, columns)
df.createOrReplaceTempView("tvw_dbus_per_hour")
display(df)

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE $UCCatalog.$UCSchema.azure_dbus_per_hr_by_instance_type
# MAGIC AS
# MAGIC   WITH cleansed AS (
# MAGIC     SELECT instance
# MAGIC     , CONCAT("Standard_", REPLACE(instance, " ", "_")) AS armSkuName
# MAGIC     , CAST(vcpus AS INT) AS vcpus
# MAGIC     , CAST(REPLACE(ram, " GiB", "") AS FLOAT) AS ram
# MAGIC     , CAST(dbus_per_hour AS FLOAT) AS dbus_per_hour
# MAGIC     FROM tvw_dbus_per_hour
# MAGIC   )
# MAGIC   SELECT c.*, ntypes.*
# MAGIC   FROM $UCCatalog.$UCSchema.azure_node_types ntypes
# MAGIC   LEFT JOIN cleansed c ON ntypes.description = c.armSkuName;
# MAGIC 
# MAGIC 
# MAGIC SELECT * FROM $UCCatalog.$UCSchema.azure_dbus_per_hr_by_instance_type
# MAGIC ORDER BY armSkuName;

# COMMAND ----------


