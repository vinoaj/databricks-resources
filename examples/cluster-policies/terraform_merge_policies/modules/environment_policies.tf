locals {
  dev_policy = {
    "aws_attributes.first_on_demand" : {
      "type" : "fixed",
      "value" : 0
    },
    "aws_attributes.availability" : {
      "type" : "fixed",
      "value" : "SPOT_WITH_FALLBACK"
    },
    "aws_attributes.spot_bid_price_percent" : {
      "type" : "fixed",
      "value" : 100
    },
    "custom_tags.environment" : {
      "type" : "fixed",
      "value" : "dev"
    }
  }

  prod_policy = {
    "aws_attributes.first_on_demand" : {
      "type" : "fixed",
      "value" : 0
    },
    "aws_attributes.availability" : {
      "type" : "fixed",
      "value" : "ON_DEMAND"
    },
    "custom_tags.environment" : {
      "type" : "fixed",
      "value" : "prod"
    }
  }
}

output "dev_policy" {
  value = local.dev_policy
}

output "prod_policy" {
  value = local.prod_policy
}