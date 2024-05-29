# Exercícios

## Pacotes

1. Criação de Pacotes e Módulos:

    * Crie um diretório chamado `"processamento_texto"`.
    * Dentro deste diretório, crie três arquivos:
        - `string_utils.py`
        - `word_utils`
        - `__init__.py`
    * No arquivo `string_utils.py`, defina funções para contar `vogais`, `consoantes`, `digitos` e `pontuações`.
    * No arquivo `word_utils.py`, defina funções para `contar palavras` e `retornar um conjunto de palavras únicas.` em uma string.
    * No arquivo `__init__.py`, importe todas as funções dos módulos `string_utils.py` e `word_utils` para que elas possam ser acessadas diretamente a partir do pacote.

2. Importação e Uso do Pacote:

    * Fora do diretório `"processamento_texto"`, crie um programa Python chamado `main.py`.
    * Importe o pacote `"processamento_texto"`.
    * Use as funções do pacote para realizar operações textuais e imprima os resultados.

## Modulos

3. Escreva uma programa que solicita ao usuário que forneça o caminho para um diretório contendo arquivos de aulas.
O programa então deve utilizar o pacote `os` para listar todos os arquivos encontrados no diretório e exibi-los em ordem alfabética.

    O programa deve seguir as seguintes etapas:

        * Solicite ao usuário que digite o caminho para o diretório de aulas.
        * Verifique se o diretório fornecido existe utilizando os.path.exists().
            OBS: Se o diretório não existir, exiba uma mensagem informando que o diretório não foi encontrado e encerre o programa.
        * Liste todos os arquivos encontrados no diretório utilizando os.listdir() ou os.walk().
        * Exiba os nomes dos arquivos em ordem alfabética.

4. Desenvolva uma função que gere uma senha aleatória com uma combinação de letras, números e caracteres especiais.\
    Utilizar função `random.choices()` e variáveis `string.ascii_lowercase`, `string.digits` e `string.punctuation`.

## Numpy

5. Refaça a questão 5 da lista 2 (Aula 10)

## Leitura e Escrita de Arquivo

6. Dado o arquivo "noticia.txt":

    * Exiba o conteúdo do arquivo no terminal.
    * Conte o número de caracteres no arquivo.
    * Conte o número de palavras no arquivo.

    OBS: Considere uma palavra como qualquer conjunto de caracteres entre espaços em branco ou quebras de linha (\n).

7. Dado o arquivo "notas.csv":

    * Exiba cada linha do arquivo no terminal.
    * Calcule a média das notas de cada aluno.
    * Crie um novo arquivo chamado `"notas_atualizado.csv"` contendo todas as informações do arquivo original, além de uma nova coluna `"nota_final"` com as médias calculadas.
    * Exiba a média da turma na `"nota1"`, `"nota2"` e `"nota_final"`. Utilizar as funções `numpy.array` e `numpy.mean`

## Tratamento de Erro:

8. Escreva um programa que solicite ao usuário para digitar um número e o imprima.
9. Modifique o programa anterior para lidar com a situação em que o usuário digita algo que não é um número.
10. Escreva uma função que abre um arquivo e imprime seu conteúdo. Certifique-se de que o programa lida com a situação em que o arquivo não existe.
11. Modifique a função anterior para lidar com a situação em que o arquivo está vazio.