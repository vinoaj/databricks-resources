locals {
  universal_policy = {
    "autoscale.min_workers" : {
      "type" : "optional",
      "defaultValue" : 1,
      "hidden" : true
    },
    "autotermination_minutes" : {
      "type" : "range",
      "defaultValue" : 30,
      "maxValue" : 90
    },
    "custom_tags.team" : {
      "type" : "allowlist",
      "values" : ["devops", "data-engineering", "data-science", "mlops"],
      "hidden" : false
    },
    "custom_tags.owner" : {
      "type" : "allowlist",
      "values" : ["john.doe@example.com", "jane.smith@example.com", "team-leads@example.com"],
      "hidden" : false
    },
    "custom_tags.cost-center" : {
      "type" : "allowlist",
      "values" : ["12345", "22456", "7789", "9900"],
      "hidden" : false
    },
    "enable_elastic_disk" : {
      "type" : "fixed",
      "value" : false,
      "hidden" : true
    },
    "enable_local_disk_encryption" : {
      "type" : "fixed",
      "value" : true,
      "hidden" : true
    },
    "instance_pool_id" : {
      "type" : "forbidden",
      "hidden" : true
    },
    "driver_instance_pool_id" : {
      "type" : "forbidden",
      "hidden" : true
    },
    "spark_version" : {
      "type" : "allowlist",
      "values" : ["auto:latest", "auto:latest-ml", "auto:prev-lts", "auto:prev-lts-ml"],
      # "pattern" : "^13\\.3 LTS$",
      "defaultValue" : "auto:latest"
    }
  }
}

output "universal_policy" {
  value = local.universal_policy
}
