#!/bin/env ruby
require 'rubygems'
require 'deltacloud'

api_url = 'http://hostname:3001/api'
api_name = 'アクセスキーID'
api_password = 'シークレットキー'

client = DeltaCloud.new( api_name, api_password, api_url )
puts "|  instance_id  |  status  |  ami_id  |"
puts "----------------------------------------"
client.instances.each do |instance|
    puts "|  #{instance.id}  |  #{instance.state}  |  #{instance.name}  |"
end
