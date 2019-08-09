#!/bin/bash

for f in $(cat TWAPI | tr -s ' ' '_' | sed 's/TWGet//g' | sed 's/TWSet//g' | uniq); do
  RESOURCE=$(echo $f | cut -d '_' -f 1 | awk '{print tolower($0)}')
  ./create-resource.sh $RESOURCE
done
