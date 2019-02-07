#!/bin/env python
from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim
import ssl
import sys

argvs = sys.argv
target_vm = argvs[1]
target_metric_group = argvs[2]
target_metric_key = argvs[3]
context = ssl._create_unverified_context()

si = SmartConnect(host="ホスト名/IPアドレス",
                  user="ユーザ名",
                  pwd="パスワード",
                  port=443,
                  sslContext=context)

content = si.RetrieveContent()
perfManager = content.perfManager
containerView = content.viewManager.CreateContainerView(content.rootFolder, [vim.VirtualMachine], True)

children = containerView.view
for child in children:
    if child.name == target_vm:
        print("VM name: %s" % child.name)
        for m in perfManager.QueryAvailablePerfMetric(entity=child):
            counter = perfManager.QueryPerfCounter([m.counterId])
            if counter[0].groupInfo.key == target_metric_group and counter[0].nameInfo.key == target_metric_key:
                metricId = vim.PerformanceManager.MetricId(counterId=m.counterId, instance="*")
                spec = vim.PerformanceManager.QuerySpec(maxSample=1, entity=child, metricId=[metricId])
                result = perfManager.QueryStats(querySpec=[spec])
                print("Metric[%s.%s]: %f" % (counter[0].groupInfo.key, counter[0].nameInfo.key, result[0].value[0].value[0]))

