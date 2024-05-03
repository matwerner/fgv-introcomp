# Lista de Exercícios 1

**Q1**.
Escreva um programa que encontre todos os números que são divisíveis por $7$, mas não são múltiplos de $5$,
entre $2.000$ e $3.200$ (ambos incluídos).\
Os números obtidos devem ser impressos em sequência separada por vírgula em uma única linha.

**Q2**.
Dado um número $n$, escreva um programa para gerar um dicionário que contenha $(i, i*i)$, aonde $i$ é a chave e $i*i$ é o valor, para todo $\forall i  \in \{1, \dots, n\}$.\
Depois, o programa deverá imprimir o dicionário no terminal.

Exemplo :
```python
Entrada: n = 8
Saída: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
```


**Q3**.
Escreva um programa que receba 2 números, $X$ e $Y$, como entrada e gere uma matriz bidimensional.\
O valor do elemento na $i$-ésima linha e $j$-ésima coluna da matriz deve ser i*j. 

**Observação 1**:\
$i \in \{0, 1, \dots, X-1\}$;
$j \in \{0, 1, \dots. Y-1\}$.

**Observação 2**:\
Assuma que os valores $X$ e $Y$ serão passados como uma entrada do console em formato separado por vírgula.

Exemplo:
```python
Entrada: 3,5
Saída: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
```


**Q4**.
Escreva um programa que receba uma lista de palavras separadas por virgula como entrada e
imprima essas mesmas palavras ordenadas alfabeticamente em uma sequência separada por vírgula. 

Exemplo :
```
Entrada: ola,mundo,como,vai
Saída: como,mundo,ola,vai
```

**Q5**
Escreva um programa que aceite uma sequência de palavras separadas por espaços em branco como entrada
e imprima as palavras após remover todas as palavras duplicadas e ordená-las alfanumericamente. 

Exemplo :
```
Entrada: ola mundo como vai ola mundo novamente
Saída: como mundo novamente ola vai
```


**Q6**.
Escreva um programa para verificar se uma senha passada como entrada, atende aos seguintes critérios:
A seguir estão os critérios para verificar a senha:

1. Pelo menos 1 letra entre [a-z]
2. Pelo menos 1 número entre [0-9]
3. Pelo menos 1 letra entre [A-Z]
4. Comprimento mínimo: 6
5. Comprimento máximo: 12

Seu programa deve aceitar uma sequência de senhas separadas por vírgula e irá verificá-las de acordo com os critérios acima.
Senhas que correspondem aos critérios devem ser impressas, cada uma separada por uma vírgula.

Exemplo:
```
Entrada: ABd1234@1,a F1#,2w3E*,2We3345
Saída: ABd1234@1
```

## Extras

**E1**.
Compare o desempenho de buscas por termos específicos em uma lista (list) e em um conjunto (set).

Para isso, escreva um programa que gere uma lista de **strings** contendo todos os digitos de $1$ até $N$.\
A partir dai, crie dois scripts que armaze esses dados como uma lista e como um conjunto, respectivamente, e procure pelos mesmos termos.\
Isto é, se $N = 5$ , crie uma lista  $A = [1,2,3,4,5]$ e, em seguida, verifique se $1, \dots, 5$ estão nessa lista.

Para medir o tempo computacional, utilize a função **time** do linux:
```bash
time python meu_programa.py
```

Repita esse procedimento para $N = \{10, 1.000, 100.000\}$.

Após executar o programa, responda às seguintes perguntas:

a) Como o valor de $N$ afeta o tempo de busca utilizando ambas as estruturas de dados?

b) Qual estrutura de dados você recomendaria para armazenar e buscar grandes volumes de dados?

**E2**.
Dado o texto a seguir:

    "Algoritmos são a base da programação. A lógica e a estrutura de dados são fundamentais para criar sistemas eficientes e robustos.
    A prática constante é essencial para aprimorar as habilidades de programação e resolver problemas de forma criativa."

a)
Remova as seguintes palavras:
1. algoritmos
2. programação
3. lógica
4. estrutura de dados
5. sistemas

b)
Repita o exercicio anterior, mascarando as palavras em vez de remove-las.
Isto é, troque "sistemas" por "xxxxxxxx".

**E3**. Implemente um programa que permita aos usuários manipular uma lista de números inteiros.
O programa deve apresentar um menu simples no terminal com as seguintes operações:

1. **Adicionar no final**: Permite inserir um novo número inteiro ao final da lista.
2. **Remover do final**: Remove o último número inteiro da lista.
3. **Ordenar**: Ordena os números inteiros na lista em ordem crescente.
4. **Apresentar soma**: Calcula e exibe a soma de todos os números inteiros presentes na lista.
5. **Exibir conteúdo**: Mostra todos os números inteiros atualmente presentes na lista.

Além disso, o programa deve permitir que o usuário pressione ```'q'``` para sair do programa.

**Observação 1**:\
Caso o usuário insira um valor que não seja reconhecido como uma operação válida, o programa deve informar que a opção não é válida e solicitar que o usuário escolha novamente.

**Observação 2**:\
Antes de adicionar um número inteiro à lista, o programa deve verificar se a entrada fornecida pelo usuário contém apenas números inteiros. Se a entrada não for composta apenas de números, o programa deve exibir uma mensagem de erro e solicitar ao usuário que insira um número inteiro válido.

## MAIS EXECÍCIOS

https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt