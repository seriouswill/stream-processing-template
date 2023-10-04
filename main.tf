variable "gh_user" {
  description = "Name of key for GitHub user to access the url"
  type        = string
}

variable "repo_url" {
  description = "The URL of the git repository to clone"
  type        = string
  default     = "https://github.com/${var.gh_user}/stream-processing-template.git"  # Optional default value
}

variable "key_name" {
  description = "Name of key for AWS access"
  type        = string
}

provider "aws" {
  region = "eu-west-2"
}

resource "aws_instance" "msk_client" {
  ami             = "ami-0b2287cff5d6be10f" # Amazon Linux 2 AMI (HVM) - Kernel 5.10, SSD Volume Type
  instance_type   = "t2.micro"
  key_name        = "${var.key_name}" # Ensure you have this key pair in AWS
  user_data = <<-EOF
              #!/bin/bash
              sudo yum update -y
              sudo yum install -y python3
              sudo yum install -y java-1.8.0-openjdk-devel
              sudo yum install -y git
              
              # Install confluent-kafka for Python
              pip3 install confluent-kafka

              # Download and extract Kafka
              wget https://downloads.apache.org/kafka/3.5.1/kafka_2.12-3.5.1.tgz -P /home/ec2-user/
              tar -xzf /home/ec2-user/kafka_2.12-3.5.1.tgz -C /home/ec2-user/
              
              
              # Clone the git repository
              git clone ${var.repo_url} /home/ec2-user/stream-processing-template
              EOF


  tags = {
    Name = "${var.git_username}MSKClient"
  }

    
  
}

output "instance_public_ip" {
  value = aws_instance.msk_client.public_ip
}
