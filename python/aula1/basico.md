# Aula Introdutória de Python

Nesta aula, vamos explorar os fundamentos da linguagem de programação Python.

## Como o Interpretador Lê o Código

O interpretador Python lê o código linha por linha e executa as instruções conforme encontra.

# Funções (Caso do Print)

Funções em Python são blocos de código reutilizáveis que realizam tarefas específicas.
Um exemplo comum é a função print(), que exibe texto na tela.

Exemplo:

python
```python
print("Olá, mundo!")
```

Existem diversas outras funções built-in no python, como 
```input```,
```type```,
```int```,
```float```.

## Constantes Numéricas e Textuais

Em Python, você pode trabalhar com constantes:
1. Numéricas (como inteiros e floats);
2. Textuais (strings). 

Elas são valores fixos que não podem ser alterados durante a execução do programa.

Exemplos:

```python
numero = 10
texto = "Python é incrível!"
```

## Nomes de Variáveis

As variáveis em Python devem seguir algumas regras:

    Podem começar com letra ou underscore (_)
    Podem conter letras, números e underscores
    São sensíveis a maiúsculas e minúsculas

Algumas dicas:
1. Seja Descritivo;
2. Seja Conciso;
3. Mantenha a Consistência.

## Exemplos de convenções de nomenclatura: camelCase e snake_case.

**camelCase**: Capitalize cada palavra, exceto a primeira, sem espaços entre elas.
```python
nomeDoUsuario = "abcde"
contagemDeItens = 10
```

**snake_case**: Use minúsculas e underscores (_) para separar palavras.
```python
nome_do_usuario = "abcde"
contagem_de_itens = 10
```

## Atribuições

Em Python, você pode atribuir valores a variáveis usando o operador de atribuição (=).

Exemplo:

```python
x = 10
```

O Python primeiro avalia a expressão à direita do sinal de igualdade e, em seguida, atribui o resultado à variável x.
## Operadores

Python suporta vários tipos de operadores, como divisão, subtração, adição, etc.

| Operador | Descrição       | Exemplo     |
|----------|-----------------|-------------|
| +        | Adição          | `5 + 3`     |
| -        | Subtração       | `5 - 3`     |
| *        | Multiplicação   | `5 * 3`     |
| /        | Divisão         | `5 / 3`     |
| %        | Módulo          | `5 % 3`     |
| **       | Exponenciação   | `5 ** 3`    |
| //       | Divisão Inteira | `5 // 3`    |

## Como Linhas de Código São Processadas

As linhas de código em Python são processadas em uma ordem específica, levando em consideração variáveis, constantes, operadores e funções. Por exemplo, na declaração:

```python
x = 3.9 * x * (1 + x)
```

## Ordem de Avaliação

A ordem de avaliação das expressões em Python segue a regra PEMDAS:
1. Parenteses;
2. Exponenciação;
3. Multiplicação/Divisão;
4. Adição/Subtração.

Em casos ambiguos, a expressão é processada da esquerda para direita.

```python
x = 2 ** 10 * 2 + 3 / 4
```

## Tipos de Variáveis e Operações

Python possui vários tipos de variáveis, como:
* inteiros,
* floats,
* strings,
* boleanos,
* etc.

Cada tipo de variável suporta diferentes operações.

## Conversão de Variáveis

### Implicita

Às vezes, Python converte automaticamente um tipo de variável em outro, por exemplo, ao realizar operações entre diferentes tipos.

```python
a = True
b = 2
c = 3.9

print(a + b)
print(a + c)
print(b + c)
```

### Explícita

Você também pode converter explicitamente tipos de variáveis usando funções como int(), float(), str(), etc.

```python
a = True
a = int(a)
print(a)
```

### Conversão de Valores Passados pelo Usuário

Ao receber entrada do usuário, é importante converter os valores para o tipo correto, caso necessário.

```python
x = input("Insira um número")
x = int(x)
print(x)
```

## Exercícios

1. Peça dois números ao usuário e calcule a média entre eles;
2. Converta uma temperatura passada pelo usuário de Celsius para Fahrenheit.
