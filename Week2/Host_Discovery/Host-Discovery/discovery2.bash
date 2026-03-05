for i in $(seq 2 50);
do
res=$(nmap -n -vv -sn "${1}.${i}" | grep "1 host up" | head -n 1);

if [ ! -z "$res" ] 
then
	echo "${1}.${i}"
fi

done
