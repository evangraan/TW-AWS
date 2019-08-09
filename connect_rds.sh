#!/bin/bash
if [ "$1" == "" ]; then
  echo "connect_rds.sh SERVER"
  echo "SERVER can be one of:"
  echo "  aws - the AWS RDS instance"
  echo "  pool - the connection pool endpoint to access the AWS RDS instance"
  echo "  monitor - the connection pool statistics endpoint for monitoring"
  echo "  ssh - log into the connection pool server"
  exit -1
fi

if [ "$1" == "aws" ]; then
  pgcli -h hostname -p 3306 -U user -W TW
fi

if [ "$1" == "pool" ]; then
  pgcli -h hostname -p 3306 -U user -W TW
fi

if [ "$1" == "monitor" ]; then
  echo "After login run 'psql -h 127.0.0.1 -U user -p 3306 pgbouncer'"
  ssh -i ~/.ssh/key.pem ubuntu@hostname
fi

if [ "$1" == "ssh" ]; then
  ssh -i ~/.ssh/key.pem ubuntu@hostname
fi

