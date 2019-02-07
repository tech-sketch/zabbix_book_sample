#!/bin/env python
import boto3
import sys

topic_arn = 'arn:aws:sns:ap-northeast-1:xxxxxxxxx:test-topic'
access_key_id = 'アクセスキーID'
secret_access_key = 'シークレットキー'
region = 'ap-northeast-1'

subject = sys.argv[1]
message = sys.argv[2]

client = boto3.client('sns', aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key, region_name=region)

request = {
  'TopicArn': topic_arn,
  'Subject': subject,
  'Message': message,
}

response = client.publish(**request)
print(response)
