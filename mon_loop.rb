# encoding=UTF-8
# -*- coding: UTF-8 -*-
# coding: UTF-8

require 'rubygems'

require 'net/ssh'
require 'redis'
require 'date'

unless defined? $r
  $r = Redis.new :host => "172.16.0.12", :port => 6379
end


def hi(cmd)
 host = '172.16.0.'
 user = 'root'
 pass = '%^'
 port = 22

(21..21).each do |ip|
 Net::SSH.start( "#{host}#{ip}", user, :password => pass , :port => port) do|ssh|
   puts "-------"*12
   puts "IP:"+host+ip.to_s
   puts "-------"*12

   result = ssh.exec!(cmd)
   return result.to_s
 end
end
end

pre = 0 
cur = $r.llen('MCC_SCT_VIP_REDIS_LISTENER_KEY').to_i

#puts hi('df -lh')

while true do
  if pre == cur 
    if pre == 0
      puts "== 0!"
    else
      puts hi("source /etc/profile; cd /data/ProgramFiles/ongoing_mcc; sh -x restart.sh")
    end
  end
    
  puts Time.now

  sleep 60
  
  pre = cur
  cur = $r.llen('MCC_SCT_VIP_REDIS_LISTENER_KEY').to_i
end

