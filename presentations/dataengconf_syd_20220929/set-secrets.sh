#!/bin/sh
# Store your Kaggle credentials in Databricks Secrets

# Constants
## Databricks-related
DB_CLI_PROFILE=profile-name
SECRET_SCOPE=vinny-vijeyakumaar

KEY_FILE=kaggle.json
KAGGLE_USERNAME=$(cat $KEY_FILE | jq -r '.username')
KAGGLE_KEY=$(cat $KEY_FILE | jq -r '.key')

databricks secrets put \
    --scope $SECRET_SCOPE \
    --key KAGGLE_USERNAME \
    --string-value $KAGGLE_USERNAME \
    --profile $DB_CLI_PROFILE

databricks secrets put \
    --scope $SECRET_SCOPE \
    --key KAGGLE_KEY \
    --string-value $KAGGLE_KEY \
    --profile $DB_CLI_PROFILE
