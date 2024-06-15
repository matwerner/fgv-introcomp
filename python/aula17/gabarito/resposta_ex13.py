def validar_ean13(codigo):
    if len(codigo) != 13 or not codigo.isdigit():
        return "Código de barras inválido. Deve conter 13 dígitos numéricos."
    
    soma_impares = sum(int(codigo[i]) for i in range(0, 12, 2))
    soma_pares = sum(int(codigo[i]) for i in range(1, 12, 2)) * 3
    
    soma_total = soma_impares + soma_pares
    digito_verificador_calculado = (10 - (soma_total % 10)) % 10
    digito_verificador_fornecido = int(codigo[12])
    
    print(soma_impares)
    print(soma_pares)
    print(digito_verificador_calculado)
    print(digito_verificador_fornecido)
    if digito_verificador_calculado == digito_verificador_fornecido:
        return "Código de barras válido."
    else:
        return "Código de barras inválido."

# Teste do programa com o código de barras do exemplo
codigo_barras = "4006381333931"
resultado = validar_ean13(codigo_barras)
print(resultado)  # Deve imprimir "Código de barras válido."