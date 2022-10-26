# Working with Google BigQuery & Google Cloud Storage

## ⚠️ Caution!
- **DO NOT** upload your service account credential files to `DBFS` or your `git` repo. Instead, utilise [Databricks Secrets](https://docs.databricks.com/security/secrets/index.html#secrets-user-guide) and your git providers secret management facilities

## TL;DR
### Rendered Notebooks
- [Examples of Working with BigQuery](https://vinoaj.github.io/databricks-resources/examples/google-bq-gcs/rendered_notebooks/working_with_bigquery.html)
- [Authentication set up](https://vinoaj.github.io/databricks-resources/examples/google-bq-gcs/rendered_notebooks/gcp_authentication_setup.html)

### Notebooks
- [working_with_bigquery.py](working_with_bigquery.py)
- [gcp_authentication_setup.py](gcp_authentication_setup.py)


## Pre-requisites
- Databricks CLI installed on your local environment
    - Databricks CLI authenticated with your target Databricks Workspace

## Setup
### Steps
**Steps**
1. Identify
  * Google Cloud project that will be the **querying** project. This is the project that will be billed for the queries run against BigQuery
  * Google Cloud project that will be the **data source**. This is the project that houses the BigQuery datasets / tables to be queried
  * (If requiring WRITEs to BQ): Identify a Google Cloud Storage (GCS) bucket to hold temporary Parquet files before loading them into BigQuery 
2. (If requiring WRITEs to BQ): Provision a GCS bucket to hold temporary Parquet files before loading them into BigQuery ([sample code](01_create_gcs_bucket.sh))
3. Google Cloud service account ([sample code](02_provision_gcp_service_account.sh))
  * Create service account in querying project
  * Provide service account with appropriate permissions to querying project
  * Provide service account with appropriate permissions to BQ project
  * (If requiring WRITEs to BQ): Provide service account with appropriate permissions to temporary storage bucket
4. Register service account credentials with Databricks Secrets ([sample code](03_register_gcp_secrets.sh))
5. Configure clusters

### Cluster Configuration
- Let's assume our service account name is `databricks-reader@vinoaj-querying-source.iam.gserviceaccount.com`
- If you have followed the above code examples, your secrets will be in Databricks Secrets with:
  - Scope: `cloud-credentials`
  - Key: `databricks-reader@vinoaj-querying-source.iam.gserviceaccount.com*`
- Add the following configuration to the cluster's Spark config settings
```
# For BQ READ-ONLY
credentials {{secrets/cloud-credentials/databricks-reader@vinoaj-querying-source.iam.gserviceaccount.com}}

# Include the below only if you require BQ WRITE and/or GCS READ+WRITE
spark.hadoop.google.cloud.auth.service.account.enable true
spark.hadoop.fs.gs.auth.service.account.email databricks-reader@vinoaj-querying-source.iam.gserviceaccount.com
spark.hadoop.fs.gs.project.id vinoaj-querying-source
spark.hadoop.fs.gs.auth.service.account.private.key {{secrets/cloud-credentials/databricks-reader@vinoaj-querying-source.iam.gserviceaccount.com-private-key}}
spark.hadoop.fs.gs.auth.service.account.private.key.id {{secrets/cloud-credentials/databricks-reader@vinoaj-querying-source.iam.gserviceaccount.com-private-key-id}}
```

## TODO
- Terraform examples
