def criar_tabuleiro():
    return [[' ' for _ in range(3)] for _ in range(3)]

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print('|'.join(linha))
        print('-+-+-')

def fazer_movimento(tabuleiro, linha, coluna, jogador):
    if tabuleiro[linha][coluna] == ' ':
        tabuleiro[linha][coluna] = jogador
        return True
    else:
        print("Posição já preenchida. Tente novamente.")
        return False

def verificar_vitoria(tabuleiro, jogador):
    for i in range(3):
        if all([tabuleiro[i][j] == jogador for j in range(3)]) or \
           all([tabuleiro[j][i] == jogador for j in range(3)]):
            return True
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador or \
       tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True
    return False

def verificar_empate(tabuleiro):
    for linha in tabuleiro:
        for celula in linha:
            if celula == ' ':
                return False
    return True

def jogo_da_velha():
    tabuleiro = criar_tabuleiro()
    jogadores = ['X', 'O']
    jogador_atual = 0

    while True:
        imprimir_tabuleiro(tabuleiro)
        linha = int(input("Jogador {} - Escolha a linha (0, 1, 2): ".format(jogadores[jogador_atual])))
        coluna = int(input("Jogador {} - Escolha a coluna (0, 1, 2): ".format(jogadores[jogador_atual])))
        
        if fazer_movimento(tabuleiro, linha, coluna, jogadores[jogador_atual]):
            if verificar_vitoria(tabuleiro, jogadores[jogador_atual]):
                imprimir_tabuleiro(tabuleiro)
                print("Parabéns! Jogador {} venceu!".format(jogadores[jogador_atual]))
                break
            elif verificar_empate(tabuleiro):
                imprimir_tabuleiro(tabuleiro)
                print("Empate!")
                break
            jogador_atual = (jogador_atual + 1) % 2

jogo_da_velha()