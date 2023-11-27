"""
Transforme o algoritmo criado acima em recursivo.
"""


def count_pair_interative(n):
    count = 0
    for number in range(1, n + 1):
        if number % 2 == 0:
            count += 1
    return count


def count_pair(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return 1 + count_pair(n-1)
    else:
        return count_pair(n-1)


print(count_pair(4))
