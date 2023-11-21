import random
import json
import csv

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


def game_word_scrambler():
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

# Exercício 4:
# Dado o seguinte arquivo no formato JSON,
# leia seu conteúdo e calcule a porcentagem de livros
#  em cada categoria em relação ao número total de livros.
#  O resultado deve ser escrito em um arquivo no formato CSV
#  como o exemplo abaixo.


def retrieve_books(file):
    return json.load(file)


def count_books_by_categories(books):
    categories = {}
    for book in books:
        for category in book["categories"]:
            if not categories.get(category):
                categories[category] = 0
            categories[category] += 1
    return categories


def calculate_percentage_by_category(book_count_by_category, total_books):
    return [
        [category, num_books / total_books]
        for category, num_books in book_count_by_category.items()
    ]


def write_csv_report(file, header, rows):
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(rows)


if __name__ == "__main__":
    # retrieve books
    with open("books.json") as file:
        books = retrieve_books(file)

    # count by category
    book_count_by_category = count_books_by_categories(books)

    # calculate percentage
    number_of_books = len(books)
    books_percentage_rows = calculate_percentage_by_category(
        book_count_by_category, number_of_books
    )

    # write csv
    header = ["categoria", "percentagem"]
    with open("report.csv", "w") as file:
        write_csv_report(file, header, books_percentage_rows)

# Exercício 5


def divisible_by_three_or_five(n):
    divisibol = []

    for index in range(n):
        index += 1
        if index % 5 == 0 and index % 3 == 0:
            divisibol.append('FizzBuzz')
            continue
        elif index % 5 == 0:
            divisibol.append("Buzz")
            continue
        elif index % 3 == 0:
            divisibol.append('Fizz')
            continue
        divisibol.append(index)

    return divisibol


print(divisible_by_three_or_five(15))


# Exercício 6


def validate_email(email):
    index = 0
    if not email[index].isalpha():
        raise ValueError("Username should start with a letter")

    # validate username
    while email[index] != "@" and index < len(email):
        letter = email[index]
        if (
            not letter.isalpha()
            and not letter.isdigit()
            and letter not in ("_", "-")
        ):
            raise ValueError(
                "Username should contain only letters, "
                "digits, dashes or underscores"
            )
        index += 1
    index += 1  # @
    # validate website
    while email[index] != "." and index < len(email):
        letter = email[index]
        if not letter.isalpha() and not letter.isdigit():
            raise ValueError(
                "Website should contain only letters, and digits"
            )
        index += 1

    index += 1  # .
    # validate extension
    counter = 0
    while index < len(email):
        counter += 1
        index += 1
    if counter > 3:
        raise ValueError("Extension maximum length is 3")
    return None
