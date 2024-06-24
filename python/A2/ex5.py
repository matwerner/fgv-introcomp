def verificar_cartao(numero):
    numero = str(numero)
    inverso = numero[::-1]

    impares = []
    for i in range(0, len(inverso), 2):
        impares.append(int(inverso[i]))
    s1 = sum(impares)
    print("s1", s1)

    pares = []
    for j in range(1, len(inverso), 2):
        pares.append(int(inverso[j]))
    
    temp = []
    for par in pares:
        n = par * 2
        n = sum([int(d) for d in str(n)])
        temp.append(n)
    s2 = sum(temp)
    print("s2", s2)

    return (s1 + s2) % 10 == 0

# A)
print('A soma S1 do cartão 30569309025904 é 33')
print(verificar_cartao(30569309025904))

# B)
print('A soma S2 do cartão 37144963539 é 21')
print(verificar_cartao(37144963539))

# C)
print('O cartão 4539148803436467 é valido')
print(verificar_cartao(4539148803436467))

# D) 
print('Os cartões 453914880343, 540436789012345 e 60116011601166 são todos inválidos')
print(verificar_cartao(453914880343))
print(verificar_cartao(540436789012345))
print(verificar_cartao(60116011601166))

# E) 
print('Os cartões 453215876690 e 356600202036050 são válidos')
print(verificar_cartao(453215876690))
print(verificar_cartao(356600202036050))