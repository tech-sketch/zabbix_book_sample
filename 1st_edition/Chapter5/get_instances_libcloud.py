#!/bin/env python

from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

ACCESS_ID = 'アクセスキーID'
SECRET_KEY = 'シークレットキー'

Driver = get_driver(Provider.EC2_AP_NORTHEAST)
conn = Driver(ACCESS_ID, SECRET_KEY)
nodes = conn.list_nodes()

print nodes
