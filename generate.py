#! /bin/python3

import sys

num_groups = int(sys.argv[1])

PROVIDER = """
provider "aws" {
  version = "2.68.0"
}"""

SUBNET_GROUP = """
resource "aws_elasticache_subnet_group" "group_%03d" {
  name = "subnet-group-%03d"
  subnet_ids = ["subnet-0b3aca8eb8c1b289d"]
}"""

print(PROVIDER.lstrip())
for i in range(1, num_groups + 1):
    print(SUBNET_GROUP % (i, i))
