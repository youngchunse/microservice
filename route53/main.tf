data "aws_elb" "elb" {
  name = var.lb_name
}

data "aws_route53_zone" "primary" {
  name         = var.domain_name
}

resource "aws_route53_record" "www" {
  zone_id = aws_route53_zone.primary.zone_id
  name    = var.domain.name
  type    = "A"

  alias {
    name                   = data.aws_elb.elb.dns_name
    zone_id                = data.aws_elb.elb.zone_id
    evaluate_target_health = true
  }
}
