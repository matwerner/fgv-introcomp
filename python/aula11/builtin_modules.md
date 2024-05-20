# Módulos Built-in

Python vem com uma biblioteca padrão rica em módulos que fornecem uma ampla gama de funcionalidades prontas para uso em várias áreas de desenvolvimento de software.

Aqui estão alguns módulos built-in comumente utilizados:

### os
Funções para interagir com o sistema operacional subjacente. Ele permite realizar operações como manipulação de arquivos, execução de comandos do sistema e manipulação de caminhos de arquivos.

### sys
Acesso a algumas variáveis ​​do interpretador Python e funções relacionadas ao sistema. Ele é frequentemente utilizado para configurar o comportamento do interpretador e manipular parâmetros da linha de comando.

### math
Funções matemáticas para operações comuns, como trigonometria, exponenciação, raiz quadrada, logaritmos, entre outras. Ele é útil para realizar cálculos complexos e manipulações numéricas.

### string
O módulo `string` fornece constantes e funções para manipulação de strings em Python. Ele inclui funções para formatação de strings, manipulação de caracteres, verificação de tipos de caracteres, entre outras operações úteis.

### random
O módulo `random` é utilizado para geração de números aleatórios em Python. Ele oferece uma variedade de funções para criar números aleatórios, embaralhar sequências e realizar seleções aleatórias.

### datetime
O módulo `datetime` fornece classes para manipulação de datas e horas em Python. Ele permite criar objetos de data e hora, realizar operações de cálculo de datas, formatar datas e horas para exibição, entre outras funcionalidades relacionadas a tempo.

### time
O módulo `time` fornece funções para trabalhar com tempo em Python. Ele permite medir o tempo de execução de programas, realizar operações relacionadas a temporização, como adições de tempo e suspensões, além de fornecer funções para trabalhar com timestamps e representações de tempo em segundos.

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

### Exemplo de Uso
Aqui está um exemplo simples que demonstra o uso de alguns desses módulos built-in:

```python
import os
import sys
import math
import string
import random
from datetime import datetime
import time

# Exemplo de uso dos módulos
print(os.listdir('.'))  # Lista os arquivos no diretório atual
print(sys.platform)  # Plataforma do sistema operacional
print(math.factorial(5))  # Fatorial de 5
print(string.ascii_lowercase)  # Alfabeto em minúsculas
print(random.choice(['a', 'b', 'c']))  # Escolha aleatória de uma letra
print(datetime.now())  # Data e hora atual
print(time.time())  # Timestamp atual em segundos
```

Este exemplo mostra como os diferentes módulos built-in podem ser utilizados para realizar uma variedade de tarefas, desde operações básicas de sistema até manipulação de datas e horas, cálculos matemáticos e geração de números aleatórios.

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