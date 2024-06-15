def soma_dos_digitos(numero):
    soma = 0
    while numero > 0:
        soma += numero % 10
        numero = numero // 10
    return soma

def gerar_numeros_harshad(n):
    numeros_harshad = []
    numero_atual = 1
    
    while len(numeros_harshad) < n:
        if numero_atual % soma_dos_digitos(numero_atual) == 0:
            numeros_harshad.append(numero_atual)
        numero_atual += 1
    
    return numeros_harshad

# Leitura do valor de n
n = int(input("Digite o valor de n: "))

# Geração e impressão dos números de Harshad
numeros_harshad = gerar_numeros_harshad(n)
print(numeros_harshad)