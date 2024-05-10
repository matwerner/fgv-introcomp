# Recursão

Nesta aula, exploraremos o conceito de recursão em Python, que é uma técnica poderosa onde uma função chama a si mesma diretamente ou indiretamente para resolver um problema. A recursão é amplamente utilizada em algoritmos e pode simplificar a solução de problemas complexos.

## O que é Recursão?

Recursão é um conceito em programação onde uma função resolve um problema dividindo-o em subproblemas menores e chamando a si mesma para resolver esses subproblemas.

- **Caso Base**: Uma função recursiva precisa ter um caso base que define a condição de parada da recursão, evitando que a função chame a si mesma indefinidamente.
- **Caso Recursivo**: Além do caso base, a função recursiva precisa ter um caso recursivo que divide o problema em subproblemas menores e chama a si mesma para resolver esses subproblemas.

### Exemplo: Cálculo de Fatorial

O cálculo do fatorial de um número é um exemplo clássico de recursão. O fatorial de um número inteiro positivo \( n \) (denotado por \( n! \)) é o produto de todos os inteiros positivos menores ou iguais a \( n \).

A fórmula para calcular o fatorial de \( n \) é:

$ n! = \begin{cases} 1 & \text{se } n = 0 \\ n \times (n-1)! & \text{se } n > 0 \end{cases} $

```python
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

print(fatorial(5))  # Output: 120
```

### Exemplo: Sequência de Fibonacci

A sequência de Fibonacci é outra aplicação comum de recursão. Nesta sequência, cada número é a soma dos dois números anteriores.

A fórmula para calcular o termo nn da sequência de Fibonacci é:

$ 
F(n) = 
\begin{cases} 
    0 & \text{se } n = 0 \\
    1 & \text{se } n = 1 \\ 
    F(n-1) + F(n-2) & \text{se } n > 1
\end{cases} 
$

```python
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(7))  # Output: 13
```

## Vantagens e Desvantagens da Recursão

* Vantagens:
    - Simplifica a solução de problemas complexos;
    - Torna o código mais legível e fácil de entender;
    - Pode ser mais eficiente em alguns casos.
* Desvantagens:
    - Pode consumir mais memória devido ao uso da pilha de chamadas;
    - Pode ser menos eficiente em comparação com abordagens iterativas para alguns problemas;
    - Pode ser difícil de depurar devido à natureza aninhada das chamadas de função.

## Comparação: Iteração vs Recursão

Ao resolver problemas em programação, muitas vezes enfrentamos a escolha entre usar iteração (loops) ou recursão para implementar uma solução. Ambas as abordagens têm seus próprios prós e contras, e a escolha entre elas depende do problema específico e das preferências do programador.

### Iteração

Na iteração, usamos loops (como `for` ou `while`) para repetir um bloco de código várias vezes até que uma condição de término seja atendida. Aqui estão algumas características da iteração:

- **Clareza**: Em alguns casos, a iteração pode ser mais clara e direta do que a recursão, especialmente para problemas simples.
- **Eficiência**: Em geral, a iteração é mais eficiente em termos de uso de memória e velocidade de execução, especialmente para problemas onde a recursão pode levar a uma grande quantidade de chamadas de função.

### Recursão

Na recursão, uma função chama a si mesma diretamente ou indiretamente para resolver um problema. Aqui estão algumas características da recursão:

- **Elegância**: A recursão pode simplificar a solução de problemas complexos, tornando o código mais elegante e fácil de entender.
- **Flexibilidade**: Alguns problemas são naturalmente resolvidos de forma mais eficiente com recursão, especialmente aqueles que podem ser decompostos em subproblemas menores e idênticos ao problema original.

### Escolhendo entre Iteração e Recursão

- **Natureza do Problema**: Alguns problemas são naturalmente mais adequados para serem resolvidos com recursão, enquanto outros são mais facilmente resolvidos com iteração.
- **Eficiência**: Em casos onde a eficiência é uma preocupação (por exemplo, em problemas que exigem um grande número de chamadas de função), pode ser preferível usar iteração.
- **Legibilidade**: Em casos onde a clareza e a legibilidade do código são mais importantes do que a eficiência, a recursão pode ser a melhor escolha.

É importante considerar esses fatores ao decidir entre iteração e recursão para resolver um problema específico. Em última análise, a escolha depende do contexto do problema e das preferências individuais do programador.

## Exercícios

1. Escreva uma função recursiva para calcular a soma dos primeiros `n` números naturais.
2. Implemente uma função recursiva para encontrar o máximo divisor comum (MDC) de dois números.
3. Desenvolva uma função recursiva para calcular a potência de um número `x` elevado a um expoente `n`.
4. Escreva uma função recursiva para inverter uma lista.

