# Comprehension

Em Python temos existem construções sintáticas que permitem a construção de sequências de maneira mais clara e concisa.
São elas:

* list comprehension
* set comprehension
* dict comprehension

## List comprehension

Uma list comprehension é uma maneira concisa de construir uma lista preenchida.
Um uso comum é construir uma nova lista onde cada elemento é o resultado de 
alguma expressão aplicada a cada membro de outra sequência ou iterável, 
ou para construir uma subsequência cujos elementos satisfazem uma certa condição.

Ela irá seguir um modelo: 

```python
lista = ["expressão" for "elemento" in "sequência" if "condição"]
```

Vejamos o código abaixo:

```python
cubos = []
for elementos in range(10):
    cubos.append(elementos**3)
print(cubos)
```

Podemos reescrevê-lo de forma mais concisa utilizando a list comprehension:

```python
cubos2 = [elementos**3 for elementos in range(10)]
print(cubos2)
```

A seguir temos mais um exemplo da conversão para a list comprehension.

De:

```python
lista = []
for x in range(1001):
    if x%5==0 or x%3==0:
        lista.append(x**2)
print(sum(lista))
```

Para:

```python
lista2 = [x**2 for x in range(1001) if x%5==0 or x%3==0]
print(sum(lista2))
```

### Multiplos loops

Nós também podemos fazer uma list comprehension com múltiplos loops.

Por exemplo,

```python
pontos = []
for x in [1,2,3]:
    for y in [3,4,5]:
        if x != y:
            pontos.append((x,y))
print(pontos)
```

se transforma em

```python
# Os loops serão postos, sem separação (somente um espaço), na mesma sequência do código original.
pontos = [(x,y) for x in [1,2,3] for y in [3,4,5] if x != y] 
print(pontos)
```

No entando, o que acontece quando queremos manipular uma lista com multiplas dimensões?

```python
matriz = [[1,2,3], [4,5,6], [7,8,9]]
matriz = [elemento * elemento for linha in matriz for elemento in linha]
```

Como podemos ver, nós acabamos achatando (flatten) a matriz em uma única dimensão.
Se quisermos manter a dimensionalidade, o correto é

```python
matriz = [[1,2,3], [4,5,6], [7,8,9]]
matriz = [[elemento * elemento for elemento in linha] for linha in matriz]
```

## Set comprehension

As set comprehensions permitem que conjuntos sejam construídos usando os mesmos princípios que as compreensões de lista,
a única diferença é que a seqüência resultante é um conjunto.

Seguiremos o modelo, apenas trocando os colchetes (da list comprehension) por chaves: 

```python
conjunto = {"expressão" for "elemento" in "sequência" if "condição"}.
```

Vejamos o exemplo abaixo:

```python
consoantes = set()
for letra in 'cursodafgv': 
    if letra not in "aeiou":
        consoantes.add(letra)
print(consoantes)
```

para

```python
consoantes = {letra for letra in 'cursodafgv' if letra not in "aeiou" }
print(consoantes)
```

## Dict comprehension

Finalmente, podemos escrever dicionários de maneira sucinta usando dict comprehension.
Lembrando apenas de tomar cuidado pois o dicionário distingue letras maiúsculas de minúsculas.

Usamos o modelo:

```python
dicionario = {'elemento' : 'operação' for 'elemento' in 'sequência' if 'condição'}
```

Vejamos o exemplo abaixo:

```python
quadrado = {}
for x in range(4):
    quadrado[x] = x**2
print(quadrado)
```

para

```python
quadrado = {x: x**2 for x in range(4)}
print(quadrado)
```

## Exercícios

1. Obtenha todos os inteiros da lista ```[1, 'hello', 'world', 3.9, 2]```
2. Remova todos os elementos maiores que 2 do conjunto ```{1, 2, 3, 4, 5}```
3. Filtre apenas os item que comecem com 'a' no dicionário  ```{'aipim': 8, 'limão': 5, 'batata': 5, 'alho': 20}```

