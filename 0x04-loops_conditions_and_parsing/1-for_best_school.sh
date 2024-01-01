#!/usr/bin/env bash
# a bash script to print a message 10 times
mess="Best School"
i=0
until [ "$i" -eq 10 ]
do
    echo "$mess"
    ((i=i+1))
done 
