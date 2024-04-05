# Lista de exercicíos 1

## BASH

1. Dado um número como entrada ($1), diga se ele é impar ou par.
2. Dado os 3 lados de um triangulo como entrada ($1, $2 e $3), classifica-lo como Equilátero, Isoceles ou Escaleno;
3. Dado dois números ($1, $2), calcular a soma, subtração, multiplicação e divisão deles
4. Dado um número, imprima todos os seus divisores. Por exemplo, 2, 5 e 10 são divisores de 10;
5. Dado a lista `numeros.txt`, imprima no terminal:
    * O menor número
    * O maior número
    * A média
6. Imprima no terminal:
    * Uma coluna de 0's com n linhas;
    * Uma linha de 0's com m colunas;
    * Uma matriz de 0's com n linhas e m colunas;
7. Dado dois arquivos de entrada, verifique se eles são iguais

## GREP

8. Dado o arquivo `senhas.txt`, contendo uma senha por linha, quantas delas atendem aos critérios específicos abaixo?
    * 8 caracteres no mínimo;
    * Uma letra maiúscula;
    * Uma letra minúscula;
    * Um caracter especial (?@#$%&:;~*+-<>=_).
9. Dado o arquivo `grep_sed.txt`, encontre todas as linhas que:
    * Possuem a palavra "linha";
    * Possuem a palavra "linha" e suas variações (E.g: "linhas", "Linha" ou "Linhas");
    * Comecem com a palavra "linha" e suas variações;
    * Terminam com a palavra "teste.";
    * Não contem a palavra "teste";
    * Contem ao menos um número;
    * Contem ao menos 10 caracters.
10. Dado o arquivo `registros.txt`, quantos
    * E-mails?
    * Telefones?
    * Datas de Nascimento?
    * CPFs?
    * IP's? 

## SED

11. Dado o arquivo "grep_sed.txt", faça as seguintes operações:
    * Troque a palavra "teste" por "verificação";
    * Delete as linhas contendo a palavra "linha" e variações;
    * Remova todos os artigos (o, a, os, as) do texto;
    * Introduza um texto no inicio da linha;
    * Introduza um texto no final da linha;
    * Delete linhas em branco;
    * Retire todos os acentos (Exemplo: é -> e ou ã -> a)
    * Pegue todas os termos entre "Linha com a palavra" e "."