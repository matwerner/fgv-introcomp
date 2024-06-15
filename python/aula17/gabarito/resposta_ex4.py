def freq_intervalos(lista):
    # Determinar o valor máximo e mínimo na lista
    max_valor = max(lista)
    min_valor = min(lista)
    
    # Calcular a amplitude dos intervalos
    amplitude = (max_valor - min_valor + 1) // 5
    
    # Inicializar o dicionário para armazenar as frequências
    freq_dict = {'{}-{}'.format(i, i + amplitude - 1): 0
                 for i in range(min_valor, max_valor, int(amplitude))}
    
    # Atribuir os valores da lista aos intervalos e calcular as frequências
    for num in lista:
        for key in freq_dict:
            inicio, fim = map(int, key.split('-'))
            if inicio <= num <= fim:
                freq_dict[key] += 1
                break
    
    return freq_dict

# Exemplo de uso da função
lista_numeros = [5, 12, 20, 27, 33, 40, 55, 63, 70, 88, 94, 99]
print(freq_intervalos(lista_numeros))