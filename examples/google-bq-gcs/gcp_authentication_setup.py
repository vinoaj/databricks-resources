# Databricks notebook source
# MAGIC %md
# MAGIC # GCP Authentication Setup
# MAGIC This Notebook outlines the steps required to configure your clusters

# COMMAND ----------

# MAGIC %md
# MAGIC **Steps**
# MAGIC 
# MAGIC 1. Identify
# MAGIC   * Google Cloud project that will be the **querying** project. This is the project that will be billed for the queries run against BigQuery
# MAGIC   * Google Cloud project that will be the **data source**. This is the project that houses the BigQuery datasets / tables to be queried
# MAGIC   * (If requiring WRITEs to BQ): Identify a Google Cloud Storage (GCS) bucket to hold temporary Parquet files before loading them into BigQuery 
# MAGIC 2. (If requiring WRITEs to BQ): Provision a GCS bucket to hold temporary Parquet files before loading them into BigQuery ([sample code](01_create_gcs_bucket.sh))
# MAGIC 3. Google Cloud service account ([sample code](02_provision_gcp_service_account.sh))
# MAGIC   * Create service account in querying project
# MAGIC   * Provide service account with appropriate permissions to querying project
# MAGIC   * Provide service account with appropriate permissions to BQ project
# MAGIC   * (If requiring WRITEs to BQ): Provide service account with appropriate permissions to temporary storage bucket
# MAGIC 4. Register service account credentials with Databricks Secrets ([sample code](03_register_gcp_secrets.sh))
# MAGIC 5. Configure clusters

# COMMAND ----------

# MAGIC %md
# MAGIC ## Cluster configuration
# MAGIC 
# MAGIC - Let's assume our service account name is `databricks-reader@vinoaj-querying-source.iam.gserviceaccount.com`
# MAGIC - If you have followed the above code examples, your secrets will be in Databricks Secrets with:
# MAGIC   - Scope: `cloud-credentials`
# MAGIC   - Key: `databricks-reader@vinoaj-querying-source.iam.gserviceaccount.com*`
# MAGIC - Add the following configuration to the cluster's Spark config settings
# MAGIC ```
# MAGIC # For BQ READ-ONLY
# MAGIC credentials {{secrets/cloud-credentials/databricks-reader@vinoaj-querying-source.iam.gserviceaccount.com}}
# MAGIC parentProject vinoaj-querying-source
# MAGIC viewsEnabled true
# MAGIC 
# MAGIC # Include the below only if you require BQ WRITE and/or GCS READ+WRITE
# MAGIC spark.hadoop.google.cloud.auth.service.account.enable true
# MAGIC spark.hadoop.fs.gs.auth.service.account.email databricks-reader@vinoaj-querying-source.iam.gserviceaccount.com
# MAGIC spark.hadoop.fs.gs.project.id vinoaj-querying-source
# MAGIC spark.hadoop.fs.gs.auth.service.account.private.key {{secrets/cloud-credentials/databricks-reader@vinoaj-querying-source.iam.gserviceaccount.com-private-key}}
# MAGIC spark.hadoop.fs.gs.auth.service.account.private.key.id {{secrets/cloud-credentials/databricks-reader@vinoaj-querying-source.iam.gserviceaccount.com-private-key-id}}
# MAGIC temporaryGcsBucket vv_databricks_tmp_000
# MAGIC materializationProject vinoaj-querying-source
# MAGIC materializationDataset temp_us
# MAGIC ```
