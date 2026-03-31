network_prefix=$1
dns_server=$2

echo "dns resolution for $network_prefix"

for i in {1..254}; do 
  host=$network_prefix.$i
  resolvedIP=$(nslookup $host $dns_server | grep "=")
  
  if [[ -n "$resolvedIP" ]]
  then
    echo $resolvedIP
  fi
done

