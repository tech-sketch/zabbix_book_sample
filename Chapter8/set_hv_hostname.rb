#!/bin/env ruby

require 'rubygems'
require 'rbvmomi'

ZABBIX_SERVER = 'Zabbixサーバホスト名orIPアドレス'
HV_NAME = ARGV[0]
VSPHERE_HOST = ARGV[1]
VSPHERE_ID = 'vSphereユーザ名'
VSPHERE_PASSWORD = 'vSphereパスワード'
ZABBIX_SENDER = 'zabbix_senderパス'

vim = RbVmomi::VIM.connect :host => VSPHERE_HOST, :user => VSPHERE_ID, :password => VSPHERE_PASSWORD, :insecure => true

dc = vim.serviceInstance.find_datacenter

dc.vmFolder.childEntity.grep(RbVmomi::VIM::VirtualMachine).find do |vm|
  cmd = "#{ZABBIX_SENDER} -z #{ZABBIX_SERVER} -s #{vm.name} -k hv.hostname -o #{HV_NAME} > /dev/null"
  if system(cmd)
    next
  else
    print 1
    exit(0)
  end
end
print 0
