# Exercício 1: Dada uma lista, descubra o menor elemento.
# Por exemplo, [5, 9, 3, 19, 70, 8, 100, 2, 35, 27] deve retornar 2.

list = [5, 9, 3, 19, 70, 8, 100, 2, 35, 27]
min(list)


def min_number_list():
    min_number = list[0]

    for number in list:
        if number < min_number:
            min_number = number
    return min_number


min_number_list()


# Exercício 2: Faça um programa que, dado um valor n qualquer, tal que n > 1,
#  imprima na tela um triângulo retângulo com n asteriscos de base.
#  Por exemplo, para n = 5 o triângulo terá 5 asteriscos na base:


def draw_asterisk_up(n):
    for index in range(n):
        repeat = index + 1
        print(repeat * "*")


def draw_asterisk_down(n):
    for index in range(n):
        repeat = n - index
        print(repeat * "*")


draw_asterisk_up(5)
draw_asterisk_down(5)


# Exercício 3: Crie uma função que receba um número inteiro N
#  e retorne o somatório de todos os números de 1 até N.
#  Por exemplo, para N = 5, o valor esperado será 15.


def some_number(n: int):
    some = 0
    for number in range(n):
        some += number + 1

    return some


some_number(5)

type_fuel = {
    "A": {"price": 1.90, "discount": 0.03, "discount_target": 0.05},
    "G": {"price": 2.50, "discount": 0.04, "discount_target": 0.06},
}


def price_liters(type, liters):
    price = type_fuel[type]["price"]
    discount = type_fuel[type]["discount"]

    if liters > 20:
        discount = type_fuel[type]["discount_target"]
    total = price * liters
    total -= total * discount
    return total
