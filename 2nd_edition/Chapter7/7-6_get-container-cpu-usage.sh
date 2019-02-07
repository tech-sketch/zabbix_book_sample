#!/bin/bash

CONTAINER_ID=$1
CPU_TYPE=$2

cd /sys/fs/cgroup/cpuacct/docker/${CONTAINER_ID}*

cat cpuacct.stat | grep $CPU_TYPE |cut -d ' ' -f 2
