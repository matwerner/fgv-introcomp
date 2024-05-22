# Módulos Built-in

Python vem com uma biblioteca padrão rica em módulos que fornecem uma ampla gama de funcionalidades prontas para uso em várias áreas de desenvolvimento de software.

Aqui estão alguns módulos built-in comumente utilizados:

### os
Funções para interagir com o sistema operacional subjacente. Ele permite realizar operações como manipulação de arquivos, execução de comandos do sistema e manipulação de caminhos de arquivos.

```python
import os

def list_files_in_directory(directory):
    return os.listdir(directory)

# Example usage
directory_path = "."
print(list_files_in_directory(directory_path))
```

### sys
Acesso a algumas variáveis ​​do interpretador Python e funções relacionadas ao sistema. Ele é frequentemente utilizado para configurar o comportamento do interpretador e manipular parâmetros da linha de comando.

```python
import sys

def print_python_version():
    print("Python version:", sys.version)

# Example usage
print_python_version()
```

### math
Funções matemáticas para operações comuns, como trigonometria, exponenciação, raiz quadrada, logaritmos, entre outras. Ele é útil para realizar cálculos complexos e manipulações numéricas.

```python
import math

def calculate_circle_area(radius):
    return math.pi * (radius ** 2)

# Example usage
radius = 5
print(f"The area of the circle with radius {radius} is {calculate_circle_area(radius):.2f}")
```

### string
O módulo `string` fornece constantes e funções para manipulação de strings em Python. Ele inclui funções para formatação de strings, manipulação de caracteres, verificação de tipos de caracteres, entre outras operações úteis.

```python
import string

def is_palindrome(s):
    # Remove punctuation and convert to lowercase
    s = s.translate(str.maketrans('', '', string.punctuation)).replace(" ", "").lower()
    return s == s[::-1]

# Example usage
word = "A man, a plan, a canal, Panama"
print(f"'{word}' is a palindrome: {is_palindrome(word)}")
```

### random
O módulo `random` é utilizado para geração de números aleatórios em Python. Ele oferece uma variedade de funções para criar números aleatórios, embaralhar sequências e realizar seleções aleatórias.

```python
import random
import string

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage
password_length = 12
print(f"Generated password: {generate_random_password(password_length)}")
```

### datetime
O módulo `datetime` fornece classes para manipulação de datas e horas em Python. Ele permite criar objetos de data e hora, realizar operações de cálculo de datas, formatar datas e horas para exibição, entre outras funcionalidades relacionadas a tempo.

```python
from datetime import datetime

def get_current_datetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Example usage
print(f"Current date and time: {get_current_datetime()}")
```

### time
O módulo `time` fornece funções para trabalhar com tempo em Python. Ele permite medir o tempo de execução de programas, realizar operações relacionadas a temporização, como adições de tempo e suspensões, além de fornecer funções para trabalhar com timestamps e representações de tempo em segundos.

```python
import time

def sample_function():
    time.sleep(2)  # Simulate a delay

def measure_execution_time():
    start_time = time.time()
    sample_function()
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

# Example usage
print(f"Execution time: {measure_execution_time():.2f} seconds")
```

### E muitas outras

* json
* re
* collections
* itertools
* functools
* operator
* subprocess
* argparse
* logging
* unittest
* shutil
* sqlite3
* pathlib

## Por garantia...

Apenas para deixar claro, tanto na disciplina quanto na vida profissional, não é esperado que você saiba de cor todas as funcionalidades possíveis e imagináveis disponíveis por aí.
O crucial é compreender quais funcionalidades e pacotes uma linguagem de programação oferece, de modo que você saiba onde buscar as soluções quando necessário. O mais importante é desenvolver a habilidade de encontrar e aplicar a funcionalidade certa para resolver os problemas que você enfrenta. Isso inclui saber como consultar a documentação, utilizar recursos de busca e se apoiar na comunidade de desenvolvedores para encontrar as melhores práticas e soluções eficientes.


## Exercícios

Pacote os:
* Escreva um programa que liste todos os arquivos em um diretório específico.
* Crie uma função que verifique se um determinado arquivo existe em um diretório.
* Desenvolva um script que renomeie todos os arquivos em um diretório, substituindo espaços por underscores.

Pacote sys:
* Escreva um programa que imprima informações sobre a versão do Python em execução.
* Crie um script que receba argumentos da linha de comando e os imprima na tela.
* Desenvolva uma função que determine se o script está sendo executado em um sistema operacional Windows ou Unix-like.

Pacote math:
* Implemente uma função para calcular a área de um círculo dado o raio.
* Desenvolva um programa que calcule o fatorial de um número fornecido pelo usuário.
* Escreva um script que calcule a hipotenusa de um triângulo retângulo dados os comprimentos dos catetos.

Pacote random:
* Crie um jogo de adivinhação onde o computador escolhe um número aleatório e o jogador tenta adivinhar.
* Desenvolva uma função que gere uma senha aleatória com uma combinação de letras, números e caracteres especiais.
* Escreva um programa que embaralhe uma lista de palavras e as imprima em ordem aleatória.