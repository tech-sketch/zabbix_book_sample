#!/bin/env ruby

require 'rubygems'
require 'deltacloud'

ACCESS_ID = 'アクセスキーID'
SECRET_KEY = 'シークレットキー'
Deltacloud.new(:ec2, {:provider => "ap-northeast-1"}) do |driver|
    credentials = OpenStruct.new(:user => ACCESS_ID, :password => SECRET_KEY)
    puts "|  instance_id  |  status  |  ami_id  |"
    puts "-------------------------------------"
    driver.instances(credentials).each do |instance|
        puts "|  #{instance.id}  |  #{instance.state}  |  #{instance.name}  |"
   end
end
