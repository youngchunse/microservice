provider "aws" {
  region = "us-east-1"
}

terraform {
  backend "s3" {
    bucket               = "terraform-state-dev-application"
    dynamodb_table       = "terraform-state-dev-application-lock"
    key                  = "dev/us-east-1/route"
    region               = "us-east-1"
  }
}

module "route" {
  source = "./route53"
}
