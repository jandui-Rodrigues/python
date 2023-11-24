# A estrutura deve estar ordenada para que a busca binária funcione
def binary_search(numbers, target):
    # definir os índices
    start = 0
    end = len(numbers) - 1
    # 5

    while (
        start <= end
    ):  # os índices podem ser no máximo iguais, o início não pode
        # ultrapassar o fim
        mid = (start + end) // 2  # encontro o meio 3

        if (
            numbers[mid] == target
        ):  # se o elemento do meio for o alvo, devolve a posição do meio
            return mid

        if target < numbers[mid]:  # se o elemento for menor,
            # atualiza o índice do fim
            end = mid - 1
        else:  # caso contrário, atualiza o índice do inicio
            start = mid + 1

    return -1  # Não encontrou? Retorna -1


find_number = [3, 7, 10, 50]
numbers = [2, 3, 4, 10, 40]
target = 40

result = binary_search(numbers, target)
print(f"Elemento encontrado na posição: {result}")

# Exercício
# Imagine que você recebe dois arrays de tamanho igual, array1 e array2.
#  Para cada elemento do array1, realize uma busca binária no array2.
#  Mostre que a ordem de complexidade do algoritmo
#  resultante é O(n * log n), ou O(n log n).


def find_number_binary(find_numbers, numbers_search):
    find = []
    for number in find_number:
        find.append(binary_search(numbers_search, number))
    return find
