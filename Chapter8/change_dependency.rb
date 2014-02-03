#!/bin/env ruby

require 'rubygems'
require 'zbxapi'

ZABBIX_API_URL = 'http://Zabbixサーバホスト名orIPアドレス/zabbix/api_jsonrpc.php'
ZABBIX_LOGIN = 'Zabbixサーバログイン名'
ZABBIX_PASSWORD = 'Zabbixサーバログインパスワード'
TRIGGER_NAME = 'トリガー名'
HV_NAME = ARGV[0]
VM_NAME = ARGV[1]

## Get Triggerid function
def get_triggerid zbxapi, hostname, trigger_name
  trigger = zbxapi.raw_api('trigger.get',{:filter => {:host => hostname},:output => 'extend'}).find_all do |trigger|
    trigger['description'] == trigger_name
  end
  return trigger.first['triggerid']
end

## Connect Zabbix API
zbxapi = ZabbixAPI.new(ZABBIX_API_URL)
zbxapi.login(ZABBIX_LOGIN,ZABBIX_PASSWORD)
## Get Target VM Trigger info

vm_trigger_id = get_triggerid zbxapi,VM_NAME, TRIGGER_NAME

## Delete Trigger Dependencies
zbxapi.raw_api('trigger.deletedependencies',{:triggerid => vm_trigger_id})

## Get Target HV Trigger info
hv_trigger_id = get_triggerid zbxapi, HV_NAME, TRIGGER_NAME

## Add Trigger Dependencies
zbxapi.raw_api('trigger.adddependencies',{:triggerid => vm_trigger_id,:dependsOnTriggerid => hv_trigger_id})
