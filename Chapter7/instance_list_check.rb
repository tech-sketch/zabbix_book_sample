#!/bin/env ruby

require 'rubygems'
require 'aws-sdk'
require 'zbxapi'

ACCESS_KEY_ID = 'アクセスキー'
SECRET_ACCESS_KEY = 'シークレットキー'
ZABBIX_API_URL = 'http://Zabbixサーバホスト名orIPアドレス/zabbix/api_jsonrpc.php'
ZABBIX_LOGIN = 'Zabbixログインユーザ名'
ZABBIX_PASSWORD = 'Zabbixログインパスワード'
TARGET_HOSTGROUP = "照合対象ホストグループ名"

## Get EC2 instance list
ec2 = AWS::EC2.new(
    {:access_key_id=> ACCESS_KEY_ID,
     :secret_access_key=> SECRET_ACCESS_KEY
    })
instance_ids = [] 
ec2.instances.each do |instance|
  instance_ids << instance.id
end
## Get Zabbix hostgroup id
zbxapi = ZabbixAPI.new(ZABBIX_API_URL)
zbxapi.login(ZABBIX_LOGIN,ZABBIX_PASSWORD)
hostgroups = zbxapi.raw_api('hostgroup.get',{:filter => {:name => TARGET_HOSTGROUP}})
target_hostgroupid = hostgroups.first['groupid']
## Get Zabbix host list
hosts = zbxapi.raw_api('host.get',{:output => 'extend', :groupids => target_hostgroupid})
hosts.each do |host|
  if !instance_ids.include?(host['name'])
    zbxapi.raw_api('host.delete',{:hostid => host['hostid']})
  end
end
