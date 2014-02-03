#!/bin/env python

from psphere.client import Client
from psphere.managedobjects import HostSystem

client = Client("ホスト名/IPアドレス", "ログインユーザ名", "パスワード")

hosts = HostSystem.all(client)
for host in hosts:
    cpu_usage = host.summary.quickStats.overallCpuUsage
    cpu_core_num = host.summary.hardware.numCpuCores
    cpu_clock = host.summary.hardware.cpuMhz
    print "Host name: %s" % host.name
    print "CPU Usage(MHz): %d" % cpu_usage
    print "CPU Usage(%%): %f \n" % ((float(cpu_usage)/(cpu_core_num*cpu_clock))*100)
    for vm in host.vm:
        vm_cpu_usage = vm.summary.quickStats.overallCpuUsage
        vm_cpu_core_num = vm.summary.config.numCpu
        print "VM name: %s" % vm.name
        print "CPU Usage(MHz): %d" % vm_cpu_usage
        print "CPU Usage(%%): %f \n" % ((float(vm_cpu_usage)/(vm_cpu_core_num*cpu_clock))*100)
