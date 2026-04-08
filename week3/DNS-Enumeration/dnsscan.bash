#! /bin/bash

network_prefix=$1
port=$2

echo "ip,port"
for i in {1..254}; do
    host=$network_prefix.$i
    timeout .1 bash -c "echo >/dev/tcp/${host}/${port}" 2>/dev/null && echo $host,$port
done
