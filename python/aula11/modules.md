# Módulos e Pacotes

## O que são Módulos?

Até agora, nas aulas, nós criamos scripts simples contendo um conjunto pequeno de funções e variáveis a serem executados através de um interpretador Python.
Contudo, à medida que esses scripts ficam maiores, pode ser melhor dividi-los em vários arquivos separados para facilitar a manutenção.
Também pode ser interessante centralizar uma função útil em diferentes contextos em um único lugar, em vez de escrevê-la em vários programas diferentes.

Para suportar isso, Python desenvolveu uma maneira de colocar definições de funções e variáveis em um arquivo para serem usadas por outros scripts.
Esse arquivo é chamado de `módulo`.

## Por que usar Módulos?

* **Organização**: Mantém o código limpo e organizado.
* **Reutilização**: Permite reutilizar funções em diferentes partes de um programa ou em diferentes projetos.
* **Namespace**: Ajuda a evitar conflitos de nomes ao definir um escopo separado.

## Criando e usando módulos

### Criando

Um módulo em Python é simplesmente um arquivo com a extensão .py que contém definições de funções, variáveis e até mesmo outras estruturas de código, como classes.
Ou seja, nós podemos considerar que todos os scripts que desenvolvemos até agora são modulos que podem ser utilizados por outros scripts.

Por exemplo, vamos criar um módulo chamado `processamento.py``:

```python
# processamento.py

def preprocessar_texto(texto):
    # Remover espaços laterais
    texto_processado = texto.strip()

    # Color em caixa-baixa
    texto_processado = texto_processado.lower()

    # Remover números
    texto_processado = ''.join([c for c in texto_processado if not c.isdigit()])

    return texto_processado

pontuacoes = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
```

### Importando

Depois de criar um módulo, você pode importá-lo em outros arquivos Python usando a instrução `import`.

```python
# main.py

# Importar nosso modulo de processamento de texto
import processamento

texto = "A resposta para a questão fundamental da vida, do universo e de tudo mais é 42."
print(processamento.preprocessar_texto(texto))

print(processamento.pontuacoes)
```

Se preferir, você também pode importar funções específicas de um módulo usando a sintaxe `from ... import ....``

```python
# main.py

# Importar funções especificas do nosso modulo de processamento de texto
from processamento import preprocessar_texto, pontuacoes

texto = "A resposta para a questão fundamental da vida, do universo e de tudo mais é 42."
print(preprocessar_texto(texto))

print(pontuacoes)
```

Ao executar o programa principal `main.py`, ele importará o módulo `processamento.py` e usará as funções e classes definidas nele.

## Namespace e Escopo

### Namespace

Um `namespace` em Python é um contexto onde nomes únicos são associados a objetos, uma especie de extensão do `escopo de variáveis` que vimos anteriormente.
Os módulos em Python ajudam a evitar conflitos de nomes, agrupando variáveis e funções em seus próprios namespaces.

Por exemplo, se tivermos dois módulos diferentes, cada um com uma função chamada soma, não haverá conflito de nomes, pois eles estarão em namespaces separados:

```python
# modulo1.py
def soma(a, b):
    return a + b
```

```python
# modulo2.py
def soma(x, y):
    return x + y
```

Ao importar esses módulos, podemos usá-los sem se preocupar com conflitos de nomes:

```python
import modulo1
import modulo2

print(modulo1.soma(2, 3))  # Saída: 5
print(modulo2.soma(2, 3))  # Saída: 5
```

### Escopo

O escopo de váriaveis dentro de um modulo segue as mesmas regras já vista em aulas anteriores.
Isto é, dentro de um módulo, as variáveis têm escopo global ou local.
* **Variáveis globais**: São definidas no nível do módulo e podem ser acessadas de qualquer lugar dentro do módulo.
* **Variáveis locais**: São definidas dentro de funções e só podem ser acessadas dentro da função onde foram definidas.

```python
# circulo.py

# Variável global
PI = 3.14159

def calcular_area(raio):
    # Variável local
    area = PI * raio ** 2
    return area

def calcular_circunferencia(raio):
    # Usando a variável global
    circunferencia = 2 * PI * raio
    return circunferencia
```

No caso, é importante ressaltar que a variável global `PI` também será acessivel por outros scripts ao importarmos esse modulo.

## \_\_name__ == \_\_main__

Em Python, o atributo `__name__` é uma variável especial que é automaticamente definida para o nome do módulo em que está sendo utilizado.
Quando um script Python é executado, o interpretador define `__name__` como `__main__` para o script que está sendo executado diretamente.

### Por que é importante?

O uso de \_\_name__ == "\_\_main__" permite que você escreva código que será executado apenas quando o arquivo .py for executado diretamente, e não quando importado como um módulo em outro script.
Isso é útil para separar o código que deve ser executado como um programa principal do código que é destinado a ser reutilizado em outros scripts.

### Exemplo

Considere o seguinte script main.py:

```python
def saudacao(nome):
    return f"Olá, {nome}!"

def main():
    print(saudacao("Alice"))

if __name__ == "__main__":
    main()
```

Neste exemplo, a função `main()` só será chamada se o script for executado diretamente.
Se o script for importado como um módulo em outro script, a função `main()` não será chamada automaticamente.

## Diretórios e Estrutura de Pacotes

Em Python, um `pacote` é uma pasta que contém múltiplos módulos e um arquivo especial chamado `__init__.py`.
Os pacotes são usados para organizar e estruturar grandes projetos em Python.
Eles ajudam a evitar conflitos de nomes e permitem uma hierarquia clara de módulos.

Por exemplo, considere a seguinte estrutura de diretórios:

```markdown
meu_pacote/
│
├── __init__.py
├── modulo1.py
└── modulo2.py
```

Aqui, `meu_pacote` é um pacote que contém dois módulos, `modulo1.py` e `modulo2.py`.

### \_\_init__.py

O arquivo `__init__.py` é um arquivo especial em pacotes Python. Ele pode estar vazio ou conter código de inicialização para o pacote.
Este arquivo é executado quando o pacote é importado e é usado para realizar qualquer configuração necessária para o pacote.

Por exemplo, o `__init__.py` pode definir variáveis globais, importar submódulos ou configurar o comportamento padrão do pacote.

```python
# __init__.py

print("Inicializando o pacote meu_pacote...")

# Definindo uma variável global no pacote
nome_pacote = "meu_pacote"
```

Ao importar o pacote meu_pacote, o código no `__init__.py` será executado.

## Localização de Pacotes no Sistema

### Path de Importação
O Python segue uma ordem específica ao procurar por módulos e pacotes. Esse processo é determinado pela variável de ambiente `sys.path`, que é uma lista de diretórios onde o interpretador Python procura por módulos.

### Locais Padrão de Busca
Os locais padrão de busca incluem:
- **Diretório atual**: O diretório em que o script em execução está localizado.
- **Diretórios do Python instalados**: Locais onde os módulos padrão estão instalados (como `/usr/lib/python3.9` no Linux).
- **Diretórios do usuário**: Locais onde pacotes instalados pelo usuário estão localizados (como `~/Library/Python/3.9/lib/python/site-packages` no macOS).

### Verificação do sys.path

Para verificar os diretórios atualmente incluídos em `sys.path`, você pode imprimir a variável:

```python
print(sys.path)
```

### Adicionando Locais Personalizados
Você também pode adicionar seus próprios diretórios à variável `sys.path` para que o Python os pesquise ao importar módulos. Isso pode ser útil ao desenvolver pacotes ou módulos personalizados que não estão instalados globalmente.

### Exemplo de Manipulação de `sys.path`
```python
import sys

# Adiciona um diretório personalizado ao path de importação
sys.path.append('/caminho/para/seu/pacote')

# Agora o Python procurará por módulos neste diretório ao importar
```

## Exercícios

### Módulo de Operações Matemáticas

Crie um módulo chamado operacoes_matematicas.py que contenha as seguintes funções:
* adicionar(a, b): Retorna a soma de a e b.
* subtrair(a, b): Retorna a subtração de b de a.
* multiplicar(a, b): Retorna a multiplicação de a por b.
* dividir(a, b): Retorna a divisão de a por b, tratando a divisão por zero.

Crie um script separado main.py que importe o módulo operacoes_matematicas e teste todas as funções com diferentes valores.

### Módulo de Manipulação de Strings

Crie um módulo chamado manipulacao_strings.py que contenha as seguintes funções:
* contar_vogais(texto): Retorna o número de vogais em texto.
* contar_consoantes(texto): Retorna o número de consoantes em texto.
* inverter_string(texto): Retorna a string texto invertida.

Crie um script separado main.py que importe o módulo manipulacao_strings e teste todas as funções com diferentes textos.