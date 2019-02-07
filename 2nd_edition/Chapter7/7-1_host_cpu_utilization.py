#!/bin/env python
from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim
import ssl

context = ssl._create_unverified_context()

esxi_host = sys.argv[1] #HyperVisor hostname
username = sys.argv[2] #HyperVisor login username
password = sys.argv[3] #HyperVisor login password

si = SmartConnect(host=esxi_host,
                  user=username,
                  pwd=password,
                  port=443,
                  sslContext=context)

content = si.RetrieveContent()

for child in content.rootFolder.childEntity:
    if hasattr(child, 'vmFolder'):
        datacenter = child
        hostFolder = datacenter.hostFolder
        entityList = hostFolder.childEntity
        for entity in entityList:
            for host in entity.host:
                cpu_usage = host.summary.quickStats.overallCpuUsage
                print(cpu_usage)
                break
