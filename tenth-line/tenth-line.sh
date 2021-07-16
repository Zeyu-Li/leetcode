#!/bin/bash

# Read from the file file.txt and output the tenth line to stdout.
input="file.txt"
i=0
while (( i++ < 10 ))
do
  read line
done < $input
echo $line
