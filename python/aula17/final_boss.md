# Exercícios (Em construção)

Lista de exercícios em preparação para A2.

## 1. Similaridade de Jaccard entre Textos

A similaridade de Jaccard é uma medida de similaridade entre dois conjuntos, muito utilizada para comparar textos, 
definida como:

$$ S_{Jaccard}(A, B) = \frac{|A \cap B|}{|A \cup B|} $$

onde:
- $|A \cap B|$ é o número de elementos na interseção dos conjuntos $A$ e $B$,
- $|A \cup B|$ é o número de elementos na união dos conjuntos $A$ e $B$.

Considere os seguintes textos:

**Texto 1:** "O gato está no telhado."

**Texto 2:** "O gato dorme no telhado."

### Perguntas:

A. Quais são os conjuntos de palavras únicos para cada texto após a padronização (remover pontuações e transformar todas as palavras para letras minúsculas)?

B. Quantos elementos estão na interseção dos dois conjuntos?

C. Quantos elementos estão na união dos dois conjuntos?

D. Qual é a similaridade de Jaccard entre os dois textos?

## 2. Deteção de Colisão de circulos

Escreva um programa em Python que determine se dois círculos em um plano bidimensional colidem. Cada círculo é definido por uma tupla contendo as coordenadas do seu centro e o seu raio (x, y, r). O programa deve ler as informações dos dois círculos e imprimir "Colidem" se os círculos se sobrepõem ou "Não colidem" se não se sobrepõem.

Dicas:
* A distância entre os centros dos dois círculos pode ser calculada usando a fórmula da distância euclidiana.
* Dois círculos colidem se a soma dos seus raios for maior ou igual à distância entre os seus centros.

### Exemplos:

```python
circulo1 = (1, 1, 2)
circulo2 = (4, 5, 3)
resultado = detectar_colisao(circulo1, circulo2)
print(resultado) # Não colidem

circulo1 = (0, 0, 5)
circulo2 = (3, 4, 2)
resultado = detectar_colisao(circulo1, circulo2)
print(resultado) # Colidem
```

## 3. Cidade mais próxima

Considere o seguinte cenário de determinação da cidade mais próxima num mapa 2D.
Você deve escrever um programa em Python que determine qual cidade está mais próxima de cada pessoa,
com base em suas coordenadas e nas localizações das cidades.

**Descrição:**

Você receberá dois dicionários:
1. Um dicionário representando as pessoas, onde as chaves são os nomes das pessoas e os valores são as coordenadas 2D representadas por uma tupla (x, y).
2. Um dicionário representando as cidades, onde as chaves são os nomes das cidades e os valores são as coordenadas 2D representadas por uma tupla (x, y).

Para cada pessoa, você deve determinar qual cidade está mais próxima.

**Dicas**:
* Para determinar a cidade mais próxima de uma pessoa, utilize a fórmula da distância euclidiana entre dois pontos:
$$distancia = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$
* Compare essa distância entre a pessoa e todas as cidades para determinar a mais próxima.

### Exemplos

```python
# Dicionário de coordenadas das pessoas
pessoas = {'Alice': (1, 2), 'Bob': (3, 4), 'Charlie': (6, 8), 'David': (10, 10)}

# Dicionário de coordenadas das cidades
cidades = {'A': (2, 3), 'B': (5, 5), 'C': (9, 9)}

# Chamada da função
cidades_proximas = cidade_mais_proxima(pessoas, cidades)

# Saída esperada
print(cidades_proximas)  # Deve retornar {'Alice': 'A', 'Bob': 'A', 'Charlie': 'C', 'David': 'C'}
```

## 4. Histograma

Desenvolva um programa em Python que receba uma lista de números inteiros e crie $5$ intervalos equidistantes.
O programa deve atribuir cada valor da lista a um desses intervalos e imprimir a frequência de valores em cada intervalo.

Escreva uma função chamada `freq_intervalos(lista)` que receba como entrada uma lista de números inteiros e implemente a lógica descrita acima.
A função deve retornar um dicionário onde as chaves são os intervalos e os valores são as frequências de valores presentes nesses intervalos.

**Dicas:**
* Os intervalos serão sempre inteiros (Logo, utilizar divisão inteira `//``);
* Os intervalos exibidos devem incluem ambos os lados. Isto é ``[5-23]`` contem todos os números de 5 até 23.

### Exemplos

```python
lista_numeros = [70, 5, 12, 40, 55, 27, 33, 20, 63, 94, 88, 99]
resultado = freq_intervalos(lista_numeros)
print(resultado)
#  {
#     '5-23': 3,
#     '24-42': 3,
#     '43-61': 1,
#     '62-80': 2,
#     '81-99': 3
# }
```

## 5. Colisão de intervalos

Considere um programa que encontra todas as colisões entre os intervalos de números inteiros em uma lista de intervalos.
Cada intervalo é representado por uma lista de dois elementos, onde o primeiro elemento é o início do intervalo e o segundo é o fim.

Escreva um algoritmo em Python que recebe uma lista de intervalos e retorna uma lista de tuplas, onde cada tupla contém os nomes dos intervalos que têm interseção.

Por exemplo, dado o dicionário de intervalos:

```python
intervalos = {'A': (1, 5), 'B': (3, 7), 'C': (7, 10), 'D': (15, 18)}
resultado = encontrar_colisoes(intervalos)
print(resultado) # [('A', 'B'), ('B', 'C')]
```

Sua tarefa é implementar a função `encontrar_colisoes(intervalos)` que recebe como argumento intervalos, um dicionário onde as chaves são os nomes dos intervalos e os valores são listas representando os intervalos, e retorna uma lista de tuplas contendo os nomes dos intervalos que têm colisão.

## 6. Criar Matriz com Diferentes Orientações

Escreva um programa em Python que crie uma matriz $5x5$ e
preencha com números de $1$ a $25$ de três formas diferentes:\
A. No sentido horizontal;\
B. No sentido vertical;\
C. Em zique-zaque (zig zag scan).

```python
A. 
1  2  3  4  5
6  7  8  9  10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25

B. 
1  6  11 16 21
2  7  12 17 22
3  8  13 18 23
4  9  14 19 24
5  10 15 20 25

C.
1  3   6 10 15
2  5   9 14 19
4  8  13 18 22
7  12 17 21 24
11 16 20 23 25
```

## 7. Infecção numa matrix 2D

Você é responsável por desenvolver um programa que determine a propagação de infecções em um mundo representado por uma matriz 2D.
O mundo é representado por uma matriz de inteiros de dimensão $m × n$, onde cada célula pode ser saudável `(0)` ou infectada `(1)`.
Além disso, você recebe uma lista de polos de infecção, cada um representado por uma tupla $(x,y,r)$,
onde $(x,y)$ são as coordenadas do polo de infecção e $r$ é o raio de infecção.
Uma célula é considerada infectada se estiver dentro do raio $r$ de qualquer polo de infecção.

**Entrada**
* Um inteiro $m$ representando o número de linhas da matriz.
* Um inteiro $n$ representando o número de colunas da matriz.
* Uma lista de polos de infecção, onde cada polo é representado por uma tupla $(x,y,r)$.

Restrições
* $1 \le m,n \le 100$
* $0 \le x \lt m$
* $0 \le y \lt n$
* $0 \le r \le min⁡(m,n)$

**Saída**

A matriz 2D resultante após a propagação da infecção, onde células infectadas são marcadas com 1.

## Exemplo

```python
m = 5
n = 5
polos_de_infeccao = [(2, 2, 1), (4, 4, 2)]
resultado = propagar_infeccao(m, n, polos_de_infeccao)
print(resultado)
# 0 0 0 0 0
# 0 1 1 1 0
# 0 1 1 1 0
# 0 1 1 1 1
# 0 0 1 1 1
```

## 8. Mover Rainha

Implemente um programa em Python que simule o movimento de uma rainha no tabuleiro de xadrez.
A posição inicial da rainha é fornecida e o programa deve retornar uma matriz $8x8$,
onde $1$ representa as posições que a rainha pode alcançar e $0$ representa as posições que a rainha não pode alcançar.

Desenvolva uma função chamada `movimentos_rainha` que receba a posição inicial da rainha no formato de tupla (`linha`, `coluna`),
onde linha e coluna são inteiros entre $1$ e $8$ que representam a posição da rainha no tabuleiro de xadrez.
A função deve retornar uma matriz $8x8$ (lista de listas) preenchida com $0s$ e $1s$ conforme descrito acima.

Regras:
* A rainha pode se mover qualquer número de casas ao longo de uma linha, coluna ou diagonal.
* As posições no tabuleiro são representadas por números de $1$ a $8$ tanto para linhas quanto para colunas.

### Exemplo

```python
posicao_inicial = (4, 4)
resultado = movimentos_rainha(posicao_inicial)
print(resultado)
# [[0, 0, 0, 1, 0, 0, 0, 1],
#  [0, 0, 1, 0, 1, 0, 1, 0],
#  [0, 1, 0, 1, 0, 1, 0, 1],
#  [1, 0, 1, 1, 1, 1, 1, 1],
#  [0, 1, 0, 1, 0, 1, 0, 1],
#  [0, 0, 1, 0, 1, 0, 1, 0],
#  [0, 0, 0, 1, 0, 0, 0, 1],
#  [0, 0, 0, 0, 1, 0, 0, 0]]
```

## 9.Encaixar peças batalha naval

Você foi contratado para desenvolver um programa que auxilia na montagem de um tabuleiro de batalha naval. O programa deve ser capaz de encaixar as peças de um jogo de batalha naval em um tabuleiro 2D, verificando se as peças cabem nas posições desejadas sem sobreposição.

Considere as seguintes especificações:

* O tabuleiro é representado por uma matriz 2D de tamanho $n×n$, onde cada célula pode estar vazia ou ocupada por parte de uma peça.
* Cada peça tem um tamanho específico e pode ser posicionada horizontalmente ou verticalmente.
* As peças não podem se sobrepor e não podem ficar parcialmente fora do tabuleiro.
* A entrada do programa consiste em:
    * Um inteiro $n$ representando o tamanho do tabuleiro.
    * Uma lista de peças, onde cada peça é representada por uma tupla $(tamanho,orientacao,linha,coluna)$, sendo:
        * **tamanho**: um inteiro representando o tamanho da peça.
        * **orientacao**: uma string "H" para horizontal ou "V" para vertical.
        * **linha**: um inteiro representando a linha inicial para posicionamento da peça.
        * **coluna**: um inteiro representando a coluna inicial para posicionamento da peça.

**Tarefa**:

Implemente a função `montar_tabuleiro(n, pecas)` que receba um inteiro $n$ e uma lista de peças conforme descrito acima, e retorne a matriz representando o tabuleiro após encaixar todas as peças, ou `None` se alguma peça não puder ser encaixada corretamente.

**Regras**:
* Se uma peça não puder ser encaixada devido a sobreposição ou por estar fora do tabuleiro, o programa deve retornar `None`.
* Cada peça deve ser representada por um número único no tabuleiro para identificar facilmente sua posição.

### Exemplos

```python
n = 5
pecas = [(3, "H", 1, 1), (1, "V", 0, 3), (4, "H", 2, 0)]
resultado = montar_tabuleiro(n, pecas)
print(resultado)
# [
#   [0, 0, 0, 2, 0],
#   [0, 1, 1, 1, 0],
#   [3, 3, 3, 3, 0],
#   [0, 0, 0, 0, 0],
#   [0, 0, 0, 0, 0]
# ]
```

## 10. Alinhar palavras à direita

Elabore um programa em Python que alinhe à direita uma lista de palavras.
O programa deve receber uma lista de palavras e imprimir cada palavra alinhada à direita,
considerando o comprimento da palavra mais longa na lista. Considere o seguinte exemplo de entrada e saída:

```python
palavras = ["gato", "cachorro", "coelho"]
alinhar_direita(palavras)
#     gato
# cachorro
#   coelho
```

## 11. Série de Harshad

Implemente um programa em Python que gere e imprima os primeiros $n$ números da série de Harshad (ou Niven).
Um número é considerado um número de Harshad se ele for divisível pela soma de seus dígitos.
O seu programa deve ler o valor de $n$ do usuário e, em seguida, imprimir os primeiros $n$ números da série de Harshad.

**Dicas**
* Utilize uma função para calcular a soma dos dígitos de um número.
* Utilize um loop para encontrar os números de Harshad e armazene-os em uma lista até que a lista contenha $n$ elementos.

## 12. Validar CPF

Um CPF (Cadastro de Pessoas Físicas) é composto por 11 dígitos numéricos,
geralmente apresentados no formato "XXX.XXX.XXX-YY".
Para ser considerado válido, um CPF deve atender aos seguintes critérios:

1. Deve conter 11 dígitos numéricos.
2. Não deve consistir de todos os dígitos iguais (por exemplo, "111.111.111-11" não é um CPF válido).
3. Deve obedecer ao algoritmo de validação do CPF, descrito a seguir:
    * Os primeiros 9 dígitos são os números base.
    * O 10º dígito (primeiro dígito verificador) é calculado da seguinte forma:
        * Multiplique os 9 primeiros dígitos pela sequência decrescente de 10 a 2.
        * Some os resultados dessas multiplicações.
        * Calcule o resto da divisão dessa soma por 11.
        * Se o resto for menor que 2, o dígito verificador é 0. Se for maior ou igual a 2, o dígito verificador é 11 menos o resto.
    * O 11º dígito (segundo dígito verificador) é calculado da mesma forma, mas agora com a sequência decrescente de 11 a 2 (considerando os 9 dígitos base mais o primeiro dígito verificador).

Implemente a função `valida_cpf(cpf: str) -> bool` que recebe uma string representando o CPF no formato "XXX.XXX.XXX-YY"
e retorna um valor booleano indicando se o CPF é válido ou não.

### Exemplos

```python
print(valida_cpf("123.456.789-14"))  # Deve retornar False
print(valida_cpf("111.444.777-35"))  # Deve retornar True
```

## 13. Validar código de barras no formato EAN-13

Desenvolva um programa em Python que valide códigos de barras no formato EAN-13. O programa deve seguir os seguintes passos:

1. Receber um código de barras EAN-13 como entrada.
2. Calcular o dígito verificador com base nos primeiros 12 dígitos do código fornecido.
3. Comparar o dígito verificador calculado com o 13º dígito fornecido.
4. Informar se o código de barras é válido ou inválido.

**Regras para cálculo do dígito verificador:**

O dígito verificador (13º dígito) é calculado da seguinte forma:
* Some todos os dígitos ímpares da posição 1 até 11.
* Some todos os dígitos pares da posição 2 até 12 e multiplique a soma por 3.
* Some os dois resultados obtidos.
* Encontre o múltiplo de 10 mais próximo maior ou igual ao resultado obtido.
* Subtraia o resultado obtido do múltiplo de 10 encontrado. O resultado é o dígito verificador.

Exemplo:

Para o código de barras 4006381333931:

* Os 12 primeiros dígitos são: 400638133393
* A soma dos dígitos ímpares (4 + 0 + 3 + 1 + 3 + 9) = 20
* A soma dos dígitos pares (0 + 6 + 8 + 3 + 3 + 3) = 23, multiplicado por 3 = 69
* Soma total = 20 + 69 = 89
* O múltiplo de 10 mais próximo maior ou igual a 89 é 90.
* Dígito verificador = 90 - 89 = 1

## 14. Subconjuntos

Desenvolva uma função recursiva em Python chamada `gerar_subconjuntos` que receba um conjunto de elementos (representado como uma lista) e retorne uma lista contendo todos os subconjuntos possíveis desse conjunto.

Para isso, siga os passos abaixo:
* Crie a função `gerar_subconjuntos` que recebe uma lista conjunto.
* Utilize recursão para gerar todos os subconjuntos possíveis do conjunto dado.
* Teste a função com o conjunto `[1, 2, 3]` e mostre o resultado.

### Exemplo

```python
resultado = gerar_subconjuntos([1, 2, 3])
print(resultado)
# [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]
```

## 15. Balanceamento de Parênteses

Você foi designado para escrever um programa em Python que verifique se uma string contendo
apenas parênteses `(` e `)` está corretamente balanceada.

Uma string é considerada corretamente balanceada se:
* Cada parêntese de abertura `(` tem um parêntese de fechamento `)` correspondente.
* Parênteses de fechamento `)` nunca aparecem antes de um parêntese de abertura `(` correspondente.

Por exemplo, as strings `()`, `(())`, e `(()())` estão balanceadas, enquanto `)(`, `(()`, e `())(` não estão.

Para isso, escreva uma função recursiva chamada `verifica_balanceamento` que recebe uma string como entrada
e retorna `True` se a string estiver corretamente balanceada e `False` caso contrário.

### Exemplos

```python
print(verifica_balanceamento("()"))     # True
print(verifica_balanceamento("(())"))   # True
print(verifica_balanceamento("(()())")) # True
print(verifica_balanceamento(")("))     # False
print(verifica_balanceamento("(()"))    # False
print(verifica_balanceamento("())("))   # False
```

## 16. Encontrar termos no texto 

Dado o texto abaixo, escreva um programa em Python que receba uma lista de termos e reporte em quais linhas cada termo apareceu.

Texto:

```
Este é o primeiro exemplo de linha.
Esta linha é a segunda linha do exemplo.
O terceiro exemplo está aqui.
Aqui temos a quarta linha de exemplo.
E finalmente, esta é a quinta linha de exemplo.
```

Lista de Termos:

```
linha
exemplo
segunda
quinta

```

Requisitos do Programa:
* O programa deve ler o texto e a lista de termos.
* Para cada termo da lista, o programa deve identificar e imprimir em quais linhas (números das linhas) o termo aparece.
* A numeração das linhas deve começar de 1.

### Saída esperada
```
Termo 'linha' aparece nas linhas: 1, 2, 4, 5
Termo 'exemplo' aparece nas linhas: 1, 2, 3, 4, 5
Termo 'segunda' aparece na linha: 2
Termo 'quinta' aparece na linha: 5
```

## 17. Contar palavras em arquivo

Você deve desenvolver um programa em Python que leia um arquivo de texto e realize as seguintes tarefas:

* Contar o número total de palavras contidas no arquivo.
* Listar as 5 palavras mais frequentes no arquivo.
* Listar as 5 sequências de duas palavras mais frequentes no arquivo.

Para a contagem das palavras e sequências:
* Desconsidere diferenças entre maiúsculas e minúsculas (ou seja, trate todas as palavras como se fossem minúsculas).
* Remova pontuações e outros caracteres especiais para garantir a precisão das contagens.

**Bonus:** Refazer a questão considerando caracteres em vez de palavras.

### Exemplo

```python
texto = "A programação em Python é divertida. A programação é poderosa e simples. Python é uma linguagem versátil."
obter_estatisticas(texto)
# Número total de palavras: 15

# Top 5 palavras mais frequentes:
# 1. é: 3
# 2. a: 2
# 3. programação: 2
# 4. python: 2
# 5. em: 1

# Top 5 sequências de duas palavras mais frequentes:
# 1. a programação: 2
# 2. python é: 2
# 3. programação em: 1
# 4. em python: 1
# 5. é divertida: 1
```

## 18. Processar dados de dois CSVs

Suponha que você precise criar um programa em Python que leia dados de dois arquivos CSV e realize uma operação de junção (merge) baseada em uma coluna chave comum. Os arquivos CSV são alunos.csv e notas.csv, e ambos possuem uma coluna chamada id_aluno, que será usada como chave para a junção.

O arquivo alunos.csv contém as seguintes colunas:
* id_aluno
* nome
* curso

O arquivo notas.csv contém as seguintes colunas:

* id_aluno
* disciplina
* nota

Escreva um programa em Python que:

* Leia os dados dos arquivos alunos.csv e notas.csv.
* Realize uma junção (merge) entre os dados, utilizando a coluna id_aluno como chave.
* Exiba o resultado da junção em formato tabular.

**Dicas**:
* Certifique-se de que o resultado final contenha todas as colunas de ambos os arquivos.
* **NÃO** é permitido utilizar a biblioteca `pandas`.

### Exemplo

Alunos.csv:

```r
id_aluno,nome,curso
1,Alice,Engenharia
2,Bob,Medicina
3,Carol,Direito
```

Notas.csv:
```r
id_aluno,disciplina,nota
1,Matemática,85
1,Física,90
2,Biologia,78
3,Direito Constitucional,88
```

Saída esperada:
```r
   id_aluno   nome       curso              disciplina  nota
0         1  Alice  Engenharia              Matemática    85
1         1  Alice  Engenharia                  Física    90
2         2    Bob    Medicina                Biologia    78
3         3  Carol     Direito  Direito Constitucional    88
```

## 19. Expandir Notação Decimal

Implemente um programa em Python que expanda um número decimal inteiro positivo em sua forma verbal.
O programa deve solicitar ao usuário que insira um número decimal e, em seguida, exibir o número na forma expandida.
Por exemplo, se o usuário inserir o número `1234` o programa deve exibir `1000 + 200 + 30 + 4`.

**Dicas:**
* Utilize operações de divisão inteira e módulo para separar cada dígito do número.
* Considere o valor posicional de cada dígito (unidade, dezena, centena, milhar, etc.) ao construir a forma expandida.

**Restrições:**
* O número inserido pelo usuário deve ser um inteiro positivo.
* O programa deve lidar corretamente com números que contenham zeros em qualquer posição
(por exemplo, `1024` deve ser expandido para `1000 + 20 + 4`).

## 20. Cifra de Cesar

A cifra de César é um método de criptografia que desloca cada letra de uma mensagem um número fixo de posições ao longo do alfabeto.
Por exemplo, com uma chave de deslocamento de $3$, a letra `'A'` se torna `'D'`, `'B'` se torna `'E'`, e assim por diante.
Para decodificar a mensagem, cada letra é deslocada de volta o mesmo número de posições.

Desenvolva um programa em Python que decodifique uma mensagem criptografada utilizando a cifra de César.
O programa deve aceitar uma string criptografada e uma chave de deslocamento, retornando a mensagem original.
Utilize a especificação a seguir:
* A função deve ser chamada `decodificar_cifra_cesar`.
* A função deve receber dois parâmetros:
    * mensagem_criptografada (uma string) que representa a mensagem a ser decodificada.
    * chave (um inteiro) que representa o número de posições que cada letra foi deslocada na criptografia.
* A função deve retornar uma string com a mensagem original decodificada.

**Dicas:**
* A função deve lidar apenas com letras minúsculas e deve preservar espaços e outros caracteres não alfabéticos.
* Para converter uma letra em um número, utilizar a função `ord()`
* Para converter um número em uma letra, utilizar a função `chr()`

### Exemplos

```python
mensagem_criptografada = "fdhvdu"
chave = 3
resultado = decodificar_cifra_cesar(mensagem_criptografada, chave)
print(resultado) # "caesar"
```
