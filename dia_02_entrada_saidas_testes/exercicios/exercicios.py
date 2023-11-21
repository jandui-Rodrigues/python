import random

# Exercício 1:
# Faça um programa que receba um nome e imprima
# o mesmo na vertical em escada invertida.


def inverted_staircase():
    strign = 'PEDRO'

    for letter in strign:
        print(strign)
        firt, *rest = strign
        strign = "".join(rest)

# Exercício 2:
# Jogo da palavra embaralhada. Desenvolva um jogo em que a pessoa usuária
# tenha que adivinhar uma palavra que será mostrada com as letras embaralhadas.
# O programa terá uma lista de palavras e escolherá uma aleatoriamente.
#  O jogador terá três tentativas para adivinhar a palavra. Ao final,
#  a palavra deve ser mostrada na tela, informando se a pessoa ganhou
#  ou perdeu o jogo.

# Exercício 3:
# Modifique o exercício anterior para que as palavras sejam
#  lidas de um arquivo. Considere que o arquivo terá cada palavra em uma linha.


def read_words(file_name):
    file = open(file_name)
    words = file.read().split('\n')
    return words


def jogo():
    list_words = read_words('frutas.txt')
    # Sorteia uma palavra
    word = random.choice(list_words)
    # Embaralhs palavra
    scrambled_word = "".join(random.sample(word, len(word)))
    count = 0
    print(scrambled_word)
    while True:
        is_word = input('Digite qual e a palavra sorteada :')
        count += 1
        if is_word == word:
            print('Parabens voce acertou a palavra')
            break
        if count == 3:
            print('Não foi dessa vez')
            break

    print(f"A palavras era {word}")


jogo()
