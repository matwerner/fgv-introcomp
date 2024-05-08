# Funções

## Introdução

Dado o que vimos até agora no curso, como criariamos um menu simples no terminal contendo operações a seguir?
1. Visualizar um texto informativo;
2. Calcular a área de um retângulo, solicitando ao usuário que insira os valores do comprimento e largura;
3. Sair do programa

Resposta:
```python
while True:
    print("Bem-vindo ao Menu:")
    print("1. Visualizar Texto Informativo")
    print("2. Calcular Área de um Retângulo")
    print("3. Sair")

    escolha = input("Digite o número da opção desejada: ")
    if escolha == '1':
        print("Texto informativo: Python é uma linguagem de programação poderosa e versátil.")
    elif escolha == '2':
        comprimento = float(input("Digite o comprimento do retângulo: "))
        largura = float(input("Digite a largura do retângulo: "))
        area = comprimento * largura
        print("A área do retângulo é:", area)
    elif escolha == '3':
        print("Saindo do programa. Até mais!")
        break
    else:
        print("Opção inválida. Por favor, digite um número válido.")
```

Qual sua opnião a respeito desse script?\
E, se fosse necessário adicionar mais items ao menu e, até mesmo, submenus?

### Benefícios das funções

Ao adicionar novos itens e submenus, é evidente que a complexidade do código acima pode crescer rapidamente, comprometendo sua organização e legibilidade.

Nesse contexto, é crucial compreender o papel que as **funções** tem Python, assim como em outras linguagens de programação.
Elas definem blocos de código reutilizáveis, estruturados para desempenhar tarefas específicas de forma eficiente e modular.
Utilizá-las traz uma série de benefícios fundamentais:

* **Simplificação e Organização**:\
Ao agrupar operações relacionadas em funções, o código torna-se mais organizado e legível, facilitando a compreensão e manutenção futura.
* **Reutilização de Código**:\
A capacidade de chamar uma função em diferentes partes do código elimina a necessidade de repetir blocos de código, promovendo a eficiência e a consistência do programa.
* **Flexibilidade e Adaptação**:\
Ao encapsular comportamentos em funções, é possível realizar alterações significativas no comportamento do programa sem a necessidade de modificar extensivamente o código principal.

### Convertendo a aplicação acima...

Ao utilizarmos funções, podemos converter o código acima da seguinte forma:

```python
def exibir_menu():
    print("Bem-vindo ao Menu:")
    print("1. Visualizar Texto Informativo")
    print("2. Calcular Área de um Retângulo")
    print("3. Sair")

def exibir_texto_informativo():
    print("Texto informativo: Python é uma linguagem de programação poderosa e versátil.")

def calcular_area_retangulo():
    comprimento = float(input("Digite o comprimento do retângulo: "))
    largura = float(input("Digite a largura do retângulo: "))
    area = comprimento * largura
    print("A área do retângulo é:", area)

def main():
    while True:
        exibir_menu()
        escolha = input("Digite o número da opção desejada: ")
        
        if escolha == '1':
            exibir_texto_informativo()
        elif escolha == '2':
            calcular_area_retangulo()
        elif escolha == '3':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, digite um número válido.")

main()
```

## Sintaxe

Uma função tem a seguinte sintaxe em python:

<p align="center">
  <img src="function_syntax.webp" width="600"/>
</p>

### Exemplo

Uma função tem a seguinte estrutura:
```python
def saudacao(nome):
    print("Olá,", nome)
saudacao("Maria")
```

## Tipos de argumentos / parâmetros
* **Argumentos**: São os valores passados para uma função durante sua chamada.
* **Parâmetros**: São as variáveis que recebem os valores dos argumentos dentro da função.


### Sequencial
Os argumentos são associados aos parâmetros com base em sua posição.

```python
def exibir_divisao(num, den):
    print("Divsão: ", num / den)
exibir_divisao(4, 2)
```

### Palavra-chave
Os argumentos são associados aos parâmetros usando seus nomes.
```python
def exibir_divisao(num, den):
    print("Divsão: ", num / den)
exibir_divisao(num=4, den=2)
```

### Valor padrão
Os parâmetros podem ter valores padrão, que são usados quando nenhum valor é fornecido durante a chamada da função.

```python
def exibir_divisao(num, den=1):
    print("Divisão: ", num / den)
exibir_divisao(4)
```

### Observações

* Os argumentos posicionais devem vir antes dos argumentos por palavra-chave durante a chamada da função.
* A ordem dos parâmetros na definição da função é crucial para os argumentos posicionais, mas não para os argumentos por palavra-chave.

### Exercícios

1. Escreva uma função chamada ```exibir_info``` que recebe três parâmetros: ```nome```, ```idade``` e ```cidade```.
Esses parâmetros devem ter valores padrão de uma string vazia.
Dentro da função, imprima as informações no formato ```"Nome: [nome], Idade: [idade], Cidade: [cidade]"```.

2. Escreva uma função chamada ```cumprimentar_usuario``` que recebe um parâmetro ```nome```.
A função deve imprimir uma mensagem de saudação usando o nome fornecido.
Se nenhum nome for fornecido, ele deve ser padrão para "Usuário".

3. Escreva uma função chamada ```formatar_pedido``` que recebe parâmetros nomeados ```item```, ```quantidade``` e ```preco_por_unidade```, com valores padrão para ```quantidade``` $= 1$ e ```preco_por_unidade``` $= 0$. Dentro da função, calcule o preço total multiplicando a quantidade pelo preco_por_unidade. Exiba um texto que formate as informações do pedido no formato: ```"Pedido: [quantidade] x [item] a R$[preco_por_unidade] cada. Total: $[preco_total]"```.

4. Considere a seguinte função:

```python
def adicionar_elemento(lista):
    lista.append(4)

minha_lista = [1, 2, 3]
adicionar_elemento(minha_lista)
print(minha_lista)
```

a. Antes de executar o código, o que você espera que seja impresso após a chamada da função ```adicionar_elemento```?\
b. Qual é o impacto da chamada da função ```adicionar_elemento``` na lista minha_lista?\
c. Quais outros tipos de váriaveis (classes) possuem um comportamento similar? e quais possuem um comportamento diferente?

## Lidando com argumentos variáveis (*args e **kwargs)
Às vezes, pode ser útil lidar com um número variável de argumentos em uma função. Para isso, podemos usar *args e **kwargs.

### *args
Permite passar um número variável de argumentos posicionais para uma função

```python
def exibir_soma(*args):
    total = 0
    for num in args:
        total += num
    print(total)
exibir_soma(1, 2, 3, 4, 5)
```

### **kwargs
Permite passar um número variável de argumentos por palavra-chave para uma função.

```python
def saudacao(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} diz: {value}")

saudacao(Joao="Oi", Maria="Olá", Ana="Oi pessoal!")
```

### Observações

* Os argumentos posicionais e por palavra-chave ainda podem ser usados em conjunto com *args e **kwargs.
* *args e **kwargs não são palavras reservadas, mas convenções amplamente utilizadas.
* É importante manter a clareza ao usar esses recursos para evitar confusões na leitura e manutenção do código.

### Exercícios

1. Escreva uma função chamada ```calcular_media``` que recebe o nome do aluno e uma quantidade arbitrária de notas.
Dentro da função, calcule a média das notas passadas.
Exiba um texto que formate o resultado no formato: ```"O aluno [nome] teve média final [média]"```.

2. Escreva uma função chamada ```criar_perfil``` que recebe o nome de uma pessoa como primeiro argumento e argumentos de palavra-chave arbitrários representando vários aspectos de seu perfil (por exemplo, idade, cidade, ocupação, etc.).
Dentro da função, construa um dicionário onde as chaves são os nomes dos argumentos e os valores são os valores correspondentes passados para a função. 
Exiba este dicionário ao final da função.

## Retorno
Ao escrever funções em Python, é comum que elas retornem valores como resultado de suas operações.
O retorno de uma função é feito utilizando a instrução ```return```.

```python
def soma(a, b):
    resultado = a + b
    return resultado
print(soma(3, 5))
```

### Retorno de Múltiplos Valores
Uma função em Python também pode retornar múltiplos valores, separados por vírgula.

```python
def divide_e_resto(dividendo, divisor):
    quociente = dividendo // divisor
    resto = dividendo % divisor
    return quociente, resto

# Chamando a função e desempacotando os valores retornados
resultado, resto = divide_e_resto(10, 3)
print("Quociente:", resultado)
print("Resto:", resto)
```

### Retorno de Vazio (None)
Se uma função não especificar um valor de retorno utilizando a instrução ```return```, 
ela retorna automaticamente None.

```python
def funcao_sem_retorno():
    print("Esta função não tem retorno")
retorno = funcao_sem_retorno()
print(retorno) 
```

### Exercícios

1. Escreva uma função chamada ```calcular_quadrado``` que recebe um único parâmetro ```num```.
Dentro da função, calcule o quadrado de num e retorne-o.

2. Escreva uma função chamada ```calcular_propriedades_retângulo``` que recebe dois parâmetros: ```comprimento``` e ```largura```.
Dentro da função, calcule tanto a área quanto o perímetro do retângulo definido por estas dimensões.
Retorne estes valores como uma tupla (área, perímetro).

3. Escreva uma função chamada ```obter_informacoes_usuario``` que peça ao usuário que informe seu nome, idade e email
Dentro da função, construa um dicionário contendo essas informações.
Retorne este dicionário.

4. Escreva uma função chamada ```verificar_par_impar``` que recebe um parâmetro inteiro ```num```.
Dentro da função, verifique se o número é par ou ímpar.
Se for par, retorne a string "Par", caso contrário, retorne "Ímpar".

## Escopo de váriavel

O escopo de uma variável refere-se à parte do programa onde a variável é acessível.

### Exemplo:
```python
def exibir():
    x = 10  # Variável local
    print(x)

exibir()
print(x)  # Erro! x não está definido fora da função
```

### Variável Local e Global

* **Variáveis Locais**: São aquelas declaradas dentro de uma função e só são acessíveis dentro dela.
* **Variáveis Globais**: São aquelas declaradas fora de todas as funções e podem ser acessadas de qualquer lugar do programa.

```python
x = 10  # Variável global

def exibir():
    print(x)  # Variável global acessível dentro da função

exibir()
print(x)  # Variável global acessível fora da função
```

No exemplo acima, a variável ```x``` é uma variável global, pois é definida fora de qualquer função.
Portanto, pode ser acessada tanto dentro quanto fora da função ```exibir()```.

E, no caso abaixo, qual o comportamento você espera?

```python
x = 10  # Variável global

def exibir():
    x = 20  # Modificando a variável dentro da função
    print(x)

exibir()
print(x)  # Valor da variável global
```

E nesse?

```python
x = 10  # Variável global

def exibir():
    print(x)
    x = 20  # Modificando a variável dentro da função

exibir()
print(x)  # Valor da variável global
```

### A Palavra-chave global:

A palavra-chave ```global``` é usada para declarar que uma variável fora do escopo local da função deve ser tratada como global dentro da função.

```python
x = 10  # Variável global

def exibir():
    global x
    x = 20  # Modificando a variável global dentro da função
    print(x)

exibir()
print(x)  # Valor da variável global foi modificado pela função
```

### A Palavra-chave nonlocal:

A palavra-chave ```nonlocal``` é semelhante à palavra-chave ```global```, 
mas é usada para variáveis em um escopo externo ao local, mas não global.

```python
def funcao_exterior():
    x = 10  # Variável no escopo externo

    def funcao_interior():
        nonlocal x
        x = 20  # Modificando a variável no escopo externo
        print(x)

    funcao_interior()
    print(x)  # Valor da variável no escopo externo foi modificado pela função interior

funcao_exterior()
```

No exemplo acima, a variável ```x``` é definida na função exterior ```funcao_exterior()```.
Dentro da função interior ```funcao_interior()```, a palavra-chave ```nonlocal``` é usada para indicar que a variável x está no escopo exterior.
Isso permite que a função interior modifique a variável no escopo externo.

### Exercícios

1. Escreva um programa que contenha uma função chamada ```contar_chamadas``` que incrementa um contador global a cada vez que é chamada.
Em seguida, chame a função várias vezes e imprima o valor do contador.

2. Considere a seguinte função em Python: 

```python
def scope_test():
    def do_local():
        spam = "local spam"
        
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
        
    def do_global():
        global spam
        spam = "global spam"
        
    spam = "test spam"
    do_local()

    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
```

o que você espera que seja impresso após cada chamada de função e na linha final?

<!-- 
## Exercícios

1. Você foi contratado por uma loja para criar uma função que calcule o valor total das compras de um cliente, levando em consideração os descontos aplicáveis. A loja oferece os seguintes descontos com base no valor total das compras:

    * 10% de desconto para compras acima de R$ 500,00.
    * 20% de desconto para compras acima de R$ 1000,00.
    * 30% de desconto para compras acima de R$ 1500,00.

    Escreva uma função chamada ```calcular_total_compras``` que receba como argumento o valor total das compras e retorne o valor total a ser pago após aplicar os descontos.

    Teste a corretude dá sua função, utilizando os seguintes valores: R$ 400, R$ 600, R$ 1200, R$ 1800.

2. Você foi designado para criar uma função que normalize um texto, permitindo apenas letras e espaços, convertendo todas as letras para minúsculas e emovendo espaços extras entre as palavras.

    Escreva uma função chamada ```normalizar_texto``` que receba uma string como entrada e retorne o texto normalizado.

    Teste a corretude dá sua função, utilizando o seguinte texto:
    ```"Olá, este é um texto com! @caracteres especiais e espaços    extras  ."```
-->
