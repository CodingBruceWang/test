#!/bin/bash
. ./server_ips.sh

server_ips=${server_ips}
server_ips=(${server_ips//,/ }) 

for ip in ${server_ips[*]}
do
  echo $ip
  scp server_ips.sh $ip:/home/wfq/test
done
