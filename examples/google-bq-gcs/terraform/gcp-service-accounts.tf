resource "google_service_account" "sa" {
  account_id   = var.service_account_name
  display_name = "Service Account for Databricks BigQuery & GCS access"
}

resource "google_service_account_key" "sa_key" {
  service_account_id = google_service_account.sa.name
}

locals {
  querying_project_roles = [
    "roles/bigquery.dataEditor",
    "roles/bigquery.jobUser",
    "roles/bigquery.readSessionUser",
  ]
  temp_bucket_roles = [
    "roles/storage.objectAdmin",
    "roles/storage.legacyBucketOwner",
    "roles/storage.legacyObjectOwner"
  ]
  project_role_combo = distinct(flatten([
    for project in var.gcp_project_datasources : [
      for role in var.service_account_roles_datasource_project : {
        project = project
        role    = role
      }
    ]
    ]
  ))
}

output "prc" {
  value = local.project_role_combo
}

# resource "google_project_iam_custom_role" "querying_project_permissions" {
#   role_id = "databricks_querying_role"
#   title   = "Databricks Role for Querying Project"
#   permissions = [
#     "bigquery.dataEditor",
#     "bigquery.jobUser",
#     "bigquery.readSessionUser",
#   ]
# }

resource "google_project_iam_binding" "querying_project" {
  for_each = toset(local.querying_project_roles)
  project  = var.gcp_project_querying
  role     = each.value
  members  = ["serviceAccount:${google_service_account.sa.email}"]
}

# resource "google_project_iam_custom_role" "datasource_projects_permissions" {
#   role_id     = "databricks_datasource_access"
#   title       = "Databricks Role for BigQuery Access"
#   permissions = var.service_account_roles_datasource_project
# }

resource "time_offset" "expiry_period" {
  offset_days = var.sa_expiry_offset_days
}

resource "google_project_iam_binding" "datasource_projects" {
  # for_each = toset(local.project_role_combo)
  for_each = { for entry in local.project_role_combo: "${entry.project}.${entry.role}" => entry}
  project  = each.value.project
  role     = each.value.role
  members  = ["serviceAccount:${google_service_account.sa.email}"]

  condition {
    title       = "${time_offset.expiry_period.offset_days}-day expiry"
    description = "Expiring at ${time_offset.expiry_period.rfc3339}"
    expression  = "request.time < timestamp(\"${time_offset.expiry_period.rfc3339}\")"
  }
}

# resource "google_project_iam_custom_role" "tmp_bucket_permissions" {
#   role_id = "databricks_tmp_bq_load_bucket"
#   title   = "Databricks Role for BigQuery load staging GCS bucket"
#   permissions = [
#     "storage.objectAdmin",
#     "storage.legacyBucketOwner",
#     "storage.legacyObjectOwner"
#   ]
# }

resource "google_storage_bucket_iam_binding" "tmp_bucket" {
  for_each = toset(local.temp_bucket_roles)
  bucket   = google_storage_bucket.tmp_storage_bucket.name
  role     = each.value
  members  = ["serviceAccount:${google_service_account.sa.email}"]

  condition {
    title       = "${time_offset.expiry_period.offset_days}-day expiry"
    description = "Expiring at ${time_offset.expiry_period.rfc3339}"
    expression  = "request.time < timestamp(\"${time_offset.expiry_period.rfc3339}\")"
  }
}
