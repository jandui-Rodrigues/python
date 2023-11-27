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


print(somaRecursive(4))
