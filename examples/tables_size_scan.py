# Databricks notebook source
# MAGIC %md
# MAGIC # Gathering Table Sizes
# MAGIC 
# MAGIC This Notebook demonstrates how to retrieve table sizes across your schemas (databases) as well as the physical size taken up at your table's file location
# MAGIC 
# MAGIC Based on this information you can take actions such as:
# MAGIC - Running `OPTIMIZE` and `VACUUM` on tables where the table size greatly exceeds the path's combined file sizes (usually indicates a lot of outdated records that are no longer required)
# MAGIC - Convert non Delta Lake tables to Delta Lake tables
# MAGIC 
# MAGIC Prerequisites:
# MAGIC - The user who executes this should have access to all the relevant schemas and tables in your environment
# MAGIC - The cluster should be configured (e.g. via instance profiles or cluster configuration settings) with the necessary permissions to scan the table's file path (e.g. a cloud storage bucket)
# MAGIC   - If permissions are missing for a path, a size of `0` will be returned for that path
# MAGIC 
# MAGIC The method for determining table sizes will depend upon if you are using Unity Catalog or not.
# MAGIC 
# MAGIC * If you're using **Unity Catalog**: query the `INFORMATION_SCHEMA` tables
# MAGIC * If you're **NOT** using Unity Catalog: run Python scripts below to build out the information

# COMMAND ----------

# Schema & table to store your table metadata info
SINK_SCHEMA = "vinny_vijeyakumaar_demo_retail"
SINK_TABLE = "table_metadata"

dbutils.widgets.removeAll()
dbutils.widgets.text("sink_schema", SINK_SCHEMA)
dbutils.widgets.text("sink_table", SINK_TABLE)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Workflow: Unity Catalog (UC) Workspace environment
# MAGIC 
# MAGIC ... Coming soon ...

# COMMAND ----------

# MAGIC %md
# MAGIC ## Workflow: non-UC Workspace environment

# COMMAND ----------

# MAGIC %sql
# MAGIC USE CATALOG hive_metastore;

# COMMAND ----------

from concurrent.futures import ThreadPoolExecutor
from functools import reduce
from pyspark.sql.functions import lit, sum as _sum
from pyspark.sql.types import LongType, StringType, StructField, StructType
from pyspark.sql.utils import AnalysisException


def get_table_details(row):
    """Return DESCRIBE DETAIL output as a DataFrame"""
    try:
        df = spark.sql(
            f"DESCRIBE DETAIL {row['database']}.{row['tableName']}"
        ).withColumn("tableName", lit(row["tableName"]))
        return df
    except AnalysisException as e:
        if "is a view" in str(e):
            # Table is a view
            return None
        else:
            raise e


def get_storage_size(row):
    """Return the sum of file sizes at a given storage location (must be accessible by dbutils.fs.ls())"""

    location = row["location"]

    schema_output = StructType(
        [
            StructField("location", StringType(), True),
            StructField("total_size", LongType(), True),
        ]
    )

    try:
        fs_ls_output = dbutils.fs.ls(row["location"])
    except Exception as e:
        if "java.io.FileNotFoundException" in str(e):
            # Path doesn't exist or executor doesn't have permissions
            print(f"Caught FileNotFoundException: {location}")

            return spark.createDataFrame([(location, 0)], schema=schema_output)
        else:
            # If the exception is caused by a different issue, raise the exception
            raise e

    df = spark.createDataFrame(fs_ls_output)
    path_size = df.agg(_sum("size")).collect()[0][0]

    return spark.createDataFrame([(location, path_size)], schema=schema_output)


def get_schema_table_info(schema_name: str):
    # Get tables in schema, ignore temporary tables
    df_tables = spark.sql(f"SHOW TABLES IN {schema_name}").filter(
        "isTemporary == false"
    )

    # Collect DESCRIBE DETAIL information for each table
    with ThreadPoolExecutor() as executor:
        tables_info = list(executor.map(get_table_details, df_tables.collect()))

    # Drop None results (indicates table was a view)
    tables_info = filter(lambda df: df is not None, tables_info)
    df_tables_info = reduce(lambda df1, df2: df1.union(df2), tables_info)

    # Get storage consumed at each physical location
    with ThreadPoolExecutor() as executor:
        locations_info = list(
            executor.map(
                get_storage_size, df_tables_info.select("location").distinct().collect()
            )
        )

    df_locations_info = reduce(lambda df1, df2: df1.union(df2), locations_info)
    df_locations_info = df_locations_info.dropDuplicates()

    # Merge table info and storage location info
    df_tables_info_all = df_tables.join(
        df_tables_info, on="tableName", how="inner"
    ).join(df_locations_info, on="location", how="inner")

    return df_tables_info_all


# COMMAND ----------

df_schemas = spark.sql("SHOW SCHEMAS")
schema_list = [
    row["databaseName"] for row in df_schemas.select("databaseName").collect()
]

# Debugging
schema_list = ["00vsdb", "vinny_vijeyakumaar_demo_retail"]

with ThreadPoolExecutor() as executor:
    table_dfs = list(executor.map(get_schema_table_info, schema_list))

df_tables_info = reduce(lambda df1, df2: df1.union(df2), table_dfs)
df_tables_info.createOrReplaceTempView("vw_table_metadata")

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE $sink_schema.$sink_table
# MAGIC COMMENT "Table scan metadata results"
# MAGIC AS
# MAGIC SELECT database, tableName, format, numFiles, sizeInBytes,
# MAGIC   ((total_size - sizeInBytes)/sizeInBytes) * 100 AS sizeDiscrepancyPct,
# MAGIC   (sizeInBytes / 1024.0 / 1024.0 / 1024.0) as sizeInGB,
# MAGIC   total_size AS pathSizeInBytes,
# MAGIC   (total_size / 1024.0 / 1024.0 / 1024.0) as pathSizeInGB,
# MAGIC   (pathSizeInBytes - sizeInBytes) AS sizeDiscrepancyInBytes,
# MAGIC   location, name, description,
# MAGIC   * EXCEPT (database, tableName, format, numFiles, sizeInBytes, total_size, location, name, description, isTemporary)
# MAGIC FROM vw_table_metadata

# COMMAND ----------

# MAGIC %md
# MAGIC ## View results

# COMMAND ----------

# MAGIC %sql SELECT * FROM $sink_schema.$sink_table

# COMMAND ----------

# MAGIC %md
# MAGIC ## Action: explore OPTIMIZE and VACUUM for tables where location physical size >> table size
# MAGIC 
# MAGIC [Refer to this checklist](https://github.com/vinoaj/databricks-resources/blob/main/checklists/performance-tuning.md#storage-optimisations) for steps to consider when applying `OPTIMIZE` and `VACUUM` to your tables

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM $sink_schema.$sink_table
# MAGIC WHERE sizeDiscrepancyPct > 0 OR sizeDiscrepancyPct IS NULL
# MAGIC ORDER BY sizeDiscrepancyPct DESC

# COMMAND ----------

# MAGIC %md
# MAGIC ## Action: convert non-Delta tables to Delta

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM $sink_schema.$sink_table
# MAGIC WHERE format != "delta"
# MAGIC ORDER BY database, tableName
