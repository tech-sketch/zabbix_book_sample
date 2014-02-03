#!/bin/env python
import libvirt

uri = "qemu+ssh://ユーザ名@ホスト名orIPアドレス/system"

connection = libvirt.open(uri)

vmid_list = connection.listDomainsID()

for vmid in vmid_list:
    vm = connection.lookupByID(vmid)
    cpu_state = vm.vcpus()
    cpu_time = 0
    for cpu in cpu_state[0]:
        cpu_time += cpu[2]
    memory_state = vm.memoryStats()
    print "VM name: %s" % vm.name()
    print "CPU Usage time: %.1f msec" % (cpu_time/10**6)
    print "Memory Total Size: %.2f MB" % (memory_state['actual']/1024)
    print "Memory Resident Set Size: %.2f MB" % (memory_state['rss']/1024)
