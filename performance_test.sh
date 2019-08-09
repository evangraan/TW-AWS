#!/bin/bash

if [ "$1" == "" ]; then
  NUM=10
else
  NUM=$1
fi

I=0
while [ $I -lt $NUM ]; do
  echo "Spawning $I"
  #pgcli -h hostname -p 3306 -U user TW < performance-test.sql &
  pgcli -h hostname -p 3306 -U user TW < performance-test.sql &
  I=$(($I+1))
done

sleep 60
for f in $(ps aux | grep pgcli | grep hostname | tr -s ' ' ' ' | cut -d ' ' -f2); do
  kill -9 $f
done
