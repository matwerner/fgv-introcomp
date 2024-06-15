def encontrar_colisoes(intervalos):
    colisoes = set()
    for nome1, intervalo1 in intervalos.items():
        for nome2, intervalo2 in intervalos.items():
            # Se os nomes forem iguais, não faz sentido comparar
            if nome1 == nome2:
                continue
            # Se os intervalos não se sobrepõem, não há colisão
            inicio1, fim1 = intervalo1
            inicio2, fim2 = intervalo2
            if inicio1 > fim2 or inicio2 > fim1:
                continue
            # Se a colisão já foi registrada, não registra novamente
            elif (nome1, nome2) in colisoes or (nome2, nome1) in colisoes:
                continue
            colisoes.add((nome1, nome2))
    return colisoes

# Exemplo de uso
intervalos = {'A': [1, 5], 'B': [3, 7], 'C': [7, 10], 'D': [15, 18]}
respostas = encontrar_colisoes(intervalos)
print(respostas)
