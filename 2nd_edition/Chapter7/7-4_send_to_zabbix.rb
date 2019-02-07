#!/bin/env ruby
require 'rubygems'
require 'time'
require 'aws-sdk'

now = Time.now
before = now - 60*60*6
ENDTIME = now.iso8601
STARTTIME = before.iso8601
Access_key_id = 'アクセスキー'
Secret_access_key = 'シークレットキー'
Instance_id = 'インスタンスID'
Host = '登録先ホスト名'
Item_key = '登録先アイテムキー'
Zabbix_sender = 'zabbix_senderのパス'
Zabbix_server = 'Zabbixサーバのホスト名またはIPアドレス'
Zabbix_login = 'ログインユーザ名'
Zabbix_password = 'ログインパスワード'
Tmp_file = '一時出力ファイル名'

client = AWS::CloudWatch::Client.new(
  {
    :access_key_id=> Access_key_id,
    :secret_access_key=> Secret_access_key
  })

ec2_cpu_util = client.get_metric_statistics(
  {
    :namespace => 'AWS/EC2',
    :metric_name => 'CPUUtilization',
    :dimensions => [
      {
        :name => 'InstanceId',
        :value => Instance_id
      }],
    :start_time => STARTTIME,
    :end_time => ENDTIME,
    :period => 3600,
    :statistics => ['Average']
  })

## Output AWS cloudwatch data to tmp flie
file = File::open(Tmp_file,'w')
ec2_cpu_util[:datapoints].each do | datapoint |
  data = "#{Host} #{Item_key} #{datapoint[:timestamp].to_i.to_s} #{datapoint[:average].to_s}\r\n"
  file.write(data)
end

file.close

## Zabbix sender execute
cmd = "#{Zabbix_sender} -z #{Zabbix_server} -T -i #{Tmp_file} >/dev/null"

if system(cmd)
  print 0
else
  print 1
end
