# Architecture

## Workspace Topology

- [ ] How are your Workspaces going to be separated? By environment (e.g. dev, UAT, Prod), by business unit (e.g. Finance, HR), or a combination?

## Security

- [ ] Use of service principals / roles?

## Cluster Management

A cluster policy limits the ability to configure clusters based on a set of rules. The policy rules limit the attributes or attribute values available for cluster creation. Cluster policies have ACLs that limit their use to specific users and groups. Therefore you can control who can or cannot create clusters, and the limits to which they can configure those clusters.

- [ ] What cluster policies do you require?
  - [ ] Which groups / users are assigned to which cluster policies?
- [ ] Are cluster policies adhering to best practices ([General guidance](https://www.databricks.com/blog/2022/10/18/best-practices-cost-management-databricks.html) | [AWS](https://docs.databricks.com/administration-guide/clusters/policies-best-practices.html) | [Azure](https://learn.microsoft.com/en-gb/azure/databricks/administration-guide/clusters/policies-best-practices) | [GCP](https://docs.gcp.databricks.com/administration-guide/clusters/policies-best-practices.html))
  - [ ] Node count limits & auto-scaling
  - [ ] Auto-termination minutes
  - [ ] Only allow latest DBRs
  - [ ] Restrict node types for driver & workers
  - [ ] Enforce Spot on workers
  - [ ] Enforce Photon for jobs
  - [ ] Tags enforced for cost attribution
  - [ ] Set DBUs per hour restriction on interactive clusters

## Logging

Place delivery bucket location outside of the projects/resource groups holding your workspaces. This way you will be able to:

- Retain the logs if the project/resource group/account is accidentally deleted or locked off
- Consolidate all logs in a single location for easy cross-workspace analysis

- [ ] Create delivery bucket for **Audit** logs
- [ ] Create delivery bucket for **Billing** logs

### Audit Logs

These logs outline workspace- and account-level events, including when jobs and clusters are triggered.

- [ ] Configure audit log exports: [AWS](https://docs.databricks.com/administration-guide/account-settings/audit-logs.html)([sample analysis](https://docs.databricks.com/administration-guide/account-settings/audit-logs.html#analyze-audit-logs)) | [Azure](https://docs.microsoft.com/en-us/azure/databricks/administration-guide/account-settings/azure-diagnostic-logs)([sample analysis](https://docs.microsoft.com/en-us/azure/databricks/administration-guide/account-settings/azure-diagnostic-logs#analyze-diagnostic-logs)) | [Google Cloud](https://docs.gcp.databricks.com/administration-guide/account-settings-gcp/log-delivery.html)([sample analysis](https://docs.gcp.databricks.com/administration-guide/account-settings-gcp/audit-logs.html#analyze-audit-logs))
- [ ] Build out per-workspace and cross-workspace dashboards
- [ ] Set alerts

### Billing Logs

Note: automated export of this is only available on AWS

- [ ] **AWS**: Configure export of billing logs on [AWS](https://docs.databricks.com/administration-guide/account-settings/billable-usage-delivery.html)
- [ ] **Azure**: view costs through the subscription billing console

#### Google Cloud options

- [ ] Option 1: [View billable usage](https://docs.gcp.databricks.com/administration-guide/account-settings-gcp/usage.html) in the Databricks account console. You also have the option to manually download a CSV file
- [ ] Option 2: View data in the GCP billing console (you will need Google Cloud's `roles/billing.viewer` IAM role)
- [ ] Option 3: Path to automation: GCP billing data can be [exported to BigQuery](https://cloud.google.com/billing/docs/how-to/export-data-bigquery). This is usually set up as a matter of best practice when building out an enterprise's Google Cloud architecture, so you may already have a BigQuery dataset containing all your enterprise's billing usage data
  - Ask the BQ dataset admin to create a view on top of that data that limits it to the projects housing Databricks workspaces (e.g. filter by project names)
  - You can then utilise that view to keep a track of consumption of all resources associated with your workspace

### Log Analytics

- [ ] Create billing dashboard
- [ ] Create resource utilisation dashboard

## Storage

- [ ] Configure storage life cycles on your blob storage. Align it with your `VACUUM` policies (determines time travel lookback window)

## Networking

- [ ] Minimise egress costs by colocating Workspace and storage buckets
  - [ ] AWS: utilise VPC endpoints
  - [ ] Azure: utilise Private Link or Service Endpoints
  - [ ] GCP: Private Google Access

## Cost Optimisations

- [ ] Create & enforce cluster policies (see above for recommendations)
- [ ] Set budgets using the [Budget API](https://docs.databricks.com/dev-tools/api/latest/account.html#operation/create-budget) (private preview)