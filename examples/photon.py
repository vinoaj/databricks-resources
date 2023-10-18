# Databricks notebook source
# MAGIC %md
# MAGIC # Working with Photon

# COMMAND ----------

# MAGIC %md
# MAGIC ## List supported expressions
# MAGIC This command should be run on a cluster using a DBR that supports Photon

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *, CURRENT_DATE() FROM photon_exprs
