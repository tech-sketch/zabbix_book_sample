#!/bin/env python
from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim
import ssl
import sys

argvs = sys.argv
target_host = argvs[1]

target_vm = argvs[2]
context = ssl._create_unverified_context()
si = SmartConnect(host="ホスト名/IPアドレス",
                  user="ユーザ名",
                  pwd="パスワード",
                  port=443, #vSphere API稼動ポート:https(443)がデフォルト
                  sslContext=context)

content = si.RetrieveContent()

for child in content.rootFolder.childEntity:
    if hasattr(child, 'vmFolder'):
        datacenter = child
        hostFolder = datacenter.hostFolder
        entityList = hostFolder.childEntity
        for entity in entityList:
            for host in entity.host:
                if host.name == target_host:
                    for vm in host.vm:
                        if vm.name == target_vm:
                            vm.PowerOnVM_Task()
