# Função para criar e preencher a matriz na orientação horizontal
def preencher_horizontal():
    matriz = [[0]*5 for _ in range(5)]
    count = 1
    for i in range(5):
        for j in range(5):
            matriz[i][j] = count
            count += 1
    return matriz

# Função para criar e preencher a matriz na orientação vertical
def preencher_vertical():
    matriz = [[0]*5 for _ in range(5)]
    count = 1
    for j in range(5):
        for i in range(5):
            matriz[i][j] = count
            count += 1
    return matriz

# Função para criar e preencher a matriz na diagonal da esquerda para a direita
def preencher_diagonal():
    matriz = [[0]*5 for _ in range(5)]
    count = 1
    for diagonal in range(0, 9):
        for j in range(5):
            for i in range(5):
                if i + j == diagonal:
                    matriz[i][j] = count
                    count += 1
    return matriz

# Função para exibir a matriz
def imprimir_matriz(matriz):
    for linha in matriz:
        print(" ".join(str(numero).rjust(2) for numero in linha))

# Preencher e imprimir as matrizes
print("Matriz com orientação horizontal:")
matriz_horizontal = preencher_horizontal()
imprimir_matriz(matriz_horizontal)

print("\nMatriz com orientação vertical:")
matriz_vertical = preencher_vertical()
imprimir_matriz(matriz_vertical)

print("\nMatriz em zique-zaque:")
matriz_diagonal = preencher_diagonal()
imprimir_matriz(matriz_diagonal)
