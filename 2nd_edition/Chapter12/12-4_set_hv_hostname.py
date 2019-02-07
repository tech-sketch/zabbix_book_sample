#!/bin/env python
import sys
from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim
import ssl
import subprocess

argvs = sys.argv
HV_NAME = argvs[1]
VSPHERE_HOST = argvs[2]
ZABBIX_SERVER = 'Zabbixサーバホスト名またはIPアドレス'
VSPHERE_ID = 'vSphereユーザ名'
VSPHERE_PASSWORD = 'vSphereパスワード'
ZABBIX_SENDER = 'zabbix_senderパス'
context = ssl._create_unverified_context()
si = SmartConnect(
    host=VSPHERE_HOST,
    user=VSPHERE_ID,
    pwd=VSPHERE_PASSWORD,
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
                for vm in host.vm:
                    cmd = "{} -z {} -s {} -k hv.hostname -o {} > /dev/null".format(ZABBIX_SENDER, ZABBIX_SERVER, vm.name, HV_NAME)
                    result = subprocess.run(cmd, shell=True)
                    if result.returncode != 0:
                        print(1)
                        exit(0)
print(0)
exit(0)
