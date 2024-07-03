## Instruções Gerais

1. **Duração da Prova**:

    * A prova terá uma duração total de 3 horas (180 minutos).
    * Após submeter o questionário, você NÃO poderá resubmetê-lo. Certifique-se de que todos as questões estejam corretamente preenchidas antes de realizar a submissão.

2. **Pontuação Máxima**: A prova vale no total 10.5 pontos, mas a nota máxima atribuída será 10. Pontos excedentes não serão considerados.

3. **Ambiente de Desenvolvimento**:

    * Para as questões que envolvem implementação, você poderá utilizar IDEs voltadas para o desenvolvimento em Python, como PyCharm ou Visual Studio Code.
    * Não é permitido o uso de bibliotecas que não foram ensinadas durante as aulas, como pandas.
    * Bibliotecas como String, Math e Numpy podem ser utilizadas, caso desejado.

4. **Submissão do Código**:

    * Todo o código gerado durante a prova deve ser submetido ao final, junto com a submissão da prova.
    * Para submeter seu código, acesse a seção de "entrega de atividade" no EClass e selecione a tarefa "A2 - Python (Código)".
    * Detalhes sobre como o código deve ser submetido estão descritos na tarefa em si.
    * O prazo para entrega do código é equivalente ao prazo da prova, ou seja, dentro das 3 horas de duração.
    * **Atenção**: A não submissão do código das questões 5, 6 e 7 resultará na atribuição de nota zero para essas questões.

5. **Rascunhos**:

    * Folhas de papel serão disponibilizadas para rascunho.
    * Todos os rascunhos deverão ser entregues ao final da prova.
    * Por favor, escreva seu nome de forma legível em todas as folhas de rascunho utilizadas.

6. **Dúvidas**: Em caso de dúvidas quanto aos enunciados, basta avisar aos monitores em sala, que entraram em contato comigo.

### Mensagem Final

Desejo uma boa prova a todos!

## Questão 1

A respeito da ferramenta GIT, assinale as alternativas **VERDADEIRAS** abaixo:

- [V] Um "commit" representa um ponto no histórico do repositório.
- [V] Git armazena todo o histórico de mudanças de um repositório
- [V] O comando `git pull` é uma mistura dos comandos `fetch` e `merge`.
- [V] O comando `git checkout` pode ser usado para trocar de branch ou restaurar arquivos do histórico.
- [V] O comando `git merge` combina o histórico de dois branches.
- [F] GitHub é necessário para usar Git
- [F] Git automaticamente resolve todos os conflitos de merge.
- [F] O comando `git init` é usado para baixar um repositório remoto para a sua máquina local.
- [F] O comando `git clone` é usado para criar um novo repositório Git.
- [F] O comando `git pull` deve sempre ser executado antes do `git push`

## Questão 2

A respeito do bash, assinale as alternativas **VERDADEIRAS** abaixo:

- [V] O comando `sort teste.txt | uniq | wc -l` conta o número de linhas distintas presentes no arquivo "teste.txt".
- [V] O comando `cat teste.txt | grep "padrão"` mostra apenas as linhas do arquivo "teste.txt" que contêm o padrão especificado.
- [V] O comando `cd ..` retorna para o diretório pai do diretório atual.
- [V] O comando `ls .` exibe todos as pastas e arquivos presentes no diretório corrente
- [V] O comando `sed 's/palavra1/palavra2/g' teste.txt` substitui globalmente todas as ocorrências de "palavra1" por "palavra2" no arquivo "teste.txt".
- [F] Executar o comando `cat teste.txt teste.txt >> teste2x.txt` diversas vezes consecutivas não altera o conteudo do arquivo "teste2x.txt
- [F] O comando `uniq teste.txt` remove todas as linhas duplicadas do arquivo "teste.txt"
- [F] O comando `mkdir pasta1/pasta2/pasta3` cria todas as pastas necessárias, incluindo subpastas, se elas não existirem.

## Questão 3

A respeito do conteudo de Redes de Computadores visto em sala de aula, assinale as alternativas **VERDADEIRAS** abaixo:

- [V] TCP/IP é um conjunto de protocolos de comunicação usado para interconectar redes de computadores na Internet.
- [V] SSH usa chaves criptográficas para autenticação, proporcionando maior segurança em comparação com métodos de login tradicionais baseados em senha.
- [V] HTML é o formato de linguagem padrão usado na estruturação e formatação de páginas web, permitindo a troca de informações entre clientes (navegadores) e servidores web na World Wide Web.
- [V] O endereço IP é globalmente único em uma rede de computadores
- [F] SSH é usado exclusivamente para transferência de arquivos entre servidores remotos
- [F] GET, PUT, POST e DELETE são métodos padrão do protocolo TCP/IP
- [F] No protocolo HTTP, o status 5XX significa que uma requisição foi bem-sucedida.
- [F] HTTP é considerado um protocolo seguro para transferir páginas web e outros recursos na World Wide Web

## Questão 4

Você recebeu um arquivo CSV denominado `transacoes.csv`, contendo as operações financeiras de compra e venda de ações
de uma empresa durante um determinado período de tempo, onde existem apenas duas colunas denominadas **operação** e **valor**,
sendo que a coluna **operação** pode ter apenas dois valores: "venda" e "compra", enquanto **valor** representa um número inteiro correspondendo ao preço da ação durante a operação.

O seu objetivo é completar a função python abaixo que leia o arquivo de transações
e determine se o saldo daquele período foi positivo ou não.

```python
def saldo_positivo(nome_arquivo):
    # Bloco de código a ser implementado
    return saldo > 0
print(saldo_positivo('transacoes.csv'))
```

Por exemplo, considere as transações abaixo:
```
compra,100
venda,101
venda,102
```

Após processar essa lista, a função deveria retornar "True".

Assuma que o arquivo de transações sempre corretamente preenchido,
ou seja, não existe linhas com informações faltando ou no formato errado.

Marque todas as opções que implementam corretamente a função descrita acima:

a) Verdadeiro
```python
saldo = 0
with open(nome_arquivo) as arquivo:
    mapa = {'compra': -1, 'venda': 1}
    linha = arquivo.readline()
    while linha:
        operacao, valor = linha.strip().split(',')
        saldo += mapa[operacao] * int(valor)
        linha = arquivo.readline()
```

b) Verdadeiro
```python
with open(nome_arquivo, 'r') as arquivo:
    saldo = 0
    leitor = csv.reader(arquivo)
    for linha in leitor:
        valor = int(linha[1])
        if linha[0] == 'compra':
            saldo += -valor
        elif linha[0] == 'venda':
            saldo += valor
```

c) Verdadeiro
```python
vendas = sum([int(linha.split(',')[1]) for linha in open(nome_arquivo)
              if linha.split(',')[0] == 'venda'])
compras = sum([int(linha.split(',')[1]) for linha in open(nome_arquivo)
               if linha.split(',')[0] == 'compra'])
saldo = vendas - compras
```

d) Verdadeiro
```python
saldo = 0
with open(nome_arquivo, 'r+') as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        if linha[0] == 'venda':
            saldo += int(linha[1])
    for linha in leitor:
        if linha[0] == 'compra':
            saldo -= int(linha[1])
```

e) Falso
```python
transacoes = []
linhas = open(nome_arquivo, mode='r').read()
for linha in linhas:
    operacao, valor = linha.split(',')
    if operacao == 'compra':
        transacoes.append((-1, int(valor)))
    else:
        transacoes.append((1, int(valor)))
saldo = sum([op * val for op, val in transacoes])
```

f) Falso
```python
saldo = 0
arquivo = open(nome_arquivo, mode='r')
for linha in arquivo:
    operacao, valor = linha.strip().split(',')
    if linha[0] == 'compra':
        saldo -= int(valor)
for linha in arquivo:
    operacao, valor = linha.strip().split(',')
    if operacao == 'venda':
        saldo += int(valor)
arquivo.close()
```

## Questão 5

Considere o programa abaixo:

```python
def func_a(n):
    if n <= 0:
        return 1
    return 2 * func_b(n * 2)

def func_b(n):
    if n <= 0:
        return 2
    return 3 + func_c(n - 3)

def func_c(n):
    if n <= 0:
        return 3
    return -1 * func_a(n // 3)

print(func_c(11))
```

Assinale entre as opções a seguir, as afirmações verdadeiras:

- [V] `func_c(4)` retorna $-12$.
- [V] `func_a(2)` retorna $4$.
- [V] Trocar todos os caso bases `"if n <= 0:"` por `"if n == 0:"` pode causar um loop infinito.
- [F] Trocar `return 3 + func_c(n - 3)` por `return 3 + func_c(n)` pode causar um loop infinito.
- [F] `func_b(11)` eventualmente chama `func_a(3)` durante a recursão.
- [F] `func_c(11)` chama $3$ vezes a função `func_a(n)` ao longo da recursão


## Questão 6

A função abaixo deve receber um dicionário contendo a lista de compromissos de diferentes pessoas e a duração de um novo compromisso, 
e retornar as possíveis faixas de horário que esse compromisso pode ser marcado.
O dicionário de compromissos (denominado simplesmente como compromissos) possui
como chave o nome da pessoa e como valor uma lista de intervalos de tempo (início, fim)
representando os compromissos dessa pessoa em um dia.
A duração do novo compromisso é denominada duracao_reuniao.

Pressuposições:

* Cada intervalo de tempo é uma tupla de dois inteiros, onde o primeiro inteiro representa a hora de início e o segundo inteiro representa a hora de fim (ambos em formato de 24 horas).
* O dia começa às 00:00 e termina às 23:59.
* Os intervalos de tempo não se sobrepõem dentro das listas de compromissos individuais de cada pessoa.
* A nova reunião deve ocorrer dentro do mesmo dia.

### Exemplo

Por exemplo, dado o dicionário e a duração abaixo:
```python
compromissos = {
    'Alice': [(9, 10), (12, 13), (16, 18)],
    'Bob': [(10, 11), (12, 14), (14, 15)],
    'Carlos': [(9, 10), (15, 16), (18, 20)]
}
duracao_reuniao = 1
```

A função deveria retornar a lista:
```python
[(0, 9), (11, 12), (20, 24)]
```

O código abaixo, entretanto, contém erros e não funciona como esperado.
Marque as opções correspondentes às correções necessárias para que a função comporte-se como esperado.
O código final correto é obtido pela aplicação de todas as modificações sugeridas pelas opções selecionadas.

```python
(1) def encontrar_horarios_disponiveis_errado(compromissos, duracao_reuniao):
(2)     linha_do_tempo = set()
(3)     for pessoa, intervalos in compromissos.items():
(4)         for inicio, fim in intervalos:
(5)             for hora in range(inicio, fim):
(6)                 linha_do_tempo.add(hora)
(7)     h = 0
(8)     horarios_disponiveis = []
(9)     while h < 24:
(10)         if linha_do_tempo[h]:
(11)             h += 1
(12)             continue
(13)         d = h + 1
(14)         while d not in linha_do_tempo:
(15)             d += 1
(16)         if d - h >= duracao_reuniao:
(17)             horarios_disponiveis.append((h, d))
(18)         h += 1
(19)     return horarios_disponiveis
```

- [F] Substituir a linha (2) por `linha_do_tempo = []`
- [V] Substituir a linha (2) por `linha_do_tempo = [False] * 24`
- [F] Substituir a linha (6) por `linha_do_tempo.append(hora)`
- [V] Substituir a linha (6) por `linha_do_tempo[hora] = True`
- [F] Substituir a linha (10) por `if h in linha_do_tempo`
- [V] Substituir a linha (14) por `while d < 24 and not linha_do_tempo[d]`
- [F] Substituir a linha (14) por `while d < 24 and not linha_do_tempo[d] and d - h < duracao_reuniao`
- [F] Substituir a linha (16) por `if d > h + 1`
- [V] Substituir a linha (18) por `h = d + 1`
- [F] Substituir a linha (18) por `h += duracao_reuniao`

## Questão 7

O Automated Readability Index (ARI) é uma métrica projetada para quantificar a complexidade de um texto
com base na contagem de caracteres, palavras e sentenças.
Este índice fornece uma avaliação automatizada da dificuldade de leitura de um texto,
sendo fundamental para determinar sua adequação para diferentes públicos-alvo.
Quanto maior o valor da métrica, mais complexo é o texto.

### Cálculo da métrica ARI

O ARI é calculado usando a fórmula:

$$
ARI = 
4.71 \times \bigg(\frac{\#caracteres}{\#palavras}\bigg) 
+ 0.5 \times \bigg(\frac{\#palavras}{\#sentencas}\bigg) 
- 21.43 
$$

Onde:
* **#caracteres**: é o número total de caracteres no texto, considerando **APENAS números e letras** como caracteres válidos;
* **#palavras**: é o número total de palavras no texto, definidas como **sequências de caracteres válidos** separadas por espaços em branco. Caracteres especiais e pontuações **NÃO** são incluídos como parte das palavras;
* **#sentenças**: é o número total de sentenças no texto, identificadas como conjuntos de palavras separadas pelas pontuações ".", "?", e "!". Cada uma dessas pontuações indica o fim de uma sentença.

Observações:
* Considere que os textos fornecidos já estão normalizados para minúsculas e sem acentos;
* A sentença final pode ou não ser acompanhada de uma pontuação. Por exemplo, os textos "python" e "python." são formados por apenas uma sentença;
* Não existem sentenças sem caracteres válidos, ou seja, o texto "Python..." contém apenas uma sentença.

### Exemplo

Por exemplo, o texto:

```
o ari - um indice de legibilidade automatizado - calcula a complexidade de um texto.
```

possui:

```
#caracteres = 67
#palavras = 13
#sentencas = 1

ARI = 9.34
```

Já

```
python3 facilita a criacao de algoritmos. algoritmos eficientes melhoram o desempenho
```

possui:

```
#caracteres = 74
#palavras = 11
#sentencas = 2

ARI = 13.00
```

### Tarefa

Escreva uma função que calcule a complexidade de um texto baseado na métrica ARI.
Em seguida, dados os textos:

```python
T1 = "a nintendo e uma das empresas mais iconicas no mundo dos videogames, com uma historia que remonta a 1889, quando foi fundada como uma fabricante de cartas de baralho no japao! ao longo das decadas, a nintendo se reinventou inumeras vezes - eventualmente se estabelecendo como um dos principais nomes da industria de jogos eletronicos.. a empresa e conhecida por suas franquias de sucesso como mario, the legend of zelda e pokemon, que se tornaram parte integral da cultura pop. a nintendo tambem e reconhecida por suas inovacoes em hardware (desde o game boy e o nintendo ds ate o nintendo switch), que combina jogos de console com a portabilidade de um dispositivo movel."
T2 = "o playstation, desenvolvido pela sony, e uma das marcas de videogames mais populares do mundo!! lancado originalmente em 1994, o playstation revolucionou a industria com seus graficos em 3d e uma vasta biblioteca de jogos que atrairam milhoes de jogadores. a marca continuou a inovar com o lancamento de novos consoles, como o playstation 2 -- que se tornou o console mais vendido de todos os tempos -- e o playstation 4, que solidificou a sony como lider no mercado de jogos... alem dos consoles, a sony expandiu a marca playstation com servicos como o playstation network, que oferece jogos online, streaming de midia e uma comunidade global de jogadores."
T3 = "a marca xbox, criada pela microsoft, entrou no mercado de videogames em 2001 com o lancamento do xbox original. desde entao, a linha de consoles xbox tem se destacado por sua poderosa capacidade de hardware e uma forte enfase em servicos online, exemplificada pelo xbox live - que foi pioneira no jogo multiplayer online em consoles!!! com sucessos como o xbox 360 e o xbox one, a microsoft continuou a expandir o ecossistema xbox com iniciativas como o game pass,, um servico de assinatura que oferece acesso a uma vasta biblioteca de jogos. a mais recente geracao de consoles (o xbox series x e series s) reforca o compromisso da microsoft com inovacoes tecnologicas e uma experiencia de jogo integrada entre dispositivos"
```


selecione as opções verdadeiras abaixo:

- [V] T1 contem $545$ caracteres válidos
- [V] T2 contem $108$ palavras
- [V] T3 contem $4$ sentenças
- [V] $|ARI(T2) - ARI(T2)| \le 0.5$
- [F] $ARI(T3) \in [15.0, 16.0]$

## Questão 8

Caça Palavras é um jogo onde o objetivo é encontrar palavras escondidas dentro de uma grade de letras.
As palavras podem estar dispostas nas seguintes orientações:

* Horizontal (da esquerda para a direita)
* Vertical (de cima para baixo)
* Diagonal (da esquerda para a direita, de cima para baixo)
* Diagonal (da esquerda para a direita, de baixo para cima)

O tabuleiro é representado por uma matriz $M \times N$ de letras, onde:
* $M$ é o número de linhas;
* $N$ é o número de colunas;
* E cada entrada da matriz contém uma letra de 'A' a 'Z' (Estamos ignorando acentos).

### Exemplo de Tabuleiro e Palavras

Considere o seguinte tabuleiro de 5x5:

```python
tabuleiro = [
    ['P', 'B', 'C', 'D', 'E'],
    ['U', 'A', 'G', 'C', 'J'],
    ['S', 'I', 'N', 'I', 'T'],
    ['H', 'U', 'R', 'T', 'T'],
    ['F', 'V', 'W', 'X', 'Y']
]
```

Exemplos de palavras presentes no tabuleiro:

* **Horizontal (esquerda para direita)**: "INIT" (posição: (2,1) a (2,4))
* **Vertical (cima para baixo)**: "PUSH" (posição: (0,0) a (3,0))
* **Diagonal descendente (da esquerda para a direita, de cima para baixo)**: "GIT" (posição: (1,2) a (3,4))
* **Diagonal ascendente (da esquerda para a direita, de baixo para cima)**: "FUNC" (posição: (4,0) a (1,3))

Exemplo de uma palavra que não está no tabuleiro: "WHILE"

### Tarefa

Implemente a função `busca_palavra(tabuleiro, palavra)` que verifica se uma palavra está presente no tabuleiro.
A função deve retornar True se a palavra for encontrada e False caso contrário.

Em seguida, dado o seguinte tabuleiro de 30x30 abaixo, responda às seguinte perguntas:

```python
tabuleiro = [
	['B', 'V', 'J', 'U', 'W', 'M', 'M', 'X', 'U', 'P', 'M', 'A', 'B', 'A', 'B', 'Y', 'T', 'E', 'F', 'D', 'P', 'P', 'C', 'Z', 'P', 'K', 'F', 'B', 'E', 'H'],
	['D', 'I', 'P', 'L', 'U', 'C', 'E', 'F', 'X', 'J', 'U', 'B', 'E', 'A', 'L', 'O', 'P', 'G', 'R', 'H', 'O', 'S', 'B', 'E', 'W', 'G', 'F', 'M', 'S', 'J'],
	['E', 'H', 'Z', 'Y', 'E', 'N', 'T', 'G', 'Z', 'E', 'J', 'L', 'O', 'O', 'J', 'O', 'H', 'B', 'Q', 'V', 'F', 'V', 'I', 'L', 'C', 'J', 'Z', 'S', 'V', 'H'],
	['S', 'U', 'T', 'T', 'T', 'E', 'O', 'I', 'D', 'Z', 'L', 'D', 'B', 'S', 'X', 'L', 'F', 'F', 'K', 'Z', 'U', 'D', 'N', 'O', 'F', 'D', 'V', 'V', 'O', 'R'],
	['T', 'L', 'Q', 'Y', 'W', 'H', 'D', 'G', 'O', 'E', 'V', 'H', 'H', 'Q', 'Y', 'E', 'V', 'A', 'Q', 'F', 'Z', 'Y', 'J', 'S', 'A', 'P', 'Q', 'T', 'H', 'G'],
	['G', 'B', 'X', 'A', 'N', 'B', 'O', 'G', 'H', 'W', 'S', 'U', 'D', 'Z', 'M', 'A', 'U', 'T', 'R', 'U', 'O', 'C', 'A', 'R', 'I', 'Y', 'E', 'O', 'B', 'O'],
	['F', 'P', 'U', 'T', 'A', 'H', 'N', 'S', 'X', 'M', 'X', 'Y', 'Z', 'R', 'V', 'N', 'Y', 'D', 'Y', 'N', 'E', 'K', 'S', 'Q', 'I', 'J', 'M', 'U', 'M', 'K'],
	['T', 'I', 'O', 'F', 'K', 'K', 'F', 'U', 'O', 'S', 'B', 'G', 'Z', 'O', 'L', 'O', 'Q', 'Y', 'Q', 'C', 'B', 'X', 'H', 'B', 'B', 'E', 'K', 'T', 'E', 'S'],
	['J', 'L', 'X', 'I', 'V', 'K', 'M', 'Y', 'I', 'O', 'N', 'C', 'T', 'D', 'Y', 'N', 'X', 'Y', 'I', 'A', 'V', 'M', 'U', 'O', 'F', 'Q', 'I', 'S', 'K', 'S'],
	['A', 'H', 'J', 'B', 'K', 'R', 'L', 'G', 'S', 'L', 'K', 'G', 'P', 'R', 'O', 'G', 'R', 'A', 'M', 'O', 'C', 'A', 'O', 'I', 'W', 'R', 'K', 'C', 'D', 'I'],
	['R', 'I', 'I', 'A', 'B', 'X', 'L', 'V', 'G', 'O', 'I', 'T', 'U', 'I', 'Z', 'T', 'G', 'H', 'X', 'W', 'M', 'A', 'T', 'R', 'O', 'Z', 'U', 'D', 'J', 'E'],
	['C', 'L', 'V', 'V', 'C', 'M', 'F', 'U', 'D', 'Y', 'E', 'S', 'D', 'Z', 'J', 'H', 'E', 'Y', 'H', 'F', 'K', 'E', 'I', 'G', 'U', 'M', 'G', 'S', 'X', 'X'],
	['E', 'Z', 'W', 'P', 'C', 'D', 'A', 'E', 'B', 'N', 'K', 'S', 'T', 'H', 'A', 'C', 'A', 'C', 'S', 'K', 'L', 'G', 'L', 'F', 'G', 'A', 'Q', 'V', 'P', 'A'],
	['L', 'T', 'T', 'W', 'J', 'R', 'Y', 'P', 'T', 'L', 'T', 'F', 'D', 'A', 'M', 'H', 'N', 'G', 'W', 'M', 'T', 'A', 'Y', 'R', 'H', 'J', 'O', 'N', 'C', 'R'],
	['C', 'I', 'V', 'A', 'L', 'G', 'O', 'R', 'A', 'T', 'M', 'O', 'E', 'J', 'P', 'K', 'K', 'O', 'S', 'H', 'W', 'R', 'G', 'A', 'O', 'Z', 'E', 'Y', 'B', 'Y'],
	['K', 'U', 'J', 'C', 'R', 'V', 'J', 'Y', 'W', 'M', 'W', 'E', 'U', 'R', 'N', 'G', 'S', 'S', 'Z', 'N', 'W', 'K', 'B', 'Q', 'A', 'R', 'R', 'A', 'Y', 'I'],
	['O', 'A', 'U', 'F', 'T', 'F', 'B', 'L', 'W', 'Q', 'B', 'Z', 'B', 'P', 'G', 'W', 'A', 'B', 'D', 'Z', 'N', 'I', 'Q', 'R', 'E', 'B', 'H', 'T', 'Q', 'O'],
	['P', 'A', 'N', 'L', 'J', 'A', 'R', 'Z', 'Y', 'T', 'C', 'N', 'S', 'O', 'T', 'A', 'H', 'N', 'G', 'K', 'L', 'J', 'U', 'I', 'X', 'O', 'T', 'Y', 'Z', 'X'],
	['Q', 'D', 'N', 'V', 'N', 'Q', 'H', 'W', 'P', 'I', 'U', 'V', 'S', 'N', 'M', 'C', 'I', 'O', 'B', 'L', 'T', 'O', 'L', 'U', 'A', 'R', 'H', 'E', 'C', 'X'],
	['C', 'P', 'W', 'L', 'N', 'P', 'S', 'E', 'Y', 'E', 'Q', 'S', 'W', 'D', 'I', 'C', 'P', 'O', 'M', 'O', 'U', 'N', 'O', 'N', 'I', 'M', 'V', 'K', 'H', 'I'],
	['T', 'O', 'X', 'D', 'W', 'N', 'F', 'L', 'L', 'A', 'T', 'R', 'T', 'I', 'G', 'U', 'T', 'Z', 'C', 'E', 'T', 'K', 'R', 'P', 'J', 'M', 'P', 'L', 'E', 'U'],
	['N', 'N', 'A', 'N', 'A', 'Q', 'W', 'I', 'H', 'R', 'A', 'V', 'B', 'I', 'J', 'Q', 'Q', 'Y', 'C', 'L', 'Z', 'O', 'V', 'M', 'J', 'W', 'Q', 'S', 'P', 'L'],
	['P', 'E', 'D', 'W', 'U', 'B', 'H', 'A', 'O', 'G', 'X', 'J', 'W', 'Z', 'Q', 'V', 'R', 'X', 'M', 'D', 'A', 'W', 'U', 'G', 'Y', 'O', 'K', 'C', 'C', 'B'],
	['O', 'W', 'K', 'R', 'T', 'W', 'M', 'X', 'N', 'K', 'I', 'Q', 'U', 'T', 'R', 'U', 'S', 'C', 'P', 'Y', 'T', 'S', 'N', 'M', 'Z', 'U', 'K', 'R', 'P', 'O'],
	['S', 'R', 'Q', 'Z', 'O', 'D', 'V', 'X', 'J', 'F', 'I', 'V', 'Y', 'G', 'F', 'K', 'P', 'Q', 'C', 'M', 'A', 'I', 'S', 'Q', 'V', 'I', 'U', 'I', 'R', 'O'],
	['Z', 'Y', 'W', 'M', 'Y', 'B', 'S', 'Z', 'J', 'M', 'N', 'M', 'V', 'X', 'G', 'A', 'D', 'X', 'O', 'A', 'R', 'G', 'L', 'E', 'X', 'K', 'L', 'P', 'O', 'L'],
	['W', 'A', 'V', 'F', 'W', 'K', 'K', 'X', 'Z', 'B', 'J', 'Y', 'O', 'G', 'Z', 'Y', 'X', 'X', 'D', 'T', 'L', 'W', 'H', 'V', 'F', 'J', 'P', 'T', 'H', 'E'],
	['P', 'T', 'I', 'C', 'J', 'N', 'H', 'C', 'R', 'V', 'T', 'Z', 'C', 'R', 'A', 'K', 'C', 'E', 'S', 'Y', 'V', 'K', 'C', 'H', 'O', 'I', 'I', 'T', 'I', 'A'],
	['E', 'T', 'R', 'L', 'G', 'R', 'P', 'R', 'P', 'B', 'Y', 'B', 'J', 'M', 'J', 'O', 'W', 'Q', 'M', 'L', 'R', 'X', 'Q', 'P', 'B', 'F', 'P', 'K', 'E', 'N'],
	['W', 'F', 'N', 'F', 'U', 'L', 'F', 'Z', 'X', 'F', 'H', 'P', 'H', 'S', 'J', 'T', 'H', 'H', 'Q', 'Z', 'D', 'T', 'H', 'P', 'F', 'S', 'X', 'L', 'S', 'O'],
]
```

- [V] A palavra 'BYTE' esta presente no caça palavras e se encontra na orientação horizontal
- [V] A palavra 'BOOLEANO' esta presente no caça palavras e se encontra na orientação vertical
- [V] A palavra 'STRING' esta presente no caça palavras e se encontra na orientação diagonal ascendente
- [V] A palavra 'LISTA' esta presente no caça palavras e se encontra na orientação diagonal descendente
- [F] A palavra 'ARRAY' esta presente no caça palavras e se encontra na orientação vertical
- [F] A palavra 'ALGORITMO' não esta presente no caça palavras
