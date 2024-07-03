matriz = [
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

def busca_horizontal(tabuleiro, palavra):
    num_linhas = len(tabuleiro)
    num_colunas = len(tabuleiro[0])
    # Percorre o tabuleiro
    for i in range(num_linhas):
        for j in range(num_colunas):
            # Verifica se o primeiro caractere da palavra está na posição atual
            if tabuleiro[i][j] != palavra[0]:
                continue
            # Pega um pedaço horizontal do tabuleiro com o mesmo tamanho da palavra
            pedaco_tabuleiro = tabuleiro[i][j:j + len(palavra)]
            if pedaco_tabuleiro == list(palavra):
                return True
    return False

def busca_vertical(tabuleiro, palavra):
    num_linhas = len(tabuleiro)
    num_colunas = len(tabuleiro[0])
    # Percorre o tabuleiro
    for i in range(num_linhas):
        for j in range(num_colunas):
            # Verifica se o primeiro caractere da palavra está na posição atual
            if tabuleiro[i][j] != palavra[0]:
                continue
            pedaco_tabuleiro = []
            # Pega um pedaço vertical do tabuleiro com o mesmo tamanho da palavra
            for k in range(len(palavra)):
                # Verifica se a palavra cabe na vertical
                if i + k >= num_linhas:
                    break
                pedaco_tabuleiro.append(tabuleiro[i + k][j])
            if pedaco_tabuleiro == list(palavra):
                return True
    return False

def busca_diagonal_descendente(tabuleiro, palavra):
    num_linhas = len(tabuleiro)
    num_colunas = len(tabuleiro[0])
    # Percorre o tabuleiro
    for i in range(num_linhas):
        for j in range(num_colunas):
            # Verifica se o primeiro caractere da palavra está na posição atual
            if tabuleiro[i][j] != palavra[0]:
                continue
            # Pega um pedaço diagonal descendente do tabuleiro com o mesmo tamanho da palavra
            pedaco_tabuleiro = []
            for k in range(len(palavra)):
                # Verifica se a palavra cabe na diagonal descendente
                if i + k >= num_linhas or j + k >= num_colunas:
                    break
                pedaco_tabuleiro.append(tabuleiro[i + k][j + k])
            if pedaco_tabuleiro == list(palavra):
                return True

def busca_diagonal_ascendente(tabuleiro, palavra):
    num_linhas = len(tabuleiro)
    num_colunas = len(tabuleiro[0])
    # Percorre o tabuleiro
    for i in range(num_linhas):
        for j in range(num_colunas):
            # Verifica se o primeiro caractere da palavra está na posição atual
            if tabuleiro[i][j] != palavra[0]:
                continue
            # Pega um pedaço diagonal ascendente do tabuleiro com o mesmo tamanho da palavra
            pedaco_tabuleiro = []
            for k in range(len(palavra)):
                # Verifica se a palavra cabe na diagonal ascendente
                if i - k < 0 or j + k >= num_colunas:
                    break
                pedaco_tabuleiro.append(tabuleiro[i - k][j + k])
            if pedaco_tabuleiro == list(palavra):
                return True
    return False

def busca_palavra(tabuleiro, palavra):
    if busca_horizontal(tabuleiro, palavra):
        return f"Encontrou {palavra} na horizontal"
    if busca_vertical(tabuleiro, palavra):
        return f"Encontrou {palavra} na vertical"
    if busca_diagonal_descendente(tabuleiro, palavra):
        return f"Encontrou {palavra} na diagonal descendente"
    if busca_diagonal_ascendente(tabuleiro, palavra):
        return f"Encontrou {palavra} na diagonal ascendente"
    return f"Não encontrou {palavra}"

print(busca_palavra(matriz, "BYTE"))
print(busca_palavra(matriz, "BOOLEANO"))
print(busca_palavra(matriz, "STRING"))
print(busca_palavra(matriz, "LISTA"))
print(busca_palavra(matriz, "ARRAY"))
print(busca_palavra(matriz, "ALGORITMO"))
