#!/bin/env ruby

require 'rubygems'
require 'time'
require 'aws-sdk'

now = Time.now
before = now - 60*60*6
ENDTIME = now.iso8601
STARTTIME = before.iso8601

ACCESS_KEY_ID = 'アクセスキー'
SECRET_ACCESS_KEY = 'シークレットキー'
INSTANCE_ID = 'インスタンスID'
HOST = '登録先ホスト名'
ITEM_KEY = '登録先アイテムキー'
ZABBIX_SENDER = 'zabbix_senderのパス'
ZABBIX_SERVER = 'Zabbixサーバのホスト名orIPアドレス'
ZABBIX_LOGIN = 'ログインユーザ名'
ZABBIX_PASSWORD = 'ログインパスワード'
TMP_FILE = '一時出力ファイル名'


client = AWS::CloudWatch::Client.new(
    {:access_key_id=> ACCESS_KEY_ID,
     :secret_access_key=> SECRET_ACCESS_KEY
    })

ec2_cpu_util = client.get_metric_statistics({:namespace => 'AWS/EC2',
                                            :metric_name => 'CPUUtilization',
                                            :dimensions => [{:name => 'InstanceId',
                                                            :value => INSTANCE_ID}],
                                            :start_time => STARTTIME,
                                            :end_time => ENDTIME,
                                            :period => 3600,
                                            :statistics => ['Average']
                                            })

## Output AWS cloudwatch data to tmp flie 
file = File::open(Tmp_file,'w')
ec2_cpu_util[:datapoints].each do | datapoint |
  data = "#{HOST} #{ITEM_KEY} #{datapoint[:timestamp].to_i.to_s} #{datapoint[:average].to_s}\r\n"
  file.write(data)
end
file.close

## Zabbix sender execute
cmd = "#{ZABBIX_SENDER} -z #{ZABBIX_SERVER} -T -i #{TMP_FILE} >/dev/null"
if system(cmd)
  print 0
else
  print 1
end
