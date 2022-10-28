#!/bin/bash

# Load config parameters
source config.sh

gcloud storage buckets create gs://$TMP_BUCKET_NAME \
  --project=$GCP_PROJECT_QUERYING \
  --default-storage-class=$DEFAULT_STORAGE_CLASS \
  --location=$LOCATION \
  --public-access-prevention
