pedidos = []
with open('pedidos_produtos.csv') as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas[1:]: # Ignora o cabeçalho
        # Strip é para remover o '\n' no final da linha
        pedido_id, categoria_id, categoria_nome, valor = linha.strip().split(',')
        pedidos.append((pedido_id, categoria_id, categoria_nome, int(valor)))
print("Pedidos: ", len(pedidos))
print()

produtos_unicos = {pedido[1] for pedido in pedidos}
print("Produtos unicos: ", len(produtos_unicos))
print()

valores = [pedido[3] for pedido in pedidos]
print("Faturamento: ", sum(valores))
print()

# Categoria com mais pedidos / maior faturamento
categorias_contador = {}
for pedido in pedidos:
    categoria = pedido[2]
    if categoria not in categorias_contador:
        categorias_contador[categoria] = 0
    # Pedido
    # categorias_contador[categoria] += 1
    # Faturamento
    categorias_contador[categoria] += pedido[3]

print('Categorias:')
categorias_contador = sorted(categorias_contador.items(), key=lambda x: x[1], reverse=True)
for categoria, total in categorias_contador:
    print(f"{categoria}: {total}")
