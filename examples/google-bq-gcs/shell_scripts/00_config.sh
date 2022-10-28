#!/bin/bash

# DATABRICKS
## Which Databricks CLI connection profile to use
DB_CLI_PROFILE=DEFAULT
## Databricks Secrets scope to store cloud credentials
SECRET_SCOPE=cloud-secrets

# AZURE
ADLS_ACCOUNT=vinnyvijeyakumaaradls
AZURE_CRED_FILES=azurecreds.txt
ADLS_KEY=$(<$CRED_FILES)

# GOOGLE CLOUD
## Project that will be issuing BigQuery queries and be billed for the queries
GCP_PROJECT_QUERYING=vinoaj-querying-source
## Project housing the relevant BigQuery datasets
GCP_PROJECT_DATASOURCE=vinoaj-bq-datasets
## Service account name
SA_NAME=databricks-reader
SA=$SA_NAME@$GCP_PROJECT_QUERYING.iam.gserviceaccount.com
echo "Service Account: $SA"

## Bucket to hold temporary Parquet files before loading into BigQuery
BUCKET_NAME=vv_databricks_tmp_000
## https://cloud.google.com/storage/docs/storage-classes
DEFAULT_STORAGE_CLASS=STANDARD
## https://cloud.google.com/storage/docs/locations
LOCATION=US

