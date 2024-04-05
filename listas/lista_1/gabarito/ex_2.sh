a=$1
b=$2
c=$3

is_equal_ab=false
if [ ${a} -eq ${b} ]; then
	is_equal_ab=true
fi

is_equal_ac=false
if [ ${a} -eq ${c} ]; then
	is_equal_ac=true
fi

is_equal_bc=false
if [ ${b} -eq ${c} ]; then
	is_equal_bc=true
fi

if ${is_equal_ab} && ${is_equal_ac}; then
	echo "Triangulo é equilatero"
elif ${is_equal_ab} || ${is_equal_bc} || ${is_equal_ac}; then
	echo "Triangulo é isósceles"
else
	echo "Triangulo é escaleno"
fi