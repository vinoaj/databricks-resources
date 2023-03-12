# Databricks on Google Cloud

- [Databricks on Google Cloud Security Best Practices](https://databricks.com/blog/2022/06/13/databricks-on-google-cloud-security-best-practices.html)
- [(Unofficial) Implementation Best Practices Guide](https://github.com/bhavink/databricks/tree/master/gcpdb4u)

## Networking

- [Network sizing guide](https://docs.gcp.databricks.com/administration-guide/cloud-configurations/gcp/network-sizing.html)

## Integrations

- [MLOps on Databricks with Vertex AI on Google Cloud](https://www.databricks.com/blog/2022/08/12/mlops-on-databricks-with-vertex-ai-on-google-cloud.html)
- [Spark BigQuery Connector](https://github.com/GoogleCloudDataproc/spark-bigquery-connector)

## Security

### Storing Service Account Keys in Databricks Secrets

First `base64` encode the `json` key file

```shell
base64 credentials.json > credentials.json.b64.txt
```

Upload to Databricks secrets as a binary file

```shell
databricks secrets put \
    --scope gcp-keys \
    --key service-account-name@gcp-project.iam.gserviceaccount.com \
    --binary-file credentials.json.b64.txt \
    --profile config_profile_name # Optional if using multiple profiles
```
