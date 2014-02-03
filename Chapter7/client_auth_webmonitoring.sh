#!/bin/sh

KEY=$1
URL=$2
PASSWORD="Input password"
WORD="Input check word"

include_line_num=`curl -s --insecure --cert $KEY:$PASSWORD $URL |grep "$WORD" |wc -l 2> /dev/null`

if [ $include_line_num -gt 0 ];
then
    echo "OK"
else
    echo "NG"
fi
