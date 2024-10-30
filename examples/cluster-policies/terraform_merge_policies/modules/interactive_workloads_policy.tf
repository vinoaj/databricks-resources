locals {
  interactive_workloads_policy = {
    "data_security_mode" : {
      "type" : "allowlist",
      "default" : "SINGLE_USER",
      "values" : ["SINGLE_USER", "USER_ISOLATION"]
    },
    "workload_type.clients.jobs" : {
      "type" : "fixed",
      "value" : false
    },
    "workload_type.clients.notebooks" : {
      "type" : "fixed",
      "value" : true
    }
  }
}

output "interactive_workloads_policy" {
  value = local.interactive_workloads_policy
}
