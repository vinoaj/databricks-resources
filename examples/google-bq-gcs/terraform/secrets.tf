resource "databricks_secret_scope" "cloud_secrets_scope" {
  name = var.secret_scope_name
}

resource "databricks_secret_acl" "sec_admin_manage" {
  principal  = databricks_group.sec_admin.display_name
  permission = "MANAGE"
  scope      = databricks_secret_scope.cloud_secrets_scope.name
}

resource "databricks_secret_acl" "cluster_creator_read" {
  principal  = databricks_group.cluster_creator.display_name
  permission = "READ"
  scope      = databricks_secret_scope.cloud_secrets_scope.name
}

locals {
  key_json = jsondecode(base64decode(google_service_account_key.sa_key.private_key))
  key_pkid = local.key_json.private_key_id
  key_pk   = local.key_json.private_key
}

resource "databricks_secret" "credentials" {
  scope        = databricks_secret_scope.cloud_secrets_scope.id
  key          = google_service_account.sa.email
  string_value = google_service_account_key.sa_key.private_key
}

resource "databricks_secret" "private_key_id" {
  scope        = databricks_secret_scope.cloud_secrets_scope.id
  key          = "${google_service_account.sa.email}-private-key-id"
  string_value = local.key_pkid
}

resource "databricks_secret" "private_key" {
  scope        = databricks_secret_scope.cloud_secrets_scope.id
  key          = "${google_service_account.sa.email}-private-key"
  string_value = local.key_pk
}
