variable "secret_scope_name" {
    description = "Name of Databricks Secret Scope"
    type = string
    default = "cloud-credentials"
}

variable "gcp_project_querying" {
  description = "The GCP project that will be billed for BigQuery queries"
  type        = string
  default     = "vinoaj-querying-source"
}

variable "gcp_project_datasources" {
  description = "The GCP projects housing the BigQuery datasets that will be read"
  type        = list(string)
  default     = ["vinoaj-bq-datasets"]
}

variable "sa_expiry_offset_days" {
  description = "Number of days before service account's access to datasource project expires"
  type        = number
  default     = 90
}

variable "service_account_name" {
  description = "Name of the service account to attach to the clusters"
  type        = string
  default     = "databricks-reader"
}

variable "service_account_roles_datasource_project" {
  description = "Service Account's roles in the datasource project"
  type        = list(string)
  default = [
    "roles/bigquery.user",
    "roles/bigquery.jobUser",
    # Include if writing to the datasource(s) is allowed
    # "roles/bigquery.dataEditor"
  ]
}

variable "tmp_gcs_bucket_name" {
  description = "For BQ writes: GCS bucket that will stage data before loading into BigQuery"
  type        = string
  default     = "vv_databricks_tmp_00"
}

variable "tmp_gcs_bucket_location" {
  description = "Which region the bucket is in"
  type        = string
  default     = "US"
}

variable "bq_materialization_dataset" {
    description = "Name of BQ dataset for temporary materialisation of SQL queries"
    type = string
    default = "temp_databricks"
}

variable "workspace_url" {
    type = string
    default = "https://abcdef.cloud.databricks.com/"
}
