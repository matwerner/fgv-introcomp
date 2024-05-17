import random

# Lista de palavras para o jogo
palavras = ["python", "programacao", "computador", "algoritmo", "desenvolvimento", "openai", "inteligencia"]

def escolher_palavra():
    return random.choice(palavras)

def mostrar_palavra(palavra, letras_adivinhadas):
    resultado = ""
    for letra in palavra:
        if letra in letras_adivinhadas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado

def jogo_da_forca():
    palavra_secreta = escolher_palavra()
    letras_adivinhadas = []
    tentativas_restantes = 6

    print("Bem-vindo ao Jogo da Forca!")
    print("Adivinhe a palavra secreta.")

    while tentativas_restantes > 0:
        print("\nPalavra: ", mostrar_palavra(palavra_secreta, letras_adivinhadas))
        print("Tentativas restantes:", tentativas_restantes)

        palpite = input("Digite uma letra: ").lower()

        if palpite in letras_adivinhadas:
            print("Você já tentou essa letra. Tente novamente.")
        elif palpite in palavra_secreta:
            letras_adivinhadas.append(palpite)
            if set(letras_adivinhadas) == set(palavra_secreta):
                print("\nParabéns! Você ganhou! A palavra era:", palavra_secreta)
                break
        else:
            tentativas_restantes -= 1
            print("Letra não encontrada. Tente novamente.")

    if tentativas_restantes == 0:
        print("\nVocê perdeu! A palavra era:", palavra_secreta)

jogo_da_forca()