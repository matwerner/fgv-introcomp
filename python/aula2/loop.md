# Loops

Loops são estruturas de controle de fluxo em programação que permitem
repetir  a execução de um mesmo bloco de código enquanto 
uma condição específica é verdadeira ou para um número específico de vezes.

## Sintaxe e estrutura

### While

O loop ```while``` é usado para executar um bloco de código repetidamente enquanto uma condição especificada for verdadeira.

```python
# Sintaxe do loop while
while condição:
    # bloco de código a ser repetido enquanto a condição for verdadeira
```

```python
# Exemplo de loop while para imprimir os números de 1 a 5
i = 1
while i <= 5:
    print(i)
    i += 1
```

Obs: Python não possui um loop ```until``` como vimos em bash.
Contudo, o mesmo efeito pode ser obtido em python simplesmente negando a condição do ```while```.

### For

Já loop ```for``` é usado para iterar sobre uma sequência de elementos, 
como uma ```lista```, ```tupla```, ```dicionário``` ou ```intervalo numérico```.
Estruturas de dados que veremos detalhadamente mais para frente.

```python
# Sintaxe do loop for
for elemento in sequencia:
    # bloco de código a ser repetido para cada elemento na sequência
```

```python
# Exemplo de loop for para iterar sobre uma lista de cores
cores = ["vermelho", "verde", "azul"]
for cor in cores:
    print(cor)
```

#### Função Range

No caso do ```intervalo numérico```, a função ```range``` é comumente usada.
Ela permite gerar uma sequência de números em um intervalo específico e é utilizada
em loops for para especificar a quantidade de iterações.

```python
# Sintaxe da função range
range(início, fim, passo)
```

```python
# Exemplo de uso da função range em um loop for
for i in range(1, 6):
    print(i)  # Imprime os números de 1 a 5
```

## Interrompendo o fluxo

Dentro de loops, podemos adicionar as declarações ```break``` e ```continue```
para interromper a execução natural de um bloco de código dentro do loop.

### Break

A declaração break é usada para interromper a execução de um loop antes que ele seja concluído, com base em uma condição específica.
Quando o Python encontra a declaração break, ele sai imediatamente do loop e continua a execução do código após o loop.

```python
for n in range(1, 6):
    if n == 3:
        break
    print(n)
print("Fim!")
```

### Continue

A declaração continue é usada para pular para a próxima iteração do loop, ignorando o restante do código dentro do bloco do loop.
Quando o Python encontra a declaração continue, ele volta para o início do loop e continua com a próxima iteração.

```python
for n in range(1,6):
    if numero % 2 == 0:
        continue
    print(n)
```

## Cuidados

É importante ter cuidado ao usar loops para evitar problemas como loops infinitos.
Um loop infinito ocorre quando a condição de parada nunca é alcançada,
resultando em um programa que continua executando indefinidamente.

```python
while True:
    print("Este é um loop infinito!")
    # Cuidado: Este loop nunca terminará!
```

Outros cuidados comentados para condicionais também são validos aqui, como
evitar aninhamentos excessivos.

## Exercícios

1. Exiba os 20 primeiros números da sequência de Fibonacci
2. Imprima no terminal:\
    a. Uma coluna de 0's com n linhas;\
    b. Uma linha de 0's com m colunas;\
    c. Uma matriz de 0's com n linhas e m colunas.
3. Insera números inteiros e os some até que o usuário digite a letra "q" para encerrar o programa.
