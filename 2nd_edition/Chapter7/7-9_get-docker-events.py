#!/bin/env python
import docker
import sys
import time
import subprocess

args = sys.argv

interval = args[1] #第1引数:取得期間(秒)指定(現在時刻から何秒前に発生したイベントをまとめて収集するかを指定)
zabbix_server = args[2] #第2引数:データ送付先Zabbixサーバ
zabbix_host = args[3] #第3引数:Zabbixトラッパーアイテムの登録先ホスト名
zabbix_itemkey = args[4] #第4引数:Zabbixトラッパーアイテムキー名

client = docker.DockerClient(base_url='tcp://DockerホストのIP:2375')

until = int(time.time()) #スクリプト実行時の現在時刻を取得
since = until - int(interval)

for event in client.events(since=since, until=until):
    output = subprocess.check_output("zabbix_sender -z {} -s {} -k {} -o '{}'".format(zabbix_server, zabbix_host, zabbix_itemkey, event), shell=True)
    print(output)
