default[:zabbix][:server] = "Zabbixサーバホスト名 または IPアドレス"
default[:zabbix][:agent][:install] = true # Zabbixエージェントインストール実行フラグ
default[:zabbix][:agent][:upgrade] = false # Zabbixエージェントアップデート実行フラグ
default[:zabbix][:agent][:yum][:version] = "2.2.1-1.el6" # yumインストール時のバージョン指定
default[:zabbix][:agent][:apt][:version] = "1:2.2.1-1" # apt-getインストール時のバージョン指定
