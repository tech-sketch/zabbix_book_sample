if node.zabbix.agent.install
  include_recipe "zabbix_agent::install"
  include_recipe "zabbix_agent::rewrite_conf"
elsif node.zabbix.agent.upgrade
  include_recipe "zabbix_agent::remove"
  include_recipe "zabbix_agent::install"
  include_recipe "zabbix_agent::rewrite_conf"
else
  include_recipe "zabbix_agent::rewrite_conf"
end
