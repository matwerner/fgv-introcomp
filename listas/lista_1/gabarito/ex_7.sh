filepath1=$1
filepath2=$2

content1=$(cat ${filepath1})
content2=$(cat ${filepath2})

if [ "${content1}" = "${content2}" ]; then
	echo "Arquivos são iguais"
else
	echo "Arquivos são diferentes"
fi