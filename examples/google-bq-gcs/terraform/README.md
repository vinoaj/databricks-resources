## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_databricks"></a> [databricks](#requirement\_databricks) | ~>1.6.1 |
| <a name="requirement_google"></a> [google](#requirement\_google) | ~>4.41.0 |
| <a name="requirement_time"></a> [time](#requirement\_time) | ~>0.9.0 |

## Providers

| Name | Version |
|------|---------|
| <a name="provider_databricks"></a> [databricks](#provider\_databricks) | 1.6.1 |
| <a name="provider_google"></a> [google](#provider\_google) | 4.41.0 |
| <a name="provider_time"></a> [time](#provider\_time) | 0.9.0 |

## Modules

No modules.

## Resources

| Name | Type |
|------|------|
| [databricks_cluster.bq_readonly](https://registry.terraform.io/providers/databricks/databricks/latest/docs/resources/cluster) | resource |
| [databricks_cluster.bq_readwrite](https://registry.terraform.io/providers/databricks/databricks/latest/docs/resources/cluster) | resource |
| [databricks_group.cluster_creator](https://registry.terraform.io/providers/databricks/databricks/latest/docs/resources/group) | resource |
| [databricks_group.sec_admin](https://registry.terraform.io/providers/databricks/databricks/latest/docs/resources/group) | resource |
| [databricks_group_member.me](https://registry.terraform.io/providers/databricks/databricks/latest/docs/resources/group_member) | resource |
| [databricks_secret.credentials](https://registry.terraform.io/providers/databricks/databricks/latest/docs/resources/secret) | resource |
| [databricks_secret.private_key](https://registry.terraform.io/providers/databricks/databricks/latest/docs/resources/secret) | resource |
| [databricks_secret.private_key_id](https://registry.terraform.io/providers/databricks/databricks/latest/docs/resources/secret) | resource |
| [databricks_secret_acl.cluster_creator_read](https://registry.terraform.io/providers/databricks/databricks/latest/docs/resources/secret_acl) | resource |
| [databricks_secret_acl.sec_admin_manage](https://registry.terraform.io/providers/databricks/databricks/latest/docs/resources/secret_acl) | resource |
| [databricks_secret_scope.cloud_secrets_scope](https://registry.terraform.io/providers/databricks/databricks/latest/docs/resources/secret_scope) | resource |
| [google_bigquery_dataset.materialization_dataset](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/bigquery_dataset) | resource |
| [google_project_iam_binding.datasource_projects](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/project_iam_binding) | resource |
| [google_project_iam_binding.querying_project](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/project_iam_binding) | resource |
| [google_service_account.sa](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/service_account) | resource |
| [google_service_account_key.sa_key](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/service_account_key) | resource |
| [google_storage_bucket.tmp_storage_bucket](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket) | resource |
| [google_storage_bucket_iam_binding.tmp_bucket](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket_iam_binding) | resource |
| [time_offset.expiry_period](https://registry.terraform.io/providers/hashicorp/time/latest/docs/resources/offset) | resource |
| [databricks_current_user.me](https://registry.terraform.io/providers/databricks/databricks/latest/docs/data-sources/current_user) | data source |
| [databricks_node_type.smallest](https://registry.terraform.io/providers/databricks/databricks/latest/docs/data-sources/node_type) | data source |
| [databricks_spark_version.latest_lts](https://registry.terraform.io/providers/databricks/databricks/latest/docs/data-sources/spark_version) | data source |
| [google_client_config.current](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/client_config) | data source |
| [google_client_openid_userinfo.me](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/client_openid_userinfo) | data source |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_bq_materialization_dataset"></a> [bq\_materialization\_dataset](#input\_bq\_materialization\_dataset) | Name of BQ dataset for temporary materialisation of SQL queries | `string` | `"temp_databricks"` | no |
| <a name="input_databricks_profile"></a> [databricks\_profile](#input\_databricks\_profile) | Databricks CLI profile to use to authenticate Terraform with your Databricks Workspace | `string` | `"DEFAULT"` | no |
| <a name="input_gcp_project_datasources"></a> [gcp\_project\_datasources](#input\_gcp\_project\_datasources) | The GCP projects housing the BigQuery datasets that will be read | `list(string)` | <pre>[<br>  "vinoaj-bq-datasets"<br>]</pre> | no |
| <a name="input_gcp_project_querying"></a> [gcp\_project\_querying](#input\_gcp\_project\_querying) | The GCP project that will be billed for BigQuery queries | `string` | `"vinoaj-querying-source"` | no |
| <a name="input_gcp_project_querying_location"></a> [gcp\_project\_querying\_location](#input\_gcp\_project\_querying\_location) | Default location for resources in querying project | `string` | `"US"` | no |
| <a name="input_sa_expiry_offset_days"></a> [sa\_expiry\_offset\_days](#input\_sa\_expiry\_offset\_days) | Number of days before service account's access to datasource project(s) expires | `number` | `90` | no |
| <a name="input_secret_scope_name"></a> [secret\_scope\_name](#input\_secret\_scope\_name) | Name of Databricks Secret Scope | `string` | `"cloud-credentials"` | no |
| <a name="input_service_account_name"></a> [service\_account\_name](#input\_service\_account\_name) | Name of the GCP service account to attach to the clusters | `string` | `"databricks-reader"` | no |
| <a name="input_service_account_roles_datasource_project"></a> [service\_account\_roles\_datasource\_project](#input\_service\_account\_roles\_datasource\_project) | Service Account's roles in the datasource project(s) | `list(string)` | <pre>[<br>  "roles/bigquery.user",<br>  "roles/bigquery.jobUser"<br>]</pre> | no |
| <a name="input_tmp_gcs_bucket_location"></a> [tmp\_gcs\_bucket\_location](#input\_tmp\_gcs\_bucket\_location) | Which region the temp bucket is in | `string` | `"US"` | no |
| <a name="input_tmp_gcs_bucket_name"></a> [tmp\_gcs\_bucket\_name](#input\_tmp\_gcs\_bucket\_name) | For BQ writes: GCS bucket that will stage data before loading into BigQuery | `string` | `"vv_databricks_tmp_00"` | no |
| <a name="input_workspace_url"></a> [workspace\_url](#input\_workspace\_url) | n/a | `string` | `"https://abcdef.cloud.databricks.com/"` | no |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_cluster_read_only"></a> [cluster\_read\_only](#output\_cluster\_read\_only) | n/a |
| <a name="output_cluster_read_write"></a> [cluster\_read\_write](#output\_cluster\_read\_write) | n/a |
| <a name="output_databricks_user"></a> [databricks\_user](#output\_databricks\_user) | n/a |
| <a name="output_google_user"></a> [google\_user](#output\_google\_user) | n/a |
