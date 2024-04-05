num=$1
remainder=$((num % 2))
if [ ${remainder} -eq 0 ]; then
	echo "${num} é par"
else
	echo "${num} é impar"
fi