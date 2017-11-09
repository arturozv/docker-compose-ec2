provider "aws" {
  region = "${var.region}"
}

terraform {
  backend "s3" {
    bucket = "tf-states"
    key    = "key"
    region = "us-west-2"
  }
}
