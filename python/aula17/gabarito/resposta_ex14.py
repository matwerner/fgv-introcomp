def gerar_subconjuntos(conjunto):
    if len(conjunto) == 0:
        return [[]]
    else:
        subsets = gerar_subconjuntos(conjunto[1:])
        next_elem = conjunto[0]
        new_subsets = []
        for subset in subsets:
            new_subsets.append([next_elem] + subset)
        return subsets + new_subsets

# Teste da função com o conjunto [1, 2, 3]
resultado = gerar_subconjuntos([1, 2, 3])
print(resultado)