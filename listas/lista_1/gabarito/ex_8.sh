valid_count=0
total_count=0
while read password; do
	has_number=false
	if $(echo ${password} | grep -E -q "[0-9]"); then
		has_number=true
	fi

	has_lowercase=false
	if $(echo ${password} | grep -E -q "[a-z]"); then
		has_lowercase=true
	fi

	has_uppercase=false
	if $(echo ${password} | grep -E -q "[A-Z]"); then
		has_uppercase=true
	fi

	has_min_character=false
	if $(echo ${password} | grep -E -q ".{8,}"); then
		has_min_character=true
	fi

	is_valid=false
	if ${has_number} && ${has_lowercase} && ${has_uppercase} && ${has_min_character}; then
		is_valid=true
		valid_count=$((valid_count+1))
	fi

	total_count=$((total_count+1))

	echo -e "${is_valid}\t| ${password}"
done < "../senhas.txt"

echo "${valid_count} de ${total_count} senhas são validas"