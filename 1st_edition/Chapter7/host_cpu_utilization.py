#!/bin/env python

from psphere.client import Client
from psphere.managedobjects import HostSystem
esxi_host = sys.argv[1]  #HyperVisor hostname
username = sys.argv[2]  #HyperVisor login username
password = sys.argv[3]  #HyperVisor login password

client = Client(esxi_host, username, password)

hosts = HostSystem.all(client)
cpu_usage = hosts[0].summary.quickStats.overallCpuUsage
print cpu_usage
