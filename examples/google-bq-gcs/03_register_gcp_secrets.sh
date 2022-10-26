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

databricks secrets create-scope --scope $SECRET_SCOPE \
    --profile $DB_CLI_PROFILE

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
