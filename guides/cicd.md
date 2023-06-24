# CI/CD with Databricks

## Azure DevOps

- [Reference](https://learn.microsoft.com/en-us/azure/databricks/dev-tools/ci-cd/ci-cd-azure-devops)
- The Databricks API token can either be a personal access token or an Azure Active Directory (AD) token
  - It is recommended that you use PATs belonging to service principals instead of users
- Managing PATs for service principals ([reference](https://learn.microsoft.com/en-us/azure/databricks/administration-guide/users-groups/service-principals#--manage-personal-access-tokens-for-a-service-principal))
  - An admin can create an AD access token
  - Run the following `curl` command
  ```
  curl -X POST -H 'Content-Type: application/x-www-form-urlencoded' \
  https://login.microsoftonline.com/<tenant-id>/oauth2/v2.0/token \
  -d 'client_id=<client-id>' \
  -d 'grant_type=client_credentials' \
  -d 'scope=2ff814a6-3304-4ab8-85cb-cd0e6f879c1d%2F.default' \
  -d 'client_secret=<client-secret>'
  ```
  - Where
    - `tenant-id` is the ID of the Azure AD tenant
    - `client-id` is the ID of the service principal
    - `client-secret` is the secret of the service principal
  - Do not change the value of the `scope` parameter. It represents the programmatic ID for Azure Databricks (`2ff814a6-3304-4ab8-85cb-cd0e6f879c1d`) along with the default scope (`/.default`, URL-encoded as `%2f.default`).
- The Azure AD access token is in the `access_token` value within the output of the call.
- [Further information](https://learn.microsoft.com/en-us/azure/databricks/dev-tools/auth#--azure-service-principal-authentication)
- If the service principal [requires `allow-cluster-create` or `allow-instance-pool-create` entitlements](https://learn.microsoft.com/en-us/azure/databricks/administration-guide/users-groups/service-principals#manage-entitlements-for-a-service-principal), use the Service Principals API to grant those entitlements to them
