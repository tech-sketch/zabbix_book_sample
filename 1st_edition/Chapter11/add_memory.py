#!/bin/env python
import sys
from psphere.client import Client
from psphere.managedobjects import HostSystem
argvs = sys.argv
HOSTNAME = argvs[1]
ADD_MEMORY_SIZE = argvs[2]
client = Client("ホスト名/IPアドレス", "ログインユーザ名", "パスワード")
config = client.factory.create('ns0:VirtualMachineConfigSpec')

hosts = HostSystem.all(client)
try:
    for host in hosts:
        for vm in host.vm:
            if vm.name == HOSTNAME:
                config.memoryMB = vm.summary.config.memorySizeMB + int(ADD_MEMORY_SIZE)
                vm.ReconfigVM_Task(spec=config)
except:
    print "[Error] Reconfigure VM"
else:
    print "[Successful] Reconfigure VM"
