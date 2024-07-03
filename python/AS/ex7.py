def calcular_ari(texto):
    # Poderia usar string.ascii_lowercase e string.digits, para simplificar
    letras = 'abcdefghijklmnopqrstuvwxyz'
    numeros = '0123456789'
    pontuacoes = '.?!'

    # Remover caracteres não alfanuméricos que não são espaços nem pontuações finais
    texto_limpo = ''
    for c in texto:
        if c in letras or c in numeros or c in pontuacoes or c == ' ':
            texto_limpo += c

    # Contar caracteres válidos (números e letras)
    num_caracteres = 0
    for c in texto_limpo:
        if c in letras or c in numeros:
            num_caracteres += 1
    
    # Contar palavras (sequências de caracteres válidos separadas por espaços em branco)
    # Texto só deveria ter letras, números, espaços e pontuações finais
    palavras = texto_limpo.split() 
    num_palavras = 0
    for palavra in palavras:
        for c in palavra:
            # Se a palavra tiver pelo menos um caractere alfanumérico, considerar como uma palavra
            # Ignorar pontuações finais sozinhas
            if c in letras or c in numeros:
                num_palavras += 1
                break
    
    # Para facilitar a contagem de sentenças, normalizar o texto substituindo pontuações finais por pontos
    texto_limpo = texto_limpo.replace('?', '.')
    texto_limpo = texto_limpo.replace('!', '.')
    sentencas = texto_limpo.split('.')
    num_sentencas = 0
    for sentenca in sentencas:
        # Ignorar sentenças vazias. Exemplo: A.. B
        if len(sentenca.strip()) == 0:
            continue
        num_sentencas += 1

    # Calcular ARI usando a fórmula
    score_ari = 4.71 * (num_caracteres / num_palavras) + 0.5 * (num_palavras / num_sentencas) - 21.43
    print("#caracteres: ", num_caracteres)
    print("#palavras:   ", num_palavras)
    print("#sentencas:  ", num_sentencas)
    print("ARI:         ", score_ari)
    print()

# Exemplos
exemplo1 = "o ari - um indice de legibilidade automatizado - calcula a complexidade de um texto."
exemplo2 = "python3 facilita a criacao de algoritmos. algoritmos eficientes melhoram o desempenho"
calcular_ari(exemplo1)
calcular_ari(exemplo2)

T1 = "a nintendo e uma das empresas mais iconicas no mundo dos videogames, com uma historia que remonta a 1889, quando foi fundada como uma fabricante de cartas de baralho no japao! ao longo das decadas, a nintendo se reinventou inumeras vezes - eventualmente se estabelecendo como um dos principais nomes da industria de jogos eletronicos.. a empresa e conhecida por suas franquias de sucesso como mario, the legend of zelda e pokemon, que se tornaram parte integral da cultura pop. a nintendo tambem e reconhecida por suas inovacoes em hardware (desde o game boy e o nintendo ds ate o nintendo switch), que combina jogos de console com a portabilidade de um dispositivo movel."
T2 = "o playstation, desenvolvido pela sony, e uma das marcas de videogames mais populares do mundo!! lancado originalmente em 1994, o playstation revolucionou a industria com seus graficos em 3d e uma vasta biblioteca de jogos que atrairam milhoes de jogadores. a marca continuou a inovar com o lancamento de novos consoles, como o playstation 2 -- que se tornou o console mais vendido de todos os tempos -- e o playstation 4, que solidificou a sony como lider no mercado de jogos... alem dos consoles, a sony expandiu a marca playstation com servicos como o playstation network, que oferece jogos online, streaming de midia e uma comunidade global de jogadores."
T3 = "a marca xbox, criada pela microsoft, entrou no mercado de videogames em 2001 com o lancamento do xbox original. desde entao, a linha de consoles xbox tem se destacado por sua poderosa capacidade de hardware e uma forte enfase em servicos online, exemplificada pelo xbox live - que foi pioneira no jogo multiplayer online em consoles!!! com sucessos como o xbox 360 e o xbox one, a microsoft continuou a expandir o ecossistema xbox com iniciativas como o game pass,, um servico de assinatura que oferece acesso a uma vasta biblioteca de jogos. a mais recente geracao de consoles (o xbox series x e series s) reforca o compromisso da microsoft com inovacoes tecnologicas e uma experiencia de jogo integrada entre dispositivos"
calcular_ari(T1)
calcular_ari(T2)
calcular_ari(T3)