provider "aws" {
  region = "us-east-1"
}
module "route" {
  source = "./route53"
}
