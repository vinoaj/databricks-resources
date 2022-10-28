resource "databricks_group" "sec_admin" {
  display_name = "sec-admin"
}

resource "databricks_group" "cluster_creator" {
  display_name               = "cluster-creator"
  allow_cluster_create       = true
  allow_instance_pool_create = true
}

resource "databricks_group_member" "me" {
  group_id  = databricks_group.cluster_creator.id
  member_id = data.databricks_current_user.me.id
}
