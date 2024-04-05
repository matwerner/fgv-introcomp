num=$1

divisor=1
while [ ${divisor} -le ${num} ]; do
	remainder=$((num % divisor))
	if [ ${remainder} -eq 0 ]; then
		echo ${divisor}
	fi
	divisor=$((divisor+1))
done