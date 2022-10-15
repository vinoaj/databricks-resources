#!/bin/bash

# Constants
## Databricks-related
DB_CLI_PROFILE=DEFAULT
SECRET_SCOPE=cloud-credentials

## Google Cloud-related
CRED_FILES=credentials.json
SA_USER=vinny-vijeyakumaar-gcs-reader
SA_PROJECT=my-gcp-project
SA=$SA_USER@$SA_PROJECT.iam.gserviceaccount.com

PRIVATE_KEY_ID=$(cat $CRED_FILES | jq -r '.private_key_id')
PRIVATE_KEY=$(cat $CRED_FILES | jq -r '.private_key')

# BigQuery credential requirements
## Register base64 encoded JSON file
base64 $CRED_FILES > credentials.json.b64.txt

databricks secrets put \
    --scope $SECRET_SCOPE \
    --key $SA \
    --binary-file credentials.json.b64.txt \
    --profile $DB_CLI_PROFILE

# Google Cloud Storage credential requirements
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

# Cleanup
# rm $CRED_FILES credentials.json.b64.txt