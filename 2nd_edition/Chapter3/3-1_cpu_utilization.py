#!/bin/env python
from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim
import ssl

context = ssl._create_unverified_context()
si = SmartConnect(host="ホスト名",
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
                cpu_usage = host.summary.quickStats.overallCpuUsage
                cpu_core_num = host.summary.hardware.numCpuCores
                cpu_clock = host.summary.hardware.cpuMhz
                print("Host name: %s" % host.name)
                print("CPU Usage(MHz): %d" % cpu_usage)
                print("CPU Usage(%%): %f" % ((float(cpu_usage)/(cpu_core_num*cpu_clock))*100))
                for vm in host.vm:
                    vm_cpu_usage = vm.summary.quickStats.overallCpuUsage
                    vm_cpu_core_num = vm.summary.config.numCpu
                    print("VM name: %s" % vm.name)
                    print("CPU Usage(MHz): %d" % vm_cpu_usage)
                    print("CPU Usage(%%): %f ¥n" % ((float(vm_cpu_usage)/(vm_cpu_core_num*cpu_clock))*100))
