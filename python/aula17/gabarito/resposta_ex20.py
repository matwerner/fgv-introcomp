def decodificar_cifra_cesar(mensagem_criptografada, chave):
    mensagem_decodificada = ""    
    for caractere in mensagem_criptografada:
        if 'a' <= caractere <= 'z':
            nova_posicao = (ord(caractere) - chave - ord('a')) % 26 + ord('a')
            mensagem_decodificada += chr(nova_posicao)
        else:
            mensagem_decodificada += caractere
    
    return mensagem_decodificada

# Exemplo de uso:
mensagem_criptografada = "fdhvdu"
chave = 3
print(decodificar_cifra_cesar(mensagem_criptografada, chave))  # Saída esperada: "caesar"