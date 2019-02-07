#!/bin/env python
import sys
import libvirt

target_vm = sys.argv[1] # 第1引数に指定したターゲットVM名取得
uri = "qemu+ssh://ユーザ名@ホスト名またはIPアドレス/system"

connection = libvirt.open(uri)

vm = connection.lookupByName(target_vm)
vm.create()
