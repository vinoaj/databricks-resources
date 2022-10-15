#!/bin/bash

# Constants
## Databricks-related
DB_CLI_PROFILE=DEFAULT
SECRET_SCOPE=cloud-credentials

## Azure-related
CRED_FILES=azurecreds.txt
ADLS_ACCOUNT=vinnyvijeyakumaaradls
ADLS_KEY=$(<$CRED_FILES)

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