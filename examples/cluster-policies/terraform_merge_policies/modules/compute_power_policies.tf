locals {
  allowed_instance_types = ["m5.large", "m5.xlarge", "m5.2xlarge"]

  default_compute_policy = {
    "autoscale.max_workers" : {
      "type" : "range",
      "defaultValue" : 1,
      "minValue" : 1,
      "maxValue" : 4
    },
    "driver_node_type_id" : {
      "type" : "allowlist",
      "values" : local.allowed_instance_types
    },
    "node_type_id" : {
      "type" : "allowlist",
      "values" : local.allowed_instance_types
    }
  }

  high_compute_policy = {
    "autoscale.max_workers" : {
      "type" : "range",
      "defaultValue" : 1,
      "minValue" : 1,
      "maxValue" : 8
    },
    "driver_node_type_id" : {
      "type" : "allowlist",
      "values" : local.allowed_instance_types
    },
    "node_type_id" : {
      "type" : "allowlist",
      "values" : local.allowed_instance_types
    }
  }
}

output "default_compute_policy" {
  value = local.default_compute_policy
}

output "high_compute_policy" {
  value = local.high_compute_policy
}