locals {
  job_workloads_policy = {
    "data_security_mode" : {
      "type" : "fixed",
      "value" : "SINGLE_USER"
    },
    "workload_type.clients.jobs" : {
      "type" : "fixed",
      "value" : true
    },
    "workload_type.clients.notebooks" : {
      "type" : "fixed",
      "value" : false
    }
  }
}

output "job_workloads_policy" {
  value = local.job_workloads_policy
}