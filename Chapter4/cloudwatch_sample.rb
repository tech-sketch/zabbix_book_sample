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

client = AWS::CloudWatch::Client.new({
                                    :access_key_id=> Access_key_id,
                                    :secret_access_key=> Secret_access_key
                                     })

ec2_cpu_util = client.get_metric_statistics({:namespace => 'AWS/EC2', 
                                            :metric_name => 'CPUUtilization',
                                            :dimensions => [{:name => 'InstanceId',
                                                            :value => Instance_id}],
                                            :start_time => STARTTIME,
                                            :end_time => ENDTIME,
                                            :period => 3600,
                                            :statistics => ['Average']
                                            })

ec2_cpu_util[:datapoints].each do | datapoint |
  p "time :#{datapoint[:timestamp].to_s}  average :#{datapoint[:average].to_s}"
end
