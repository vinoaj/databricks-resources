# Databricks notebook source
# MAGIC %md
# MAGIC # Databricks Network Connectivity

# COMMAND ----------

# MAGIC %md
# MAGIC ## Testing network connectivity
# MAGIC To test network connectivity from a cluster, run the `nc` command from a Notebook attached to that cluster. For example, this command tests connectivity to Databricks’ `GCP` metastore in `us-central1`

# COMMAND ----------

# MAGIC %sh nc -vz 35.239.64.150 3306
