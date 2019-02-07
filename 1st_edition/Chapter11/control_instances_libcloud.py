#!/bin/env python

import sys

from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

ACCESS_ID = 'アクセスキーID'
SECRET_KEY = 'シークレットキー'

provider = sys.argv[1]
instance_id = sys.argv[2]
command = sys.argv[3]

Driver = get_driver(Provider.__dict__[provider])

conn = Driver(ACCESS_ID, SECRET_KEY)
nodes = conn.list_nodes()

for node in nodes:
    if node.id == instance_id:
        if command == "reboot" and node.state == 0:
            result = conn.reboot_node(node)
        elif command == "terminate":
            result = conn.destroy_node(node)
        elif command == "start" and node.state != 0:
            result = conn.ex_start_node(node)
        elif command == "stop" and node.state == 0:
            result = conn.ex_stop_node(node)
        else:
            result = False
        if result == True:
            print "[OK] %s <%s>" %  (command, node.name)
        else:
            print "[NG] %s <%s>" % (command, node.name)
