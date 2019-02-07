#!/bin/env python

import sys
import shlex,subprocess
from psphere.client import Client
from psphere.managedobjects import HostSystem

zabbix_sender = 'zabbix_senderパス'
zabbix_server = 'Zabbixサーバホスト名orIPアドレス'

esxi_host = sys.argv[1]  #HyperVisor hostname
username = sys.argv[2]  #HyperVisor login username
password = sys.argv[3]  #HyperVisor login password
zabbix_host = sys.argv[4]  #Target Zabbix Host
cpu_item = 'esxi.cpu.usage'
memory_item = 'esxi.memory.usage'

client = Client(esxi_host, username, password)

hosts = HostSystem.all(client)
cpu_usage = hosts[0].summary.quickStats.overallCpuUsage
memory_usage = hosts[0].summary.quickStats.overallMemoryUsage

cpu_registry_command = "%(zabbix_sender)s -z '%(zabbix_server)s' -s '%(zabbix_host)s' -k '%(cpu_item)s' -o %(cpu_usage)s" % locals()
memory_registry_command = "%(zabbix_sender)s -z '%(zabbix_server)s' -s '%(zabbix_host)s' -k '%(memory_item)s' -o %(memory_usage)s" % locals()

try:
    subprocess.check_output(shlex.split(cpu_registry_command))
    subprocess.check_output(shlex.split(memory_registry_command))
    print 0
except subprocess.CalledProcessError as error:
    print 1
