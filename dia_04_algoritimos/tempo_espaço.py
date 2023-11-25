# Esse funçao ler um array, se ela receber 10 numeros
# retorna um array de 10 numeros se 20 retorna 20

# Á Complexidade de Tempo, temos aqui uma taxa de crescimento linear O(n),

# Conforme a entrada cresce, a saída também cresce e, consequentemente,
# o espaço ocupado por ela, o que implica dizer que sua Complexidade de Espaço
# é dada por O(n).

def squared_array(numbers):
    array_of_squares = []
    for number in numbers:
        array_of_squares.append(number * number)

    return array_of_squares

# Complexicidade de tempo vai ser 0(n)
# Complexicidade de espaço 0(n)


def multiply_array(numbers):
    result = 1
    for number in numbers:
        result *= number

    return result


# Complexicidade de tempo vai ser 0(n)
# Complexicidade de espaço 0(1)
