#!/usr/bin/bash

echo "run at startup" >> /tmp/startup.txt

while getopts ":n:" flag
do
	case "${flag}" in
		n) sender=${OPTARG};;
	esac
done
echo "number of senders $sender" >> /tmp/startup.txt

sudo apt update
sudo apt install -y openvswitch-switch
sudo ovs-vsctl add-br br0

for i in $(seq 1 $sender);
do
	echo "$i"
	# maybe should add "2>> /tmp/startup.txt" to analyse potential errors
	ifconfig eth$i 0 
	sudo ovs-vsctl add-port br0 eth$i
done

sudo ovs-vsctl set-fail-mode br0 standalone

sudo ovs-vsctl show >> /tmp/startup.txt
