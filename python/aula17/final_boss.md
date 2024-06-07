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

# A ser melhor especificado

7. (Matriz 2D) Infecção numa matrix 2D
Crie um programa que, dada uma matriz 2D representando um mundo e uma lista de polos de infecção representados por tuplas (x, y, r), verifique quais células na matriz serão infectadas. Uma célula é infectada se estiver dentro do raio r de qualquer polo de infecção.

8. (Matriz 2D) Mover Rainha
Implemente um programa em Python que simule o movimento de uma rainha no tabuleiro de xadrez. A posição inicial da rainha é fornecida e o programa deve listar todas as posições que a rainha pode alcançar.

9. (Matriz 2D) Encaixar peças batalha naval
Desenvolva um programa para encaixar peças de um jogo de batalha naval em um tabuleiro 2D. O programa deve verificar se as peças cabem nas posições desejadas sem sobreposição.

10. (Texto) Alinhar palavras à direita
Escreva um programa que alinhe à direita uma lista de palavras de diferentes comprimentos. Por exemplo, dado a lista ["gato", "cachorro", "coelho"], o programa deve imprimir:

    ```
        gato
    cachorro
      coelho
    ```

11. (Sequencia) Harshad or Niven series
Implemente um programa que gere e imprima os primeiros n números da série de Harshad (ou Niven), onde cada número é divisível pela soma de seus dígitos.

12. (Validação) Validar CPF
Escreva um programa para validar números de CPF. O programa deve verificar se o CPF fornecido segue a estrutura e as regras de formação válidas.

13. (Validação) Validar código de barras no formato EAN-13
Desenvolva um programa para validar códigos de barras no formato EAN-13. O programa deve calcular o dígito verificador e compará-lo com o fornecido.

14. (Recursão) Subconjuntos
Crie um programa em Python que gere todos os subconjuntos possíveis de um conjunto dado utilizando recursão.

15. (Recursão) Checar Balanceamento de Parênteses
Escreva um programa recursivo que verifique se uma string contendo parênteses está corretamente balanceada.

16. (Leitura) Contar palavras em arquivo
Desenvolva um programa que leia um arquivo de texto e conte o número total de palavras contidas nele.

17. (Leitura) Encontrar termos no texto
Escreva um programa que procure por uma lista de termos fornecidos em um arquivo de texto e reporte quantas vezes cada termo aparece.

18. (Leitura) Processar dados de dois CSVs
Crie um programa que leia dados de dois arquivos CSV e realize uma operação de junção (merge) baseada em uma coluna chave comum.

19. (Outros) Expandir Notação Decimal
Implemente um programa que expanda um número decimal em sua forma verbal. Por exemplo, 1234 deve ser expandido para "1000 + 200 + 30 + 4".

20. (Outros) Decodifique uma mensagem utilizando Caesar Cipher
Escreva um programa que decodifique uma mensagem criptografada utilizando a cifra de César. O programa deve aceitar uma string criptografada e uma chave de deslocamento e retornar a mensagem original. Por exemplo, para a mensagem "fdhvdu" e a chave 3, o programa deve retornar "caesar".