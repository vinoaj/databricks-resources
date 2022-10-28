resource "google_bigquery_dataset" "materialization_dataset" {
  project       = var.gcp_project_querying
  dataset_id    = var.bq_materialization_dataset
  friendly_name = "Temp Materialization"
  description   = "Temporary materialization dataset for SQL queries submitted from Databricks"
  location      = var.gcp_project_querying_location
  # 24 hour table expiry period
  default_table_expiration_ms = 3600000 * 24

  access {
    role          = "OWNER"
    user_by_email = data.google_client_openid_userinfo.me.email
  }

  access {
    role          = "WRITER"
    user_by_email = google_service_account.sa.email
  }
}
