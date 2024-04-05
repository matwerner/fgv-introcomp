n_rows=$1
n_columns=$2

# n linhas (Matriz n x 1)

i=0
while [ ${i} -lt ${n_rows} ]; do
	echo "0"
	i=$((i+1))
done
echo ""

# m colunas (Matriz 1 x m)

j=0
column=""
while [ ${j} -lt ${n_columns} ]; do
	column="${column} 0"
	j=$((j+1))
done
column=$(echo ${column} | sed "s/^ +//g" | sed "s/ +$//g")
echo $column
echo ""

# n linhas x m colunas (Matriz n x m)

i=0
while [ ${i} -lt ${n_rows} ]; do
	j=0
	column=""
	while [ ${j} -lt ${n_columns} ]; do
		column="${column} 0"
		j=$((j+1))
	done
	column=$(echo ${column} | sed "s/^ +//g" | sed "s/ +$//g")
	echo $column
	i=$((i+1))
done
echo ""