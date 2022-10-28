resource "google_storage_bucket" "tmp_storage_bucket" {
  name                        = var.tmp_gcs_bucket_name
  location                    = var.tmp_gcs_bucket_location
  storage_class               = "STANDARD"
  uniform_bucket_level_access = true

  lifecycle_rule {
    condition {
      age = 2
    }
    action {
      type = "Delete"
    }
  }

#   labels = {
#     "Purpose"    = "Temporary staging bucket for loading data into BigQuery from Databricks"
#     "Created_By" = data.google_client_openid_userinfo.me.email
#   }
}
