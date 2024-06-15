def propagar_infeccao(m, n, polos_de_infeccao):
    # Inicializa a matriz com zeros (todas células saudáveis)
    matriz = [[0 for _ in range(n)]
              for _ in range(m)]

    # Para cada polo de infecção, marque as células dentro do raio como infectadas
    for x, y, r in polos_de_infeccao:
        min_x = max(0, x - r)
        max_x = min(m, x + r + 1)
        for dx in range(min_x, max_x):
            i = dx
            min_y = max(0, y - r)
            max_y = min(n, y + r + 1)
            for dy in range(min_y, max_y):
                j = dy
                if (x - dx) ** 2 + (y - dy) ** 2 <= r ** 2:
                    matriz[i][j] = 1

    return matriz

# Teste o exemplo fornecido
m = 6
n = 6
polos_de_infeccao = [(2, 2, 1), (4, 4, 2)]
resultado = propagar_infeccao(m, n, polos_de_infeccao)
for linha in resultado:
    print(' '.join(map(str, linha)))