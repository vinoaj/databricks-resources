terraform {
  required_providers {
    databricks = {
      source  = "databricks/databricks"
      version = "~>1.6.1"
    }
    google = {
      source  = "hashicorp/google"
      version = "~>4.41.0"
    }
    time = {
        source = "hashicorp/time"
        version = "~>0.9.0"
    }
  }
}

provider "databricks" {
    profile = "e2-field-eng-west"
    host = var.workspace_url
}

provider "google" {
  project = var.gcp_project_querying
}

provider "time" {}

data "databricks_current_user" "me" {}
data "google_client_openid_userinfo" "me" {}
data "google_client_config" "current" {}

# data "databricks_group" "x" {
#     display_name = "cluster-creator"
# }

# output "me" {
#     value = data.databricks_current_user.me.user_name
# }

# output "group_members" {
#     value = data.databricks_group.x.users
# }