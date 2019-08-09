#!/bin/bash

if [ "$1" == "" ]; then
  echo "Usage: bilk-lambda.sh Action"
  echo "Takes all lambda names from the TWAPI list and performs an action on them"
  echo "Action can be one of:"
  echo "  -c Create a new lambda"
  echo "  -u Update an existing lambda"
  exit -1
fi

NAME=$1
for f in $(cat TWAPI | tr -s ' ' '_' | cut -d '_' -f1); do
  if [ "$1" == "-c" ]; then
    mkdir $f
    cp TWGetGalaxy/app.py $f/
  fi  
  ./lambda.sh $f $1
done
