#!/bin/env ruby
require 'rubygems'
require 'aws-sdk'
require 'zbxapi'

Access_key_id = 'アクセスキー'
Secret_access_key = 'シークレットキー'
Zabbix_api_url = 'http://Zabbixサーバホスト名またはIPアドレス/zabbix/api_jsonrpc.php'
Zabbix_login = 'Zabbixログインユーザ名'
Zabbix_password = 'Zabbixログインパスワード'
Target_hostgroup = '照合対象ホストグループ名'

## Get EC2 instance list
ec2 = AWS::EC2.new(
  {
    :access_key_id=> Access_key_id,
    :secret_access_key=> Secret_access_key
  })

instance_ids = []

ec2.instances.each do |instance|
  instance_ids << instance.id
end

## Get Zabbix hostgroup id
zbxapi = ZabbixAPI.new(Zabbix_api_url)
zbxapi.login(Zabbix_login,Zabbix_password)
hostgroups = zbxapi.raw_api('hostgroup.get',{:filter => {:name => Target_hostgroup}})
target_hostgroupid = hostgroups.first['groupid']

## Get Zabbix host list
hosts = zbxapi.raw_api('host.get',{:output => 'extend', :groupids => target_hostgroupid})

hosts.each do |host|
  if !instance_ids.include?(host['name'])
    zbxapi.raw_api('host.delete',{:hostid => host['hostid']})
  end
end
