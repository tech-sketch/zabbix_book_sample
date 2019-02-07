#!/bin/env python
from zabbix_api import ZabbixAPI
from datetime import datetime

api = ZabbixAPI(server="http://localhost/zabbix")
api.login("Admin", "zabbix")
itemid = 23305 #アイテムID 23305のヒストリデータを取得
time_from = int(datetime.now().timestamp()) - 60 #現在時刻の60秒前の時間をunixtimeで設定
result = api.history.get({
  "history": 0,
  "itemids": [itemid],
  "time_from": time_from})
print(result)
