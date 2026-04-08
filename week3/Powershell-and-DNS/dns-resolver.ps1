param ($network_prefix, $dns_server)
Write-Host "ip, resolved name"
for ($i=1; $i -lt 254; $i++) {
    $ip = "$network_prefix.$i"
    $hostname = Resolve-DnsName -DnsOnly $ip -Server $dns_server -ErrorAction Ignore
    if ($hostname.NameHost) {
        Write-Host "$ip $($hostname.NameHost)"
    }
}