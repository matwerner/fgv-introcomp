tabuleiro = [
    ['A','B','.','A','D','A','D','C','D','B','B','A','A','.','.','B','A','C','D','D','.','.','.','D','A','D','B','C','B','.'],
    ['D','A','D','A','B','B','.','B','C','C','D','.','A','B','A','.','D','C','.','B','C','A','A','B','C','D','.','B','A','D'],
    ['C','B','A','C','.','.','B','D','A','.','D','D','.','C','A','B','A','A','A','.','.','A','D','B','B','D','.','C','.','.'],
    ['B','.','D','.','C','C','C','B','.','.','C','D','C','D','A','B','.','.','C','A','.','B','C','C','B','.','C','B','.','A'],
    ['D','C','.','.','A','D','B','.','A','D','.','.','A','C','B','A','A','A','B','A','.','A','.','.','A','C','A','D','.','B'],
    ['B','B','.','.','A','B','A','.','C','C','C','B','A','C','.','.','.','.','A','.','.','C','A','.','B','.','.','.','D','C'],
    ['C','.','B','A','C','A','.','.','.','D','C','C','A','.','D','.','B','B','.','C','D','A','D','A','.','C','B','C','.','B'],
    ['D','.','.','B','A','B','C','D','.','.','.','D','B','C','A','.','.','A','.','.','C','.','D','C','A','C','.','D','C','C'],
    ['B','.','C','D','C','B','.','C','C','B','A','D','D','.','.','B','A','.','B','B','D','D','D','.','D','C','.','C','C','B'],
    ['C','.','C','B','C','.','.','.','D','.','D','A','.','A','.','B','C','A','B','A','B','.','.','C','A','C','C','D','.','B'],
    ['D','.','A','D','.','A','.','.','D','.','.','B','D','A','A','C','.','B','D','B','A','B','D','.','A','.','C','B','C','.'],
    ['B','.','.','B','.','C','.','B','A','D','D','A','A','.','B','A','C','B','D','.','C','.','A','D','.','A','D','D','D','.'],
    ['C','.','.','.','.','.','C','.','A','.','.','A','.','B','C','C','.','.','C','C','.','D','C','C','C','.','.','B','.','.'],
    ['.','.','.','.','.','D','D','.','.','C','D','D','B','.','C','D','A','B','.','.','C','.','.','.','.','.','A','D','C','C'],
    ['A','C','D','B','C','A','C','B','D','B','D','A','A','.','C','A','.','.','B','.','A','B','A','.','.','D','.','A','D','.'],
    ['.','C','.','.','B','.','D','.','B','D','C','C','.','D','.','B','D','A','D','.','D','D','C','A','.','.','A','C','A','.'],
    ['A','C','.','B','C','D','.','C','.','B','.','.','.','.','.','.','B','B','A','B','C','D','.','D','.','.','.','D','A','B'],
    ['A','B','A','.','D','.','B','C','.','C','D','A','B','.','C','.','.','.','D','.','C','.','D','.','C','.','.','.','.','.'],
    ['.','D','D','C','B','D','A','B','.','.','D','.','D','D','D','.','.','D','.','.','C','D','.','.','.','C','.','C','A','A'],
    ['.','C','.','.','.','.','B','.','.','B','C','D','B','B','.','B','A','.','A','D','D','B','.','D','B','D','.','.','B','C'],
    ['B','A','A','D','A','.','.','D','A','B','.','D','.','.','A','.','B','A','A','.','.','.','C','A','A','A','.','B','A','.'],
    ['.','D','B','D','C','D','C','.','B','A','.','.','C','B','A','.','.','B','.','.','D','C','D','.','B','C','C','B','B','A'],
    ['C','C','B','.','C','A','C','.','A','C','A','A','C','A','B','C','A','D','B','.','A','.','A','.','D','C','.','D','B','D'],
    ['D','B','C','B','.','B','.','B','C','.','.','.','.','C','A','D','A','A','.','D','C','B','D','A','.','.','C','D','D','.'],
    ['C','.','D','D','C','B','C','.','.','D','.','.','C','D','D','A','.','.','.','.','.','A','.','C','C','C','.','B','A','A'],
    ['B','B','.','B','.','.','.','.','D','D','A','A','.','B','A','A','.','D','B','.','.','.','C','.','B','A','B','B','C','B'],
    ['D','D','A','.','C','C','.','D','.','C','.','C','B','A','B','.','.','A','A','A','.','B','D','.','C','.','C','.','B','C'],
    ['B','D','A','A','A','.','B','.','C','A','.','C','D','B','.','C','B','.','B','A','C','B','A','A','B','D','B','C','.','B'],
    ['.','.','.','A','B','D','.','.','A','C','B','D','.','B','D','B','C','D','A','B','B','A','B','D','D','.','.','.','C','D'],
    ['B','.','.','D','D','B','D','.','D','B','D','B','A','D','C','A','A','A','D','.','D','D','.','C','D','.','.','B','C','A']
]

TAM_SEQ = 4 # Tamanho da sequencia para ganhar

# Pega todos os jogadores
jogadores = {jogador for linha in tabuleiro for jogador in linha}

# Verifica linha
for i in range(30):
    # Verifica cada jogador
    for jogador in jogadores:
        if jogador == '.':
            continue

        # Opção 1 - Verifica elemento a elemento da sequencia
        for j in range(30-TAM_SEQ+1): # Ultima possibilidade são os indices 26, 27, 28, 29
            ganhou = True
            for k in range(TAM_SEQ):
                if tabuleiro[i][j+k] != jogador:
                    ganhou = False
            if ganhou:
                print(f'Jogador {jogador} ganhou!')
        
        # Opção 2 - Verifica se a "AAAA" está na string linha
        # linha = ''.join(tabuleiro[i])
        # if jogador*TAM_SEQ in linha:
        #     print(f'Jogador {jogador} ganhou!')

# Verifica coluna
for j in range(30):
    # Verifica cada jogador
    for jogador in jogadores:
        if jogador == '.':
            continue

        # Opção 1 - Verifica elemento a elemento da sequencia
        for i in range(30-TAM_SEQ+1): # Ultima possibilidade são os indices 26, 27, 28, 29
            ganhou = True
            for k in range(TAM_SEQ):
                if tabuleiro[i+k][j] != jogador:
                    ganhou = False
            if ganhou:
                print(f'Jogador {jogador} ganhou!')
        
        # Opção 2 - Verifica se a "AAAA" está na string coluna
        # coluna = ''.join([tabuleiro[i][j] for i in range(30)])
        # if jogador*TAM_SEQ in coluna:
        #     print(f'Jogador {jogador} ganhou!')

# Verifica número de posições vazias na coluna 4
contador = 0
for i in range(30):
    if tabuleiro[i][3] == '.':
        contador += 1
print(contador)

# Verifica número de jogadas do jogador 'A'
contador = 0
for i in range(30):
    for j in range(30):
        if tabuleiro[i][j] == 'A':
            contador += 1
print(contador)