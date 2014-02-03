#!/bin/bash
for file_path in $(/bin/find $1 -type f); do
    filelist="$filelist,"'{"{#FILEPATH}":"'$file_path'"}'
done
echo '{"data":['${filelist#,}' ]}'
