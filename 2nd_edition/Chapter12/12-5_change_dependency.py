#!/bin/env python
import sys
from zabbix_api import ZabbixAPI
from datetime import datetime
ZABBIX_URL = 'http://Zabbixサーバホスト名またはIPアドレス/zabbix'
ZABBIX_LOGIN = 'Zabbixサーバログイン名'
ZABBIX_PASSWORD = 'Zabbixサーバログインパスワード'
TRIGGER_NAME = 'トリガー名'
argvs = sys.argv
HV_NAME = argvs[1]
VM_NAME = argvs[2]

class ZbxOperation:
    def __init__(self, url, username, password):
        self.api = ZabbixAPI(server=url)
        self.api.login(username, password)

    def get_trigger_id(self, host_name, trigger_name):
        result = self.api.trigger.get({
            "filter": {
                "host": host_name,
                "name": trigger_name,
             }})
        return result[0]['triggerid']

    def delete_trigger_dependency(self, trigger_id):
        self.api.trigger.deletedependencies({"triggerid": trigger_id})

    def add_trigger_dependency(self, trigger_id, depend_on_id):
        self.api.trigger.adddependencies({"triggerid": trigger_id, "dependsOnTriggerid": depend_on_id})

zbx_ope = ZbxOperation(ZABBIX_URL, ZABBIX_LOGIN, ZABBIX_PASSWORD)
vm_trigger_id = zbx_ope.get_trigger_id(VM_NAME, TRIGGER_NAME)
zbx_ope.delete_trigger_dependency(vm_trigger_id)
hv_trigger_id = zbx_ope.get_trigger_id(HV_NAME, TRIGGER_NAME)
zbx_ope.add_trigger_dependency(vm_trigger_id, hv_trigger_id)
