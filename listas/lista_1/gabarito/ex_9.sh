echo "a. Possuem a palavra 'linha';"
grep -n "linha" ../grep_sed.txt
echo

echo "b. Possuem a palavra 'linha' e suas variações (E.g: 'linhas', 'Linha' ou 'Linhas');"
grep -n -E -i "linhas?" ../grep_sed.txt
echo

echo "c. Comecem com a palavra 'linha' e suas variações;"
grep -n -E -i "^linhas?" ../grep_sed.txt
echo

echo "d. Terminam com a palavra 'teste.';"
grep -n -E "teste\.$" ../grep_sed.txt
echo

echo "e. Não contem a palavra 'teste';"
grep -n -v "teste" ../grep_sed.txt
echo

echo "f. Contem ao menos um número;"
grep -n -E "[0-9]" ../grep_sed.txt
echo

echo "g. Contem ao menos 40 caracters."
grep -n -E ".{40,}" ../grep_sed.txt
echo
