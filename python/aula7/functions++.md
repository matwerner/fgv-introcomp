# Funções (Continuação)

Conceitos avançados de funções, incluindo:
* funções aninhadas;
* funções como objetos;
* lambdas;
* recursão.

## Funções Dentro de Funções

Curiosamente, em Python, funções podem ser definidas dentro de outras funções.

```python
def externa():
    def interna():
        return "Esta é uma função interna"
    return interna()

print(externa()) # Output: Esta é uma função interna
```

Isso é útil quando uma função precisa ser usada apenas dentro do escopo de outra função.

### Exemplo: Validação de Senha

```python
def validar_senha(senha):
    def contem_caracteres_especiais(senha):
        caracteres_especiais = "!@#$%^&*()_+-=[]{}|;:,.<>?`~"
        for char in senha:
            if char in caracteres_especiais:
                return True
        return False

    if len(senha) < 8:
        return False
    if not contem_caracteres_especiais(senha):
        return False
    return True

print(validar_senha("senha@123"))  # Output: True
```

### Exemplo: Processamento de texto

```python
def processar_dicionario(dados):
    def processar_texto(texto):
        texto = texto.strip().upper()
        texto = " ".join(t.split())
        return texto

    return {
        'titulo': processar_texto(dados['titulo']),
        'autor': processar_texto(dados['autor']),
        'descricao': processar_texto(dados['descricao']),
    }

livro = {
    'titulo': '  o guia   completo para python  ',
    'autor': '  joão da  silva  ',
    'descricao': '   um  livro  abrangente  sobre  python   '
}

livro_processado = processar_dicionario(livro)
print(livro_processado)
```

É importante ressaltar que nada impede dessas funções serem declaradas do lado de fora.
A motivação para utilizar-se dessa abordagem é apenás isolar toda a lógica relacionada a uma função
 para tornar o código mais legível e manutenível.

## Funções como Objetos

Como mencionamos brevamente ao aprender estrutura de dados básicas, tudo em python é um objeto... **TUDO** em python é um objeto.
Logo, uma ***função*** é um ...? Exatamente!

```python
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

# Atribuindo funções a variáveis
operacao = soma
print(operacao(5, 3)) # Output: 8

operacao = subtracao
print(operacao(5, 3)) # Output: 2
```

Isso significa que funções podem ser atribuídas a variáveis, passadas como argumentos para outras funções e retornadas de outras funções.
Essa decisão da linguagem permite diversas aplicações interessantes.

### Exemplo: Testar diferentes pré-processamentos

```python
def encontrar_todas_as_palavras(texto, func):
    texto_processado = func(texto)
    return texto_processado.split()

def processamento1(texto):
    return texto.strip().upper()

def processamento2(texto):
    texto_processado = texto.strip().upper()

    pontuacao = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    texto_processado = "".join([letra if letra not in pontuacao else " "
                                for letra in texto_processado])
    return texto_processado

texto = "a-b"
print(encontrar_todas_as_palavras(texto, processamento1))
print(encontrar_todas_as_palavras(texto, processamento2))
```

### Exemplo: Criar uma fábrica de funções

```python
def gerar_preprocessamento(inclui_caixa_alta=False, remove_pontuacao=False):
    def preprocessamento(texto):
        texto_processado = texto.strip()
        if inclui_caixa_alta:
            texto_processado = texto_processado.upper()

        if remove_pontuacao:
            pontuacao = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
            texto_processado = "".join([letra if letra not in pontuacao else " "
                                        for letra in texto_processado])
        return texto_processado
    return preprocessamento

func1 = gerar_preprocessamento(inclui_caixa_alta=True)
func2 = gerar_preprocessamento(remove_pontuacao=True)
func3 = gerar_preprocessamento(inclui_caixa_alta=True, remove_pontuacao=True)

texto = "a-b"
print(func1(texto))
print(func2(texto))
print(func3(texto))
```

## Lambdas

As lambdas são funções anônimas (não precisam ter um nome definido) contendo apénas uma linha.
Elas são definidas usando a palavra-chave ```lambda``` e são úteis quando precisamos de uma função simples para uma operação rápida.

```python
dobro = lambda x: x * 2
print(dobro(5)) # Output: 10
```

Diversas funções built-in permitem o uso de lambdas para lidar com objetos complexos. 

```python
# Sorted
lista_dados = [
    {'nome': 'Rafael',  'idade': 30},
    {'nome': 'Bianca',  'idade': 22},
    {'nome': 'Bruno',   'idade': 18},
    {'nome': 'Eduardo', 'idade': 70},
    {'nome': 'Luisa',   'idade': 25},
]

print(sorted(lista_dados, key=lambda x: x['nome']))
print(sorted(lista_dados, key=lambda x: x['idade']))

# Max / Min
numeros = [4, 2, 7, 1, 5]
maior_numero = max(numeros, key=lambda x: x % 3)
```

## Exercicios

1. Escreva uma função externa chamada `calculadora` que recebe dois números e uma string representando uma operação matemática ('soma', 'subtracao', 
'multiplicacao' ou 'divisao'). Dentro da função `calculadora`, defina funções internas para cada operação e use essas funções internas para calcular o 
resultado com base na operação fornecida.

2. Crie uma lista de números e uma lista de funções matemáticas (por exemplo, `dobro`, `triplo`, `quadrado`).
Escreva uma função que receba uma lista de números e uma lista de funções, e aplique cada função a cada número da lista, retornando uma lista com os 
resultados.

3. Utilize a função `sorted()` para ordenar uma lista de palavras em ordem crescente de tamanho das palavras. Use uma lambda para especificar a chave de ordenação.
