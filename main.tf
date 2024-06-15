terraform{
    required_providers{
        aws = {
            source = "hashicorp/aws"
            version = "~> 3.27"
        }
    }

    required_version = ">= 0.14.9"
}

provider "aws" {
    profile = "default"
    region = "us-west-2"
}

resource "aws_instance" "app_server"{
    ami = "ami-0cf2b4e024cdb6960"
    instance_type = "t2.micro"
    key_name = "devops"
    tags = {
        Name = "app"
    }
}