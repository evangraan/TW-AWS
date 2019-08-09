#!/bin/bash

if [ "$1" == "" ]; then
  echo "Usage: create-resource.sh ResourceName"
  exit -1
fi

NAME=$1
RESULT=$(aws apigateway create-resource --rest-api-id tfbh6s5q9c --parent-id r5jdomwxbf --path-part $NAME)
ID=$(echo $RESULT | cut -d '"' -f12)
aws apigateway put-method --rest-api-id tfbh6s5q9c --resource-id $ID --http-method GET --authorization-type "NONE" --no-api-key-required --request-parameters "method.request.header.custom-header=false"
aws apigateway put-method --rest-api-id tfbh6s5q9c --resource-id $ID --http-method POST --authorization-type "NONE" --no-api-key-required --request-parameters "method.request.header.custom-header=false"
