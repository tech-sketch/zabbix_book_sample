include_recipe "zabbix_agent::add_repo"

package "zabbix-agent" do
  case node.platform
  when "centos", "redhat", "amazon"
    version "#{node.zabbix.agent.yum.version}" if !node.zabbix.agent.yum.version.empty?
    action :install
  when "ubuntu", "debian"
    version "#{node.zabbix.agent.apt.version}" if !node.zabbix.agent.apt.version.empty?
    action :install
  end
end
