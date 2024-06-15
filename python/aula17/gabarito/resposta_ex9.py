def montar_tabuleiro(n, pecas):
    # Inicializa o tabuleiro vazio
    tabuleiro = [[0 for _ in range(n)] for _ in range(n)]
    
    # Função auxiliar para verificar se a peça cabe no tabuleiro
    def cabe_peca(tamanho, orientacao, linha, coluna):
        if orientacao == "H":
            if coluna + tamanho > n:  # Verifica se a peça ultrapassa o limite do tabuleiro
                return False
            for j in range(coluna, coluna + tamanho):
                if tabuleiro[linha][j] != 0:  # Verifica sobreposição
                    return False
        elif orientacao == "V":
            if linha + tamanho > n:  # Verifica se a peça ultrapassa o limite do tabuleiro
                return False
            for i in range(linha, linha + tamanho):
                if tabuleiro[i][coluna] != 0:  # Verifica sobreposição
                    return False
        return True
    
    # Função auxiliar para posicionar a peça no tabuleiro
    def posicionar_peca(tamanho, orientacao, linha, coluna, id_peca):
        if orientacao == "H":
            for j in range(coluna, coluna + tamanho):
                tabuleiro[linha][j] = id_peca
        elif orientacao == "V":
            for i in range(linha, linha + tamanho):
                tabuleiro[i][coluna] = id_peca
    
    # Tenta posicionar cada peça no tabuleiro
    for id_peca, (tamanho, orientacao, linha, coluna) in enumerate(pecas, start=1):
        if not cabe_peca(tamanho, orientacao, linha, coluna):
            return None  # Retorna None se alguma peça não puder ser posicionada corretamente
        posicionar_peca(tamanho, orientacao, linha, coluna, id_peca)
    
    return tabuleiro

# Testando a função com o exemplo fornecido
n = 5
pecas = [(3, "H", 1, 1), (1, "V", 0, 3), (4, "H", 2, 0)]
resultado = montar_tabuleiro(n, pecas)
if resultado is None:
    print("Não foi possível montar o tabuleiro.")
    exit()

for linha in resultado:
    print(linha)