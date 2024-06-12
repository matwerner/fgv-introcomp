# Exercícios

Lista de exercícios múltipla-escolha em preparação para A2.

## 1. Verificar as diferentes formas de se fazer uma mesma solução

Marque os blocos de código que calculam a soma dos quatro vizinhos (superior, inferior, esquerdo e direito)
de um dado elemento na linha $y$ e coluna $x$ de uma matriz $A$. 
O valor do elemento central não deve ser incluído na soma.
Assuma que $0 < x < len(A[0])-1$ e $0 < y < len(A)-1$.
A cada opção errada que for selecionada, desconta-se nota do exercício.

A) 
```python
soma = 0
D = [[0,-1],[0,1],[-1,0], [1,0]]
for i in range(len(A)):
    for j in range(len(A[0])):
        if [i-y, j-x] in D:
            soma += A[i][j]
```

B)
```python
soma = 0
for i in range(y-1,y+2):
    for j in range(x-1,x+2):
        soma += A[i][j]
```

C)
```python
soma = 0
dx = [ 0, 1, 0,-1]
dy = [-1, 0, 1, 0]
for k in range(len(dx)):
    j = x + dx[k]
    i = y + dy[k]
    soma += A[i][j]
```

D)
```python
soma = 0
dx = dy = [0, 1, 0,-1]
for k in range(-1,len(dx)-1):
    j = x + dx[k]
    i = y + dy[k+1]
    soma += A[i][j]
```

E)
```python
soma = -A[y][x]
for i in range(y-1,y+2):
    for j in range(x-1,x+2):
        if i == x or j == y:
            soma += A[i][j]
```

## 2. Alterar o programa para ter comportamento correto

A função abaixo deveria calcular, para uma lista de números previamente ordenada em ordem
crescente e contendo uma quantidade ímpar de valores, a diferença entre sua média e sua mediana.
Por exemplo, dada a lista $L = [2, 3, 5, 9, 11]$, sua média é dada por:
$$Md(L) = (2 + 3 + 5 + 9 + 11)/len(L) = 6.$$

Sua mediana é dado por:
$$Mn(L) = L[len(L)//2] = 5.$$

A diferença é dada por:
$$Dif(L) = Md(L) − Mn(L) = 1.$$

Essa função, entretanto, contém erros.
Marque as opções correspondentes às correções necessárias para que a função efetue o ál ulo orretamente.
Observação: a cada item errado que for selecionado, desconta-se até $0.5$ da nota do exercício.

```python
(1) def Dif(L) :
(2)     Md = 0
(3)     for i in range(1, len(L)):
(4)         Md += L[i]/i
(5)     Md /= len(L) - 1
(6)     return Md - L[len(L)/2]
```

A) Substituir a linha (5) por `Md /= L[len(L)]`\
B) Substituir a linha (3) por `for i in range(len(L)):`\
C) Substituir a linha (4) por `Md += L[i]`\
D) Substituir a linha (2) por `Md = L[i]`\
E) Substituir a linha (5) por `Md /= len(L)`\
F) Substituir a linha (6) por `return Md - L[len(L)//2]`\
G) Substituir a linha (4) por `Md += L`\
H) Substituir a linha (2) por `Md = 1`

### 3. Fazer um programa mais complexo

Preencha as lacunas no código abaixo (L1 até L8), de forma a obter um programa que
lê um arquivo de texto e determina a palavra mais frequente com pelo menos 3 letras e sua frequência relativa de ocorrência no texto.

```python
def maxfreq (nome):
    a = # L1
    f = # L2
    for l in a:
        l = # L3
        for p in l:
            if len(p) >= 3:
                if # L4 :
                    f[p] += 1
                else:
                    # L5
    m = None
    for p in f:
        m = p
        t = 0
        for # L6 :
            t += f[p]
            if # L7 :
                m = p
    a.close()
    return # L8

def main ():
    arq = input ('Nome do arquivo: ')
    p, f = maxfreq (arq)
    print ('palavra:', p, 'freq. rel.:', f)

main()
```

| Linha  | A               | B               | C               | D               |
| ------ | --------------- | --------------- | --------------- | --------------- |
| L1:    | file(nome, 'w') | open(nome, 'w') | file(nome, 'r') | open(nome, 'r') |
| L2:    | [0]*len(nome)   | []              | {}              | [0]*len(a)      |
| L3:    | l.split()       | l.split(`,')    | a.readline()    | a.read()        |
| L4:    | p not in f      | f[p] != 0       | f[p] == 0       | p in f          |
| L5:    | f[p] = 1        | f.append(p)     | f[p] -= 1       | f[p] = 0        |
| L6:    | p in f          | p in f.values() | p in l          | p in l.keys()   |
| L7:    | f[p] < f[m]     | f[p] > t        | f[p] > f[m]     | f[p] < t        |
| L8:    | m, f[m]/t       | m, t            | m, t/f[m]       | m, f[m]         |

### 4. V ou F sobre comportamento de uma dada função

Considere o programa abaixo:

```python
def f(w):
    return w[0]

def l(w):
    return w[len(w)-1]

def m(w):
    n = len(w)
    return w[1:n-1]

def p(w):
    if len(w) <= 1:
        return True
    if f(w) != l(w):
        return False
    return p(m(w))

def main():
    print(p("allen"))
    print(p("bob"))
    print(p("o"))
    print(p("ma "))

main()
```

Assinale entre as opções a seguir, as afirmações verdadeiras.

Considerações:
* As opções podem conter desde nenhuma afirmação correta até todas.
* A cada item errado que for selecionado, desconta-se até 1 ponto da nota do exercício.

A) A função $f$, quando recebe uma string $w$, retorna o primeiro caracter da string\
B) `m(m("Paulo")) == "aul"`\
C) Ao rodar, o programa imprime `False`, depois `True` duas vezes e por último `False`\
D) Apesar de haver $4$ chamadas à função $p$ na função $main$, ela é de fato exeutada $5$ vezes\
E) Se houvesse uma última linha na função $main$ com o conteúdo: `print(p([1,2,3,2,1]))`, o programa daria erro\
F) Se houvesse uma última linha na função $main$ com o conteúdo: `print(p("12321"))`, o programa daria erro\
G) A função $l$, quando recebe uma string $w$, retorna o último caracter da string\
H) A função $f$, quando recebe um número inteiro $w$, devolve seu primeiro dígito\
I) O programa dá erro porque a linha return `w[len(w)-1]` na função $l$ está errada já que o índice da lista não é um número inteiro\
J) A função $f$, quando recebe uma matriz $w$, devolve sua primeira linha

## Questões a serem (Talvez, possivelmente, quem sabe) estruturadas

### Tipo 1. Verificar as diferentes formas de se fazer uma mesma solução
* Q2 -> https://www.ime.usp.br/~mac2166/provas/P2-2018Py.pdf
* Q2 -> https://www.ime.usp.br/~mac2166/provas/P3-2018Py.pdf
* Q2 -> https://www.ime.usp.br/~mac2166/provas/P3-2022Py.pdf
* Q3 -> https://www.ime.usp.br/~mac2166/provas/PSUB-2023Py.pdf

### Tipo 2. Alterar o programa para ter comportamento correto
* Q2 -> https://www.ime.usp.br/~mac2166/provas/PSUB-2017Py.pdf
* Q4 -> https://www.ime.usp.br/~mac2166/provas/PSUB-2017Py.pdf

### Tipo 3. Fazer um programa mais complexo
* Q4 -> https://www.ime.usp.br/~mac2166/provas/P3-2022Py.pdf
* Q3 -> https://www.ime.usp.br/~mac2166/provas/P3-2017Py.pdf
* Q3 -> https://www.ime.usp.br/~mac2166/provas/PSUB-2017Py.pdf
* Q4 -> https://www.ime.usp.br/~mac2166/provas/PSUB-2019Py.pdf

### Tipo 4. V ou F sobre comportamento de uma dada função
* Q2 -> https://www.ime.usp.br/~mac2166/provas/P2-2017Py.pdf
* Q2 -> https://www.ime.usp.br/~mac2166/provas/P3-2017Py.pdf
* Q4 -> https://www.ime.usp.br/~mac2166/provas/PSUB-2018Py.pdf
* Q4 -> https://www.ime.usp.br/~mac2166/provas/P2-2019Py.pdf