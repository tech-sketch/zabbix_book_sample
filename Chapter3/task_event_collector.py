#!/bin/env python

from psphere.client import Client

client = Client("ホスト名/IPアドレス", "ログインユーザ名", "パスワード")

task_controller = client.si.content.taskManager.CreateCollectorForTasks()
event_controller = client.si.content.eventManager.CreateCollectorForEvents()

task_list = task_controller.latestPage
event_list = event_controller.latestPage

print "-------Task List-------"
for task in task_list:
    print "Task Name: %s" % task.name
    print "Status: %s" % task.state
    print "Entity: %s" % task.entityName
    print "Date: %s\n" % task.completeTime

print "-------Event List-------"
for event in event_list:
    print "Event Name: %s" % event.fullFormattedMessage
    print "Operation User: %s" % event.userName
    print "Date: %s\n" % event.createdTime
