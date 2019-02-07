#!/bin/env python
from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim
import ssl

context = ssl._create_unverified_context()

si = SmartConnect(host="ホスト名/IPアドレス",
                  user="ユーザ名",
                  pwd="パスワード",
                  port=443,
                  sslContext=context)

content = si.RetrieveContent()

taskFilterSpec = vim.TaskFilterSpec()
eventFilterSpec = vim.event.EventFilterSpec()
task_controller = content.taskManager.CreateCollectorForTasks(filter=taskFilterSpec)
event_controller = content.eventManager.CreateCollectorForEvents(filter=eventFilterSpec)
task_list = task_controller.latestPage
event_list = event_controller.latestPage

print("-------Task List-------")
for task in task_list:
    print("Task Name: %s" % task.name)
    print("Status: %s" % task.state)
    print("Entity: %s" % task.entityName)
    print("Date: %s" % task.completeTime)

print("-------Event List-------")
for event in event_list:
    print("Event Name: %s" % event.fullFormattedMessage)
    print("Operation User: %s" % event.userName)
    print("Date: %s" % event.createdTime)
