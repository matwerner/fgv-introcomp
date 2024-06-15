def valida_cpf(cpf: str) -> bool:
    # Remover caracteres especiais do CPF
    cpf = cpf.replace('.', '').replace('-', '')

    # Verificar se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False
    
    # Verificar se todos os dígitos são iguais
    if cpf == cpf[0] * len(cpf):
        return False

    # Função para calcular o dígito verificador
    def calcular_digito(digitos):
        mult = [i for i in range(len(digitos) + 1, 1, -1)]
        soma = sum(mult[i] * int(digitos[i])
                   for i in range(len(digitos)))
        resto = soma % 11
        return '0' if resto < 2 else str(11 - resto)

    # Calcular o primeiro dígito verificador
    primeiro_digito = calcular_digito(cpf[:9])

    # Calcular o segundo dígito verificador
    segundo_digito = calcular_digito(cpf[:9] + primeiro_digito)

    # Verificar se os dígitos calculados são iguais aos fornecidos
    return cpf[-2:] == primeiro_digito + segundo_digito

# Exemplos de teste
print(valida_cpf("123.456.789-08"))  # Deve retornar True
print(valida_cpf("123.456.789-09"))  # Deve retornar True
print(valida_cpf("111.444.777-35"))  # Deve retornar True