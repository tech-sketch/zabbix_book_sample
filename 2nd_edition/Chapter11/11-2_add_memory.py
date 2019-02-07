#!/bin/env python
import sys
from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim
import ssl

argvs = sys.argv
HOSTNAME = argvs[1]
ADD_MEMORY_SIZE = argvs[2]

context = ssl._create_unverified_context()

si = SmartConnect(
    host="ホスト名",
    user="ユーザ名",
    pwd="パスワード",
    port=443,
    sslContext=context)

content = si.RetrieveContent()
config = vim.vm.ConfigSpec()

try:
    for child in content.rootFolder.childEntity:
        if hasattr(child, 'vmFolder'):
            datacenter = child
            hostFolder = datacenter.hostFolder
            entityList = hostFolder.childEntity
            for entity in entityList:
                for host in entity.host:
                    for vm in host.vm:
                        if vm.name == HOSTNAME:
                            config.memoryMB = vm.summary.config.memorySizeMB + int(ADD_MEMORY_SIZE)
                            vm.ReconfigVM_Task(spec=config)
                            break
except:
    print("[Error] Reconfigure VM")
else:
    print("[Successful] Reconfigure VM")
