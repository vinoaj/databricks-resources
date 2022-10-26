# Databricks notebook source
# MAGIC %md
# MAGIC # Working with Google BigQuery in Databricks
# MAGIC * This notebook provides examples of working with Google BigQuery from within a Databricks Workspace that sits in Azure or AWS

# COMMAND ----------

# MAGIC %md
# MAGIC ## Prerequisites (to be handled by Admin)
# MAGIC From your **Google Cloud** end you will need to:
# MAGIC - Have a service account with the relevant read & write permissions to the BigQuery projects/datasets/tables that you are interested in
# MAGIC - A dataset for temporary materialisation of results (only if you are passing SQL statements to BigQuery). This must reside in the querying project
# MAGIC - A Google Cloud Storage (GCS) bucket if you are writing to BigQuery
# MAGIC 
# MAGIC These tasks should **NOT** be the concern of the analyst; and instead should be performed as a once-off exercise by the relevant admins. [Refer to this Notebook](gcp_authentication_setup.py) for the admin's workflows to provision the relevant service accounts, set their IAM credentials, and apply them to a cluster

# COMMAND ----------

# MAGIC %md
# MAGIC ## Access Patterns (to be handled by Admin)
# MAGIC 
# MAGIC - As per Google Cloud security best practices, access to GCP resources should be handled via a service account
# MAGIC - The service account can be utilised (a) at the cluster level or (b) in Notebook/Job code
# MAGIC 
# MAGIC ### Cluster Authentication (Recommended)
# MAGIC [Refer to this Notebook](gcp_authentication_setup.py) for workflows to provision the relevant service accounts, set their IAM credentials, and apply them to a cluster
# MAGIC 
# MAGIC Attach a Google Service Account to your cluster to manage authentication with BigQuery
# MAGIC * **In Google Cloud**: If your Databricks Workspace is in Google Cloud, it is recommended that access to BigQuery is managed via a Service Account that is attached to your notebook or workflow (job) cluster. Follow [this tutorial](https://cloud.google.com/bigquery/docs/connect-databricks) for instructions
# MAGIC * **From Azure or AWS**: If your Workspace is in Azure or AWS, add credential information to the accessing cluster's Spark Config. Utilise [these instructions](https://docs.databricks.com/data/data-sources/google/bigquery.html#step-2-set-up-databricks) (also applies to Azure)
# MAGIC 
# MAGIC ### Non-Cluster Authentication
# MAGIC We **will not** cover this scenario in these notebooks, as it is not a recommended approach with respect to hardening security. However, we are presenting the steps for completeness of documentation
# MAGIC 
# MAGIC In cases where you wish to use the user's credentials, the process is
# MAGIC - Generate JSON key
# MAGIC - Store key values in Databricks Secrets
# MAGIC - Use `spark.conf.set()` to set the appropriate permissions

# COMMAND ----------

# MAGIC %md
# MAGIC ## Reading from (Querying) Google BigQuery
# MAGIC * The Spark BigQuery connector leverages BigQuery's Storage Read API for reading & writing data
# MAGIC * The BigQuery Storage Read API is the most performant option for reading table data using column filters
# MAGIC   * Limitations: because it reads directly from BigQuery storage, there is no ability to join tables or perform aggregations, windowing functions, etc
# MAGIC   

# COMMAND ----------

# MAGIC %md
# MAGIC ### Using the BigQuery Storage Read API

# COMMAND ----------

# If the below has not been configured on the cluster or needs to be overwritten, the configuration values
#   can be set using spark.conf.set()

# Parent (or querying) project
# spark.conf.set("parentProject", "vinoaj-querying-source")
# spark.conf.set("viewsEnabled", "true")

# For BigQuery WRITE
# spark.conf.set("temporaryGcsBucket", "vv_databricks_tmp_000")
# spark.conf.set("materializationProject", "vinoaj-querying-source")
# spark.conf.set("materializationDataset", "temp_us")

# COMMAND ----------

# MAGIC %md
# MAGIC Example: read in the entire contents of a table

# COMMAND ----------

table = "bigquery-public-data.iowa_liquor_sales.sales"
df = spark.read.format("bigquery").load(table)
display(df)
df.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC Example: selectively retrieve table data

# COMMAND ----------

table = "bigquery-public-data.iowa_liquor_sales.sales"
df = spark.read.format("bigquery").load(table)

# Spark DataFrames are lazily evaluated. Therefore, at this point, no call has yet been made to BigQuery

# Let's start limiting the data we want to read from BigQuery. Not only will it speed up response times, but it will
#   also minimise BigQuery API costs.
df = df.select('store_number', 'store_name', 'zip_code')

# When filtering, filters that are allowed will be automatically pushed down.
# Those that are not will be computed client side (i.e. on a Databricks cluster)
df = df.where("zip_code IS NOT NULL AND store_name LIKE '%Hy-Vee%'")

# display(df), df.show(), df.collect(), etc. are Spark action operations that will trigger query execution.
# It is at this point that BigQuery will be executed and return a response.
display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC #### Working with SQL on DataFrames
# MAGIC The beauty of Databricks Notebooks is that we can switch between PySpark and SQL in the same Notebook!
# MAGIC 
# MAGIC Work with the data using SQL
# MAGIC - Register the DataFrame as a temporary view
# MAGIC - Run your SQL statements against the view

# COMMAND ----------

df.createOrReplaceTempView("filtered_stores")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM filtered_stores
# MAGIC WHERE store_number > 2600
# MAGIC ORDER BY store_number, store_name

# COMMAND ----------

# MAGIC %md
# MAGIC #### Working with SQL on DataFrames (another example)

# COMMAND ----------

df_sales_2020 = spark.read.format("bigquery").load("bigquery-public-data.iowa_liquor_sales_forecasting.2020_sales_train")
df_sales_2021 = spark.read.format("bigquery").load("bigquery-public-data.iowa_liquor_sales_forecasting.2021_sales_predict")

df_sales_2020.createOrReplaceTempView("tvw_sales_2020")
df_sales_2021.createOrReplaceTempView("tvw_sales_2021")

# COMMAND ----------

# MAGIC %sql
# MAGIC WITH all_sales AS (
# MAGIC   SELECT *
# MAGIC   FROM tvw_sales_2020
# MAGIC 
# MAGIC   UNION
# MAGIC 
# MAGIC   SELECT *
# MAGIC   FROM tvw_sales_2021
# MAGIC )
# MAGIC SELECT *
# MAGIC FROM all_sales
# MAGIC WHERE city IN ("Ames", "Ankeny")

# COMMAND ----------

# MAGIC %md
# MAGIC ### Using SQL Queries
# MAGIC * You can also query BigQuery using SQL queries
# MAGIC * In order to retreive the results of the query, the results first have to be materialised in a temp table on BigQuery
# MAGIC * You need to specifiy a BigQuery dataset that you have write access to. This table has to be in the querying project.
# MAGIC * Add the service account to the dataset and give it the role `BigQuery Data Editor`

# COMMAND ----------

sql = """
  SELECT tag, COUNT(*) c
  FROM (
    SELECT SPLIT(tags, '|') tags
    FROM `bigquery-public-data.stackoverflow.posts_questions` a
    WHERE EXTRACT(YEAR FROM creation_date)>=2014
  ), UNNEST(tags) tag
  GROUP BY 1
  ORDER BY 2 DESC
  LIMIT 10
  """

df = (spark.read.format("bigquery")
        .option("materializationProject", "vinoaj-querying-source")
        .option("materializationDataset", "temp_us")
        .option("query", sql)
      .load())

display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Using External Tables
# MAGIC - You can declare unmanaged external tables in Databricks that will read data directly from BigQuery
# MAGIC - The creation of the external tables only needs to be done once, and it will be accessible to those with the relevant permissions

# COMMAND ----------

# MAGIC %sql
# MAGIC -- DROP TABLE vinny_vijeyakumaar.test_table;
# MAGIC 
# MAGIC -- This is a one-time operation
# MAGIC CREATE TABLE vinny_vijeyakumaar.test_table
# MAGIC USING bigquery
# MAGIC OPTIONS (table "bigquery-public-data.stackoverflow.posts_questions");

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM vinny_vijeyakumaar.test_table
# MAGIC LIMIT 10;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Writing to BigQuery
# MAGIC - In order to write to BigQuery, the connector requires write access to a GCS bucket
# MAGIC - The data held in the DataFrame is written out as Parquet files to the bucket; where it is then subsequently loaded into BigQuery

# COMMAND ----------

# _sqldf is a global variable that holds the results of the last executed SQL statement
df = _sqldf

(df.write.format("bigquery")
   .mode("append")
   # .option("temporaryGcsBucket", "vv_databricks_tmp_000")
   # Table we'll be writing to
   .option("table", "vinoaj-querying-source.test_dataset.tmp_stackoverflow")
   .save())

# COMMAND ----------

# Read from the table we just wrote to
display(spark.read.format("bigquery").load("vinoaj-querying-source.test_dataset.tmp_stackoverflow"))

# COMMAND ----------

# MAGIC %md
# MAGIC ## Best Practices
# MAGIC 
# MAGIC ### Minimising BigQuery costs
# MAGIC If you are constantly reading and manipulating data from the same BigQuery tables, this can incur unnecessary costs on BigQuery's end and introduce latency. Instead, you can take the following approaches to minimise the number of calls to BigQuery.
# MAGIC 
# MAGIC **If working with DataFrames: Use `df.cache()`**
# MAGIC 
# MAGIC [Reference](https://kb.databricks.com/en_US/scala/best-practice-cache-count-take)
# MAGIC 
# MAGIC `cache()` caches the specified DataFrame in the memory of your cluster’s workers. 
# MAGIC 
# MAGIC Let's compare 2 scenarios.
# MAGIC 
# MAGIC - In **Scenario 1** we load a table into a DataFrame and generate two different pieces of analysis around it 
# MAGIC - Because DataFrames are lazily evaluated, when `df2` and `df3` are activated, it triggers the re-computation of all DataFrames that they refer to
# MAGIC ```
# MAGIC df = spark.read.format("bigquery").load("bigquery-public-data.stackoverflow.posts_questions")
# MAGIC df2 = df.select("id", "title", "parent_id").filter("id > 69000000")
# MAGIC df3 = df2.filter("title LIKE '%SQL%'")
# MAGIC 
# MAGIC # Running the below statements will result in 3 separate calls to BigQuery
# MAGIC print(df.count())
# MAGIC print(df2.count())
# MAGIC print(df3.count())
# MAGIC ```
# MAGIC &nbsp;
# MAGIC 
# MAGIC - In **Scenario 2** we use `cache()` to cache the data on the cluster
# MAGIC - Therefore, subsequent references to `df` will read from the cache rather than forcing a re-compute
# MAGIC - This is a temporary cache, and will be lost once the cluster stops
# MAGIC ```
# MAGIC df = spark.read.format("bigquery").load("bigquery-public-data.stackoverflow.posts_questions")
# MAGIC df.cache()
# MAGIC 
# MAGIC df2 = df.select("id", "title", "parent_id").filter("id > 69000000")
# MAGIC df3 = df2.filter("title LIKE '%SQL%'")
# MAGIC df4 = df.filter("title LIKE '%SQL%'")
# MAGIC 
# MAGIC # Running the below statements will only result in 1 call to BigQuery
# MAGIC print(df.count())
# MAGIC print(df2.count())
# MAGIC print(df3.count())
# MAGIC print(df4.count())
# MAGIC ```
# MAGIC &nbsp;
# MAGIC 
# MAGIC **If working with SQL: Temporarily Persist Data in Delta Tables**
# MAGIC 
# MAGIC The above strategy is best suited for those familiar with working with Python DataFrames (e.g. through `pandas` or `pyspark`). If you prefer working with SQL, persist the data as a Delta Table in your Databricks environment, and work with that.
# MAGIC 
# MAGIC Once you are done with the data, drop the tables
# MAGIC 
# MAGIC ```
# MAGIC %python
# MAGIC df = spark.read.format("bigquery").load("bigquery-public-data.stackoverflow.posts_questions")
# MAGIC 
# MAGIC # Write table
# MAGIC df.write.mode("overwrite").saveAsTable("temp.so_post_questions")
# MAGIC 
# MAGIC %sql
# MAGIC -- Start querying in SQL (or switch to the SQL UI)
# MAGIC SELECT *
# MAGIC FROM temp.so_post_questions
# MAGIC WHERE title LIKE '%SQL';
# MAGIC 
# MAGIC %sql
# MAGIC -- Once you are done with your work
# MAGIC DROP TABLE temp.so_post_questions;
# MAGIC ```
