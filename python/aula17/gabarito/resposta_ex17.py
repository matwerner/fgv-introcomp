def ler_arquivo(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as file:
        return file.read()

def limpar_texto(texto):
    texto = texto.lower()
    # Lista de caracteres a serem removidos
    caracteres_remover = ['.', ',', '!', '?', ':', ';']
    for c in caracteres_remover:
        texto = texto.replace(c, '')
    return texto

def contar_palavras(texto):
    palavras = texto.split()
    return palavras, len(palavras)

def contar_sequencias(palavras, n=2):
    sequencias = [' '.join(palavras[i:i+n]) for i in range(len(palavras)-n+1)]
    return sequencias

def contar_frequencias(lista):
    frequencias = {}
    for item in lista:
        if item in frequencias:
            frequencias[item] += 1
        else:
            frequencias[item] = 1
    return frequencias

def main():
    # Nome do arquivo de texto
    nome_arquivo = 'texto.txt'
    
    # Leitura do arquivo
    texto = ler_arquivo(nome_arquivo)
    
    # Limpeza do texto
    texto_limpo = limpar_texto(texto)
    
    # Contagem de palavras
    palavras, total_palavras = contar_palavras(texto_limpo)
    
    # Contagem de frequências de palavras
    frequencia_palavras = contar_frequencias(palavras)
    
    # Contagem de sequências de duas palavras
    sequencias_duas_palavras = contar_sequencias(palavras)
    frequencia_sequencias = contar_frequencias(sequencias_duas_palavras)
    
    # Exibição dos resultados
    print(f'Número total de palavras: {total_palavras}')
    
    print('\nTop 5 palavras mais frequentes:')
    frequencia_palavras_lista = sorted(frequencia_palavras.items(), key=lambda x: x[1], reverse=True)
    for palavra, frequencia in frequencia_palavras_lista[:5]:
        print(f'{palavra}: {frequencia}')
    
    print('\nTop 5 sequências de duas palavras mais frequentes:')
    frequencia_sequencias = sorted(frequencia_sequencias.items(), key=lambda x: x[1], reverse=True)
    for sequencia, frequencia in frequencia_sequencias[:5]:
        print(f'{sequencia}: {frequencia}')

if __name__ == '__main__':
    main()