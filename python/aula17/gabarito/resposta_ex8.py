def movimentos_rainha(posicao_inicial):
    linha_inicial, coluna_inicial = posicao_inicial
    linha_inicial -= 1  # Ajuste para índice de matriz (0 a 7)
    coluna_inicial -= 1  # Ajuste para índice de matriz (0 a 7)
    
    tabuleiro = [[0 for _ in range(8)] for _ in range(8)]
    
    # Marca a linha e a coluna
    for i in range(8):
        tabuleiro[linha_inicial][i] = 1
        tabuleiro[i][coluna_inicial] = 1

    # Marca as diagonais
    for i in range(8):
        for j in range(8):
            if abs(linha_inicial - i) == abs(coluna_inicial - j):
                tabuleiro[i][j] = 1

    # A posição inicial da rainha também é marcada
    tabuleiro[linha_inicial][coluna_inicial] = 1
    
    return tabuleiro

# Teste da função
posicao_inicial = (4, 4)
resultado = movimentos_rainha(posicao_inicial)
for linha in resultado:
    print(linha)