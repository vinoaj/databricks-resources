output "databricks_user" {
    value = data.databricks_current_user.me.user_name
}

output "google_user" {
    value = data.google_client_openid_userinfo.me.email
}

output "cluster_read_only" {
    value = databricks_cluster.bq_readonly.url
}

output "cluster_read_write" {
  value = databricks_cluster.bq_readwrite.url
}

