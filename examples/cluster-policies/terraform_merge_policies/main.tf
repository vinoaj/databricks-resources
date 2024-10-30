terraform {
  required_providers {
    databricks = {
      source  = "databricks/databricks"
      version = "1.56.0"
    }
  }
}

provider "databricks" {
  # Configuration options
}


module "universal_policy" {
  source = "./modules"
}

module "environment_policies" {
  source = "./modules"
}

module "interactive_workloads_policy" {
  source = "./modules"
}

module "security_mode_policies" {
  source = "./modules"
}

module "compute_power_policies" {
  source = "./modules"
}
