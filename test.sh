#!/usr/bin/bash

#echo "run at startup" > /tmp/startup.txt

while getopts ":n:" flag
do
	case "${flag}" in
		n) sender=${OPTARG};;
	esac
done
echo "number of senders $sender" > sender.txt

# option 1
#for (( i=1; i<=$sender; i++ ))

# option 2
for i in $(seq 0 $sender);
do
	echo "$i"
	ifconfig eth$i
done

