#  1: Crie uma função que receba dois números e retorne o maior deles.


def bigger_number(num1: int, num2: int):
    return max(num1, num2)


# def bigger_number(num1: int, num2: int):
#     if num1 > num2:
#         return num1
#     return num2


bigger_number(2, 4)


#  2: Calcule a média aritmética dos valores contidos em uma lista.
def avarege(list_number):
    length_list = len(list_number)
    some = 0
    for number in list_number:
        some += number
    return some / length_list


avarege([3, 10, 7, 5, 9, 9, 8, 9])


#  3: Faça um programa que, dado um valor n qualquer, tal que n > 1,
#  imprima na tela um quadrado feito de asteriscos de lado de tamanho n.


def square_asterisks(n):
    asterisks = ""
    for square in range(n):
        asterisks += "*"

    for square in range(n):
        print(asterisks)


# square_asterisks(10)

#  4: Crie uma função que receba uma lista de nomes e retorne
#  o nome com a maior quantidade de caracteres. Por exemplo, para
#  ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"],
#  o retorno deve ser "Fernanda".


def bigger_name(list_name: str):
    big_name: str = ""
    for name in list_name:
        if len(name) > len(big_name):
            big_name = name
    return big_name


bigger_name(["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"])

# 5: Considere que a cobertura da tinta é de 1 litro para cada 3 metros
# quadrados e que a tinta é vendida em latas de 18 litros, que custam
# R$ 80,00. Crie uma função que retorne dois valores em uma tupla contendo
# a quantidade de latas de tinta a serem compradas e o preço total a partir
# do tamanho de uma parede (em m²).


def paint(area):
    CAN_PRICE = 80
    required_liters = area / 3
    required_cans = required_liters // 18
    if required_liters % 18:
        required_cans += 1
    return required_cans, required_cans * CAN_PRICE


paint(10)

# 6: Crie uma função que receba os três lado de um triângulo e informe qual o
# tipo de triângulo formado ou "não é triangulo", caso não seja
# possível formar um triângulo.


def is_triangle(side1, side2, side3):
    validate_triangle = (
        side1 + side2 > side3
        and side2 + side3 > side1
        and side1 + side3 > side2
    )
    return validate_triangle


def is_equilateral(side1, side2, side3):
    return side1 == side2 == side3


def is_isosceles(side1, side2, side3):
    return side1 == side2 or side2 == side3 or side1 == side3


def type_of_triangle(side1, side2, side3):

    if not is_triangle(side1, side2, side3):
        return "não é triângulo"

    elif is_equilateral(side1, side2, side3):
        return "equilátero"

    elif is_isosceles(side1, side2, side3):
        return "isósceles"

    else:
        return "escaleno"
