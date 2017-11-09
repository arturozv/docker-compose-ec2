variable "region" { default = "us-west-2" }
variable "ami" { default = ""} #packer ami
variable "instance_type" {default = "t2.small" }

variable "docker_image" { default = "arturozv/node-api" }
variable "docker_tag" { default = "latest" }
variable "service_name" { default = "docker-compose" }
variable "server_port" {default = "80"}

variable "docker_user" {}
variable "docker_email" {}
variable "docker_password" {}