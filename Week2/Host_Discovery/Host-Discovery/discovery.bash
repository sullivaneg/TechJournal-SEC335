for ip in $(seq 2 50); do ping -c 1 -W 0.5 10.0.5.$ip \
| grep "64 bytes from" | grep -o -E "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}" \
 >> sweep.txt; done
