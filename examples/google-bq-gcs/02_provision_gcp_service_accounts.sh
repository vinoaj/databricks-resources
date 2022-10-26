#!/bin/bash
source config.sh

gcloud config set project $GCP_PROJECT_QUERYING

gcloud iam service-accounts create $SA_NAME

# TODO: IAM condition examples
# - Expiry date request.time < timestamp("2021-01-01T00:00:00Z")
# - resource.type == "storage.googleapis.com/Bucket" && resource.name.startsWith("projects/_/buckets/exampleco-site-assets-")

gcloud projects add-iam-policy-binding $GCP_PROJECT_QUERYING \
  --role bigquery.readSessionUser \
  --role roles/bigquery.jobUser \
  --role roles/bigquery.dataEditor \
  --member="serviceAccount:$SA"

gcloud projects add-iam-policy-binding $GCP_PROJECT_DATASOURCE \
  --role roles/bigquery.user \
  --role roles/bigquery.jobUser \
  --role roles/bigquery.dataEditor \  # Comment this out if writing to BigQuery is not required
  --member="serviceAccount:$SA"

gsutil iam ch \
  serviceAccount:$SA:objectAdmin,legacyBucketOwner,legacyObjectOwner \
  gs://$TMP_BUCKET_NAME
