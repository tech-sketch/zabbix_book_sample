#!/bin/sh

DEPTH=$1
URL=$2

response_code=`curl -L --max-redirs $DEPTH $URL -s -o /tmp/curl.tmp -w "%{http_code}"`

echo $response_code
