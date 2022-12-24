# Databricks notebook source
# MAGIC %md
# MAGIC # Databricks Demos
# MAGIC 
# MAGIC The `dbdemos` package allows you access to a suite of Databricks' demos
# MAGIC 
# MAGIC Steps:
# MAGIC 1. List available demos: `dbdemos.list_demos()`
# MAGIC 1. Find a demo you are interested in, and run it's `install` command: e.g. `dbdemos.install('delta-lake')`
# MAGIC 
# MAGIC **Please note:**
# MAGIC - **Notebooks**: will be saved in a folder in the directory that you run this package from
# MAGIC - **Resources**: the installation code will create the necessary resources (e.g. clusters, Delta Live Tables pipelines, SQL dashboards) that are required to operate the demo
# MAGIC     - If you don't have permissions for creating any of the resources, please ask an Admin to install the demo for you, and to give you permissions to access those resources
# MAGIC - **Cleanup**: currently the demos do **not** have cleanup functionality. If you no longer require the resources created, you will need to manually delete them yourself

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 1: install `dbdemos` and list demos

# COMMAND ----------

!pip install dbdemos --quiet

import dbdemos
dbdemos.list_demos()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 2: install desired demo

# COMMAND ----------

dbdemos.install('delta-lake')
