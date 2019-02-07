#!/bin/env ruby

require 'rubygems'
require 'aws-sdk'

ACCESS_KEY_ID = 'アクセスキー'
SECRET_ACCESS_KEY = 'シークレットキー'

## Get EC2 instance list
ec2 = AWS::EC2.new(
  {:access_key_id=> ACCESS_KEY_ID,
   :secret_access_key=> SECRET_ACCESS_KEY
  })
## Get EC2 instance Description
ec2.instances.each do |instance|
  puts "----------------"
  puts "instance id:#{instance.instance_id}"
  puts "type: #{instance.instance_type}"
  puts "AZ: #{instance.availability_zone}"
  puts "status: #{instance.status}"
  puts "image: #{instance.image.description}"
  puts "security_groups:"
  instance.security_groups.each do |group|
    puts "   - #{group.name}"
    group.ip_permissions_list.each do |ip_permission|
      puts "     - #{ip_permission[:from_port]}-#{ip_permission[:to_port]}|#{ip_permission[:ip_ranges]}|#{ip_permission[:ip_protocol]}"
    end
  end
  puts "----------------"
end
