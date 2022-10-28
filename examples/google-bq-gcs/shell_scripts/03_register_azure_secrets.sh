#!/bin/bash
source config.sh

databricks secrets put \
    --scope $SECRET_SCOPE \
    --key adls-$ADLS_ACCOUNT-key \
    --string-value $ADLS_KEY \
    --profile $DB_CLI_PROFILE

# Verify
databricks secrets list \
    --scope $SECRET_SCOPE \
    --output JSON \
    --profile $DB_CLI_PROFILE

# Cleanup
# rm $CRED_FILES