def encontrar_termos(texto, termos):
    # Divide o texto em linhas
    linhas = texto.split('\n')
    
    # Cria um dicionário para armazenar os termos e as linhas em que aparecem
    resultado = {termo: [] for termo in termos}
    
    # Percorre cada linha do texto
    for i, linha in enumerate(linhas, start=1):
        # Verifica se cada termo aparece na linha
        for termo in termos:
            if termo in linha:
                resultado[termo].append(i)
    
    return resultado

# Função para ler o conteúdo de um arquivo
def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        return arquivo.read()

# Caminhos dos arquivos de entrada
caminho_texto = "texto.txt"
caminho_termos = "termos.txt"

# Lê o conteúdo dos arquivos
texto = ler_arquivo(caminho_texto)
termos = ler_arquivo(caminho_termos).strip().split('\n')

# Chama a função e obtém o resultado
resultado = encontrar_termos(texto, termos)

# Imprime o resultado de forma formatada
for termo, linhas in resultado.items():
    linhas_formatadas = ", ".join(map(str, linhas))
    if len(linhas) > 1:
        print(f"Termo '{termo}' aparece nas linhas: {linhas_formatadas}")
    else:
        print(f"Termo '{termo}' aparece na linha: {linhas_formatadas}")
