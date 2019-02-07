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
client = AWS::CloudWatch::Client.new({:access_key_id=> ACCESS_KEY_ID, :secret_access_key=> SECRET_ACCESS_KEY})

ec2_cpu_util = client.get_metric_statistics({:namespace => 'AWS/EC2',
                                             :metric_name => 'CPUUtilization',
                                             :dimensions => [{:name => 'InstanceId',
                                             :value => INSTANCE_ID}],
                                             :start_time => STARTTIME,
                                             :end_time => ENDTIME,
                                             :period => 3600,
                                             :statistics => ['Average']
                                             })
ec2_cpu_util[:datapoints].each do | datapoint |
  p "time :#{datapoint[:timestamp].to_s} average :#{datapoint[:average].to_s}"
end
