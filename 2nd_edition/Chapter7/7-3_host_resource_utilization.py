#!/bin/env python
from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim
import ssl

context = ssl._create_unverified_context()

zabbix_sender = 'zabbix_senderパス'
zabbix_server = 'Zabbixサーバホスト名またはIPアドレス'

esxi_host = sys.argv[1] #HyperVisor hostname
username = sys.argv[2] #HyperVisor login username
password = sys.argv[3] #HyperVisor login password
zabbix_host = sys.argv[4] #Target Zabbix Host

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
                memory_usage = host.summary.quickStats.overallMemoryUsage
                cpu_registry_command = "%(zabbix_sender)s -z '%(zabbix_server)s' -s '%(zabbix_host)s' -k '%(cpu_item)s' -o %(cpu_usage)s" % locals()
                memory_registry_command = "%(zabbix_sender)s -z '%(zabbix_server)s' -s '%(zabbix_host)s' -k '%(memory_item)s' -o %(memory_usage)s" % locals()
                try:
                    subprocess.check_output(shlex.split(cpu_registry_command))
                    subprocess.check_output(shlex.split(memory_registry_command))
                    print 0
                except subprocess.CalledProcessError
                    print 1
                    break
