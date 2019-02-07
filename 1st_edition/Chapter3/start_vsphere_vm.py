#!/bin/env python

import sys
from psphere.client import Client

argvs = sys.argv
target_host = argvs[1]    # 第1引数に指定したターゲットホスト名取得
target_vm = argvs[2]    # 第2引数に指定したターゲットVM名取得

client = Client("ホスト名/IPアドレス", "ログインユーザ名", "パスワード")

host = HostSystem.get(client, name=target_host)    #ターゲットホストシステム情報取得
for vm in host.vm:
    if vm.name == target_vm:
        vm.PowerOnVM_Task()    # ターゲットVMのPowerOn実行
