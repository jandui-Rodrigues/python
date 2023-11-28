from typing import List
from collections import namedtuple

# Iterativa


def countdownWhile(n):
    while n > 0:
        print(n)
        n = n - 1


# Recursividade
def countdown(n):
    if n == 0:  # caso base
        print("FIM!")
    else:
        print(n)
        countdown(n - 1)  # caso recursivo


def factorial(n):
    if n <= 1:  # caso base
        return 1
    else:
        return n * factorial(n - 1)  # caso recursivo


def somaRecursive(n):
    if n == 0:
        return 0
    else:
        return n + somaRecursive(n - 1)


# print(somaRecursive(4))

Caixa = namedtuple("Caixa", ["tem_chave", "porta"])

caixas: List[Caixa] = [
    Caixa(False, 0),
    Caixa(False, 0),
    Caixa(False, 3),
    Caixa(False, 5),
    Caixa(True, 1),
    Caixa(False, 6),
]


def find_box(list_box: List[Caixa], index: int = 0) -> Caixa:
    # Caso base
    if len(list_box) <= 1:
        return Caixa(False)
    # Caso base
    caixa = list_box[index]
    if caixa.tem_chave:
        return caixa
    # Caso recursivo
    index += 1
    return find_box(list_box, index)


print(find_box(caixas))
