locals {
  single_user_policy = {
    "data_security_mode" : {
      "type" : "fixed",
      "value" : "SINGLE_USER"
    }
  }

  user_isolation_policy = {
    "data_security_mode" : {
      "type" : "fixed",
      "value" : "USER_ISOLATION"
    }
  }
}

output "single_user_policy" {
  value = local.single_user_policy
}

output "user_isolation_policy" {
  value = local.user_isolation_policy
}