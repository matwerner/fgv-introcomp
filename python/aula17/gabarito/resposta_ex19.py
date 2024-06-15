def expand_number(num):
    # Verifica se o número é positivo
    if num <= 0:
        return "O número deve ser um inteiro positivo."

    # Convertendo o número para string para facilitar a manipulação
    num_str = str(num)
    length = len(num_str)

    # Lista para armazenar os componentes da expansão
    expanded_parts = []

    # Percorre cada dígito
    for i in range(length):
        # Pega o valor do dígito atual
        digit = int(num_str[i])

        # Calcula o valor posicional (unidade, dezena, centena, etc.)
        positional_value = digit * (10 ** (length - i - 1))

        # Adiciona na lista se o valor posicional for diferente de zero
        if positional_value != 0:
            expanded_parts.append(str(positional_value))

    # Junta todos os componentes com ' + '
    expanded_form = " + ".join(expanded_parts)
    
    return expanded_form

# Solicita ao usuário que insira um número decimal inteiro positivo
num = int(input("Insira um número decimal inteiro positivo: "))

# Chama a função e imprime o resultado
expanded_form = expand_number(num)
print(expanded_form)