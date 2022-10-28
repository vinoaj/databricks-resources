#!/bin/bash
include config.sh

## Google Cloud-related
CRED_FILES=credentials.json

gcloud config set project $GCP_PROJECT_QUERYING

# DO NOT persist this file in DBFS or your Git repo
gcloud iam service-accounts keys create --iam-account \
  "$SA" $CRED_FILES

PRIVATE_KEY_ID=$(cat $CRED_FILES | jq -r '.private_key_id')
PRIVATE_KEY=$(cat $CRED_FILES | jq -r '.private_key')


# BigQuery credential requirements
## Register base64 encoded JSON file
base64 $CRED_FILES > credentials.json.b64.txt

## Create Databricks Secret scope
databricks secrets create-scope --scope $SECRET_SCOPE \
    --profile $DB_CLI_PROFILE

# Initially the user who runs this command has MANAGE permissions for this scope
# Let's add some restrictions:
#   - We'll assume you already have 2 groups in Databricks: "sec-admin" and "cluster-admin"
#   - Members of the sec-admin group can MANAGE this scope
#   - Members of the cluster-admin group can READ this scope
#       - Note: they cannot read the CONTENTS of the secret; they are just able to access it
#       - With READ access, cluster admins can include the secrets in cluster configurations
#   - Members outside these groups can NOT READ from or WRITE to this scope

databricks secrets put-acl \
    --scope $SECRET_SCOPE \
    --principal sec-admin \ 
    --permission MANAGE

databricks secrets put-acl \
    --scope $SECRET_SCOPE \
    --principal cluster-admin \ 
    --permission READ


databricks secrets put \
    --scope $SECRET_SCOPE \
    --key $SA \
    --binary-file credentials.json.b64.txt \
    --profile $DB_CLI_PROFILE

## Delete credential files
rm -f $CRED_FILES credentials.json.b64.txt


# Google Cloud Storage (GCS) credential requirements
## Project ID
databricks secrets put \
    --scope $SECRET_SCOPE \
    --key $SA-project \
    --string-value $SA_PROJECT \
    --profile $DB_CLI_PROFILE

## Key ID
databricks secrets put \
    --scope $SECRET_SCOPE \
    --key $SA-private-key-id \
    --string-value $PRIVATE_KEY_ID \
    --profile $DB_CLI_PROFILE

## Key
databricks secrets put \
    --scope $SECRET_SCOPE \
    --key $SA-private-key \
    --string-value "$PRIVATE_KEY" \
    --profile $DB_CLI_PROFILE


# Verify
databricks secrets list \
    --scope $SECRET_SCOPE \
    --output JSON \
    --profile $DB_CLI_PROFILE
