# Condicionais

As condicionais são operações que nos permitem controlar o fluxo de execução do código com base em condições específicas.
Dependendo das condições definidas, diferentes trechos de códigos serão executados.

## Sintaxe e estrutura

Os condicionais são definidos pelas palavras-chave 
```if```, 
```elif``` (abreviação de "else if") e ```else```.
A estrutura básica dos condicionais é a seguinte:

```python
if condição:
    # bloco de código se a condição for verdadeira
elif outra_condição:
    # bloco de código se a outra condição for verdadeira
else:
    # bloco de código se nenhuma das condições anteriores for verdadeira
```

## Exemplo
Exemplo de avaliação de condições:

```python
x = 10
if x > 5 and x < 15:
    print("x está entre 5 e 15")
elif x <= 5 or x >= 15:
    print("x está fora do intervalo de 5 a 15")
```

## Operações de Comparação

Python suporta as seguintes operações de comparação:

| Operador | Descrição                  | Exemplo           |
|----------|----------------------------|-------------------|
| ==       | Igual a                    | `a == b`          |
| !=       | Diferente de               | `a != b`          |
| <        | Menor que                  | `a < b`           |
| >        | Maior que                  | `a > b`           |
| <=       | Menor ou igual a           | `a <= b`          |
| >=       | Maior ou igual a           | `a >= b`          |

## Operadores lógicos

Enquanto suporta os seguintes operados lógicos:

| Operador | Descrição                                              | Exemplo                                  |
|----------|--------------------------------------------------------|------------------------------------------|
| and      | Retorna True se ambos os operandos forem True         | `True and True`                          |
| or       | Retorna True se pelo menos um dos operandos for True   | `True or False`                          |
| not      | Retorna True se o operando for False e False se o operando for True | `not False`                     |

onde esse são todos os possiveis resultados de cada operação\
(Lembrar que True = 1 e False = 0)

**AND**

| A     | B     | A and B |
|-------|-------|---------|
| 0     | 0     | 0       |
| 0     | 1     | 0       |
| 1     | 0     | 0       |
| 1     | 1     | 1       |

**OR**

| A     | B     | A or B |
|-------|-------|--------|
| 0     | 0     | 0      |
| 0     | 1     | 1      |
| 1     | 0     | 1      |
| 1     | 1     | 1      |

**NOT**

| A     | not A |
|-------|-------|
| 0     | 1     |
| 1     | 0     |

## Ordem de Avaliação

Dado a condicional abaixo, qual mensagem será exibida na tela?

```python
x = 25
if x > 20 or x > 10 and x < 15:
    print("Opção A")
else:
    print("Opção B")
```

Similar ao que vimos com as operações matemáticas, operadores lógicos tambem
seguem uma ordem de avaliação:
1. Not
2. And
3. Or

## Cuidados

1. Identação correta apenas com ```tabs``` ('\t') ou ```espaços``` (' ')

2. Tratamento de todos os casos

```python
numero = 10
if numero > 0:
    print("O número é positivo")
elif numero < 0:
    print("O número é negativo")
else:
    print("O número é zero")
```

3. Evitar codições redundantes

```python
numero = 10
if numero > 0:
    print("O número é positivo")
elif numero > 5: 
     # Condição redundante, pois a condição anterior já cobre este caso
    print("O número é maior que 5")
else:
    print("O número é zero ou negativo")
```

4. Evitar aninhamento excessivo

```python
# Exemplo de aninhamento excessivo
numero = 1
if numero > 0:
    if numero % 2 == 0:
        print("O número é positivo e par")
    else:
        print("O número é positivo e ímpar")
else:
    print("O número é negativo")
```

## Exercícios

1. Verifique se um número é posítivo, negativo ou zero
2. Dado os 3 lados de um triangulo como entrada, classifica-lo como Equilátero, Isoceles ou Escaleno;


