#!/bin/env ruby
require 'rubygems'
require 'aws-sdk'

send_to = ARGV[0]
subject = ARGV[1]
message_body = ARGV[2]

ACCESS_KEY_ID = 'アクセスキー'
SECRET_ACCESS_KEY = 'シークレットキー'
TOPIC_ARN = 'トピックARN'

client = AWS::SNS::Client.new({:access_key_id=> ACCESS_KEY_ID,:secret_access_key=> SECRET_ACCESS_KEY})
client.publish({:topic_arn=>TOPIC_ARN, :message => message_body, :subject => subject})
