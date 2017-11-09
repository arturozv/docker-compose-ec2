# user_data = "${data.template_file.user_data.rendered}"
data "template_file" "user_data" {
  template = "${file("files/user-data.sh")}"
  vars {
    DOCKER_IMAGE = "${var.docker_image}:${var.docker_tag}"
  }
}

resource "aws_instance" "docker" {
  ami           = "${var.ami}"
  instance_type = "${var.instance_type}"
  user_data = "${data.template_file.user_data.rendered}"

  tags {
    Name = "${var.service_name}"
  }
}

resource "aws_security_group" "security_group" {
  name = "${var.service_name}-sg"
  description = "${var.service_name}Security Group"

  # SSH access
  ingress {
    from_port = 22
    to_port = 22
    protocol = "tcp"
    cidr_blocks = [
      "0.0.0.0/0"]
  }

  # HTTP access
  ingress {
    from_port = 80
    to_port = 80
    protocol = "tcp"
    cidr_blocks = [
      "0.0.0.0/0"]
  }

  egress {
    from_port = 0
    to_port = 0
    protocol = "-1"
    cidr_blocks = [
      "0.0.0.0/0"]
  }
}

