require 'rubygems'
require 'aws-sdk'
 
command = ARGV[0]
ACCESS_KEY_ID = 'アクセスキー'
SECRET_ACCESS_KEY = 'シークレットキー'
QUEUE_URL = 'https://sqs.us-east-1.amazonaws.com/キューID/test_queue'
client = AWS::SQS::Client.new({:access_key_id=> ACCESS_KEY_ID,:secret_access_key=> SECRET_ACCESS_KEY})
client.send_message({:queue_url => QUEUE_URL, :message_body => command})
