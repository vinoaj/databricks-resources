# Databricks notebook source
# MAGIC %md
# MAGIC # Working with bamboolib
# MAGIC 
# MAGIC `bamboolib` is a user interface component that allows no-code data analysis and transformations from within a Databricks notebook. 
# MAGIC 
# MAGIC `bamboolib` helps users more easily work with their data and speeds up common data wrangling, exploration, and visualization tasks. 
# MAGIC 
# MAGIC As users complete these kinds of tasks with their data, `bamboolib` automatically generates Python code in the background. Users can share this code with others, who can run this code in their own notebooks to quickly reproduce those original tasks

# COMMAND ----------

!pip install bamboolib --quiet

# COMMAND ----------

import bamboolib as bam

# COMMAND ----------

# MAGIC %md
# MAGIC To use `bamboolib` on demo data, run `bam` and then do the following:
# MAGIC * Click on "Load dummy data"
# MAGIC * Select one of the datasets
# MAGIC * Click on "Execute"
# MAGIC 
# MAGIC ## Explore actions
# MAGIC * Type into the "Search actions" box to find actions to manipulate your data
# MAGIC * Try
# MAGIC     * Changing column data types
# MAGIC     * Cleaning up column names
# MAGIC     * Replacing values in a column
# MAGIC     * One-hot encoding a column
# MAGIC     * Extracting the year from datetime columns
# MAGIC 
# MAGIC ## Exploration
# MAGIC * Click on the "Explore DataFrame" button to profile your data
# MAGIC * Use "Predictor patterns" to explore predictive relationships between features (columns)
# MAGIC * Use the "Correlation Matrix" to identify target leakage and unnecessary features

# COMMAND ----------

bam
