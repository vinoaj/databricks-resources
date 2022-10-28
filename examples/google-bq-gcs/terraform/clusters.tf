data "databricks_node_type" "smallest" {
  local_disk = true
}

data "databricks_spark_version" "latest_lts" {
  long_term_support = true
}

locals {
  secret_prefix = "secrets/${databricks_secret_scope.cloud_secrets_scope.name}/${google_service_account.sa.email}"
  spark_conf_base = {
    "credentials"            = "{{${local.secret_prefix}}}",
    "parentProject"          = var.gcp_project_querying,
    "viewsEnabled"           = true,
    "materializationProject" = var.gcp_project_querying,
    "materializationDataset" = google_bigquery_dataset.materialization_dataset.dataset_id
  }
  spark_conf_write = merge(local.spark_conf_base, {
    "spark.hadoop.google.cloud.auth.service.account.enable"  = true,
    "spark.hadoop.fs.gs.auth.service.account.email"          = google_service_account.sa.email,
    "spark.hadoop.fs.gs.project.id"                          = var.gcp_project_querying,
    "spark.hadoop.fs.gs.auth.service.account.private.key"    = "{{${local.secret_prefix}-private-key}}",
    "spark.hadoop.fs.gs.auth.service.account.private.key.id" = "{{${local.secret_prefix}-private-key-id}}",
    "temporaryGcsBucket"                                     = google_storage_bucket.tmp_storage_bucket.name
  })
}

resource "databricks_cluster" "bq_readonly" {
  depends_on              = [databricks_secret.credentials]
  cluster_name            = "Shared Interactive - BQ READONLY ${google_service_account.sa.email}"
  spark_version           = data.databricks_spark_version.latest_lts.id
  node_type_id            = data.databricks_node_type.smallest.id
  autotermination_minutes = 20
  autoscale {
    min_workers = 1
    max_workers = 50
  }
  /*
  aws_attributes {
    availability           = "SPOT"
    zone_id                = "us-east-1"
    first_on_demand        = 1
    spot_bid_price_percent = 100
  }
  */
  /*
  azure_attributes {
    availability       = "SPOT_WITH_FALLBACK_AZURE"
    first_on_demand    = 1
    spot_bid_max_price = 100
  }
  */
  spark_conf = local.spark_conf_base
}

resource "databricks_cluster" "bq_readwrite" {
  depends_on              = [databricks_secret.credentials]
  cluster_name            = "Shared Interactive - BQ READ+WRITE ${google_service_account.sa.email}"
  spark_version           = data.databricks_spark_version.latest_lts.id
  node_type_id            = data.databricks_node_type.smallest.id
  autotermination_minutes = 20
  autoscale {
    min_workers = 1
    max_workers = 50
  }
  /*
  azure_attributes {
    availability       = "SPOT_WITH_FALLBACK_AZURE"
    first_on_demand    = 1
    spot_bid_max_price = 100
  }
  */
  spark_conf = local.spark_conf_write
}
