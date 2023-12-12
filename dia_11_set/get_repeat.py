"""
Dada um lista de numeros,
retorne apens os duplicados
"""


def get_repeat(numbers):
    numbers_set = set()
    repeated_numbers = set()

    for number in numbers:
        if number in numbers_set:
            repeated_numbers.add(number)
        else:
            numbers_set.add(number)


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9]
    # resultado esperado: [8]
    print(get_repeat(numbers))
