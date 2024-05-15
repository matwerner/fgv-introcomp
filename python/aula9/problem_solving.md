# Estratégias de Resolução de Problemas

Nesta aula, exploraremos a resolução de problemas em Python.
Aprenderemos a abordar desafios computacionais de forma estruturada, aplicando técnicas como `análise`, `decomposição` e `identificação de padrões`.
Este conhecimento é fundamental para desenvolver soluções eficientes em Python.

## Exemplo prático: Jogo da Forca

Para isso, vamos exemplificar as estratégias de resolução de problemas para desenvolver o jogo da forca.
Você será desafiado a criar este clássico jogo em Python, onde cada etapa nos ajudará a compreender como utilizar as técnicas acima para alcançar soluções eficientes.

### Enunciado

Você foi contratado para desenvolver um jogo da forca em Python.
O jogo deve começar escolhendo aleatoriamente uma palavra secreta de uma lista predefinida de palavras.
O jogador tem um número máximo de tentativas, por exemplo, 6, para adivinhar a palavra.
A cada rodada, o jogador insere uma letra e o jogo informa se a letra está na palavra secreta ou não.
O jogo continua até que o jogador adivinhe todas as letras da palavra ou não tenha mais tentativas restantes.

## 1. Análise

A análise é fundamental para entender completamente o problema e seus requisitos antes de começar a escrever código. Isso envolve ler cuidadosamente o enunciado do problema, identificar entradas e saídas, e compreender quaisquer restrições ou condições especiais.

### Exemplo: Implementação do Jogo da Forca

No caso do jogo da forca, nós podemos analisar o enunciado da questão e nos perguntar:

* Quais são as entradas do problema?\
A palavra a ser adivinhada e as letras fornecidas pelo jogador.

* Qual é a saída esperada?\
A visualização da palavra com as letras adivinhadas corretamente e uma indicação de quantas tentativas restam.

* Quais são as regras do jogo?\
Por exemplo, quantas tentativas o jogador tem, como a palavra é escolhida, etc.

## 2. Decomposição

A decomposição envolve dividir o problema em partes menores e mais gerenciáveis.
Isso simplifica o processo de resolução, permitindo que você resolva cada parte individualmente e depois combine as soluções para resolver o problema como um todo.

### Exemplo: Decomposição do Jogo da Forca

No contexto do jogo da forca, a decomposição envolve dividir o problema em partes menores e mais gerenciáveis, como:
1. **Inicialização do Jogo**\
Escolher uma palavra aleatória, definir o número máximo de tentativas, etc.
2. **Lógica de Adivinhação**\
Permitir que o jogador insira uma letra e verificar se ela está na palavra.
3. **Verificação de Letras**\
Verificar se a letra inserida pelo jogador está presente na palavra.
4. **Atualização da Visualização da Palavra**\
Mostrar a palavra com as letras adivinhadas corretamente e espaços para letras não reveladas.
5. **Controle de Tentativas Restantes**\
Atualizar o número de tentativas restantes e verificar se o jogador ainda pode continuar.

Dividir o problema dessa maneira simplifica a implementação e torna mais fácil entender e depurar o código.

## 3. Identificação de Padrões

Identificar padrões no problema pode ajudar a simplificar a resolução.
Isso pode incluir padrões matemáticos, algoritmos conhecidos ou estruturas de dados que se encaixam no problema.

### Exemplo: Identificação de Padrões no Jogo da Forca

Ao implementar o jogo da forca, é útil identificar padrões que possam simplificar a resolução do problema, como algoritmos para escolher palavras aleatórias, estruturas de dados para armazenar as letras adivinhadas, etc.

* **Algoritmo para Escolher Palavras Aleatórias**\
Podemos usar a biblioteca random para escolher aleatoriamente uma palavra de uma lista predefinida.
* **Estrutura de Dados para Armazenar Letras Adivinhadas**\
Podemos usar uma lista para armazenar as letras adivinhadas pelo jogador e atualizar dinamicamente a visualização da palavra com base nessa lista.

## Outros exemplos

Para práticar as ténicas vistas hoje, você pode pensar em como desenvolveria:
* Jogos de Tabuleiro: Batalha Naval, Conect 4, Damas, Xadrez;
* Jogos de Video Game: Tetris, Breakout, Space Invaders;
* Jogos de Cartas: Blackjack, Poker;
* Sistema de Agendamento: Consulta Médica, Reserva de Hotel;
* Sistema de E-mail: Detecção de Spam, Categorização;
* etc

Não é necessário pensar nas aplicações como um todo mas, por exemplo:
* No Xadrez, como especificar todas as posições nas quais uma peça pode se mover?
* No Tetris, como detectar que um tetraminó vai colidir com outro?
* Na reserva de hotel, como ver a disponibilidade de um quarto em um período especifico?
* Na detecção de spam, como verificar se um e-mail é ou não spam?

## Exercícios

### Jogo da Velha (Tic-Tac-Toe)

Você está desafiado a criar uma versão do jogo da velha em Python.
O jogo deve permitir que dois jogadores se alternem para fazer seus movimentos em um tabuleiro 3x3.
O primeiro jogador será representado pelo símbolo 'X' e o segundo jogador pelo símbolo 'O'.
O jogo deve verificar automaticamente se há um vencedor após cada movimento e encerrar quando um jogador ganhar ou houver um empate.
Além disso, o programa deve fornecer feedback ao jogador, indicando se o movimento é válido ou se uma casa já foi preenchida.

### Reserva de Quartos de Hotel

Você foi encarregado de criar um sistema de reserva de quartos de hotel em Python.
O sistema deve permitir que os clientes selecionem o período da reserva, o número de camas desejadas e o andar do hotel.

Requisitos:

* O sistema deve permitir que os clientes selecionem o período da reserva (* Considerar apenas periódos de 1 dia).
* Os clientes devem ser capazes de escolher o número de camas desejadas para o quarto.
* Os clientes devem poder selecionar o andar do hotel onde desejam ficar.
* O sistema deve verificar a disponibilidade de quartos para o período selecionado, o número de camas e o andar desejado.
* Se um quarto estiver disponível, o sistema deve confirmar a reserva e fornecer ao cliente um número de reserva único.
* Se não houver quartos disponíveis para as preferências selecionadas, o sistema deve informar ao cliente e oferecer opções alternativas, se disponíveis.