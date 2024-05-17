# Entrada:
hangman_words = [
    'python',
    'algoritmo',
    'programacao'
]

num_max_errors = 5

def choose_word():
    return hangman_words[0]

def print_word_terminal(word, characters_used):
    word_to_user = ''
    for c in word:
        if c in characters_used:
            word_to_user += c
        else:
            word_to_user += '_'
    print(f'Palavra: {word_to_user}')

def print_current_game_state(word, characters_used, num_errors, num_max_errors):
    print_word_terminal(word, characters_used)
    print(f'Letras já utilizadas: {sorted(list(characters_used))}')
    print(f'Número de tentativas restantes: {num_max_errors - num_errors}')
    print()

def print_win_game_state():
    print('Você ganhou!')
    exit()

def print_lost_game_state(word):
    print('Você perdeu.')
    print(f'A palavra era: {word}')
    exit()

# Data
word = choose_word()
characters_used = set()
num_errors = 0

while num_errors < num_max_errors:
    print_current_game_state(word, characters_used, num_errors, num_max_errors)

    c = input('Selecione uma letra: ')
    if c not in word:
        num_errors += 1
    characters_used.add(c)

    # Whether user won or lost
    if set(word).issubset(characters_used):
        print_win_game_state()
    elif num_errors == num_max_errors:
        print_lost_game_state(word)
