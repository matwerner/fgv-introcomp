echo "a. Troque a palavra 'teste' por 'verificação';"
sed "s/teste/verificação/g" ../grep_sed.txt
echo
echo

echo "b. Delete as linhas contendo a palavra 'linha' e variações;"
sed -E "/linhas?/Id" ../grep_sed.txt
echo
echo

echo "c. Remova todos os artigos (o, a, os, as) do texto;"
sed -E "s/\b(o|a|os|as)\b//g" ../grep_sed.txt
echo
echo

echo "d. Introduza um texto no inicio da linha;"
sed -E "s/^/OI! /g" ../grep_sed.txt
echo
echo

echo "e. Introduza um texto no final da linha;"
sed -E "s/$/ TCHAU!/g" ../grep_sed.txt
echo
echo

echo "f. Delete linhas em branco;"
sed -E "/^$/d" ../grep_sed.txt
echo
echo

echo "g. Retire todos os acentos (Exemplo: é -> e ou ã -> a)"
sed -E "y/éã/ea/" ../grep_sed.txt
echo
echo

echo "h. Pegue todas os termos entre 'Linha com a palavra' e '.'"
grep "Linha com a palavra " ../grep_sed.txt | sed -E "s/Linha com a palavra (.*)\./\1/g"
