template "/etc/zabbix/zabbix_agentd.conf" do
  source "zabbix_agentd.conf.erb"
  owner "zabbix"
  group "zabbix"
  mode "0644"
  notifies :restart, "service[zabbix-agent]"
end

service "zabbix-agent"
