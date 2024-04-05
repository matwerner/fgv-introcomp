echo "E-mails?"
email_regex="^([a-z]|[0-9]|[_-])+@[a-z]+\.([a-z]{2,3}){1,2}$"
grep -c -E  "${email_regex}" ../registros.txt
grep -E -o "${email_regex}" ../registros.txt
echo

echo "Telefones?"
phone_regex="^(\+55 )?(\(?[0-9]{2,3}\)?)? *[0-9]?(-| )?[0-9]{4}(-| )?[0-9]{4}$"
grep -c -E  "${phone_regex}" ../registros.txt
grep -E -o "${phone_regex}" ../registros.txt
echo

echo "Datas de Nascimento?"
date_regex="^[0-9]{2}[-/][0-9]{2}[-/][0-9]{4}$"
grep -c -E  "${date_regex}" ../registros.txt
grep -E -o "${date_regex}" ../registros.txt
echo

echo "CPFs?"
cpf_regex="^[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}$"
grep -c -E  "${cpf_regex}" ../registros.txt
grep -E -o "${cpf_regex}" ../registros.txt
echo

echo "IP's?"
ip_regex="^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$"
grep -c -E  "${ip_regex}" ../registros.txt
grep -E -o "${ip_regex}" ../registros.txt
echo
