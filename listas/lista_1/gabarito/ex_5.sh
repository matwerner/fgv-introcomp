numbers=$(cat ../numeros.txt)

# MENOR

min_number=10000
for number in $numbers; do
	if [ $number -lt $min_number ]; then
		min_number=${number}
	fi
done
echo "Menor número: ${min_number}"

# MAIOR

max_number=-1
for number in $numbers; do
	if [ $number -gt $max_number ]; then
		max_number=${number}
	fi
done
echo "Maior número: ${max_number}"

# MÉDIA

cumulative_sum=0
n=0
for number in $numbers; do
	cumulative_sum=$((cumulative_sum + number))
	n=$((n+1))
done
# Opção A: Divisão inteira
echo "Média (Opção A): $((cumulative_sum / n))"
# Opção B: Divisão com n casas decimais
echo "Média (Opção B): $( echo "scale=2; ${cumulative_sum} / ${n}" | bc -l)"
