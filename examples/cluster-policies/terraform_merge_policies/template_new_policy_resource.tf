# Example policy for: dev + interactive + single user + default compute power

variable "policy_additions" {
  description = "User provided policy additions"
  type        = map(any)
  default = {
    "custom_tags.author" = {
      type  = "fixed",
      value = "VV"
    }
  }
}

locals {
  # Policies from various modules
  universal_policy_ref           = module.universal_policy.universal_policy
  environment_dev_policy         = module.environment_policies.dev_policy
  interactive_workload_policy    = module.interactive_workloads_policy.interactive_workloads_policy
  security_single_user_policy    = module.security_mode_policies.single_user_policy
  security_user_isolation_policy = module.security_mode_policies.user_isolation_policy
  compute_default_policy         = module.compute_power_policies.default_compute_policy

  # Security mode must take precedence (security settings must override other settings)
  selected_security_policy = merge(local.security_single_user_policy, local.security_user_isolation_policy)

  # Combine all policies in the correct order of precedence
  combined_policy = merge(
    local.universal_policy_ref,
    local.environment_dev_policy,
    local.interactive_workload_policy,
    local.compute_default_policy,
    local.selected_security_policy
  )

  # User-provided policy additions (if any)
  user_policy_additions = var.policy_additions

  # Detect any conflicting keys between combined_policy and user_policy_additions
  conflicting_keys = [for key in keys(local.user_policy_additions) : key if contains(keys(local.combined_policy), key)]

  # Error out if there are any conflicting keys
  enforce_no_conflicts = length(local.conflicting_keys) > 0 ? error("User policy addition conflict detected for keys: ${local.conflicting_keys}. User attributes cannot override critical settings.") : true

  # Merge the final policy after ensuring there are no conflicts
  # User policy additions will only be applied if they do not conflict with combined policies
  final_policy = merge(local.combined_policy, local.user_policy_additions)

  # Determine the dynamic policy name based on selected configurations
  environment   = contains(keys(local.environment_dev_policy), "custom_tags.environment") ? local.environment_dev_policy["custom_tags.environment"].value : "unknown"
  workload_type = contains(keys(local.interactive_workload_policy), "workload_type.clients.jobs") && local.interactive_workload_policy["workload_type.clients.jobs"].value ? "job" : "interactive"
  access_mode   = contains(keys(local.selected_security_policy), "data_security_mode") ? local.selected_security_policy["data_security_mode"].value : "shared"
  compute_size  = contains(keys(local.compute_default_policy), "autoscale.max_workers") && local.compute_default_policy["autoscale.max_workers"].maxValue > 4 ? "high_compute" : "default"

  # Dynamically generated policy name
  policy_name = format("%s-%s-%s-%s-policy", local.environment, local.workload_type, local.access_mode, local.compute_size)
}

resource "databricks_cluster_policy" "combined_cluster_policy" {
  name       = local.policy_name
  definition = jsonencode(local.final_policy)
}

resource "databricks_permissions" "combined_cluster_policy_permissions" {
  cluster_policy_id = databricks_cluster_policy.combined_cluster_policy.id

  access_control {
    group_name       = "data_eng"
    permission_level = "CAN_USE"
  }

  access_control {
    group_name       = "data_analysts"
    permission_level = "CAN_USE"
  }
}

output "combined_policy" {
  value = local.final_policy
}
