import math

def cidade_mais_proxima(pessoas, cidades):
    cidades_proximas = {}
    for pessoa, coordenadas_pessoa in pessoas.items():
        x_pessoa, y_pessoa = coordenadas_pessoa
        distancia_minima = float('inf')
        cidade_proxima = None
        for cidade, coordenadas_cidade in cidades.items():
            x_cidade, y_cidade = coordenadas_cidade
            distancia = math.sqrt((x_cidade - x_pessoa) ** 2 + (y_cidade - y_pessoa) ** 2)
            if distancia < distancia_minima:
                distancia_minima = distancia
                cidade_proxima = cidade
        cidades_proximas[pessoa] = cidade_proxima
    return cidades_proximas

# Teste seu código com o exemplo fornecido
pessoas = {'Alice': (1, 2), 'Bob': (3, 4), 'Charlie': (6, 8), 'David': (10, 10)}
cidades = {'A': (2, 3), 'B': (5, 5), 'C': (9, 9)}
cidades_proximas = cidade_mais_proxima(pessoas, cidades)
print(cidades_proximas)  # Deve retornar {'Alice': 'A', 'Bob': 'A', 'Charlie': 'C', 'David': 'C'}