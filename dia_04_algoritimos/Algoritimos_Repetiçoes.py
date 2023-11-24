def calculations(n):
    number1 = 0
    for n1 in range(n):
        number1 += n1

    number2 = 0
    for n1 in range(n):
        for n2 in range(n):
            number2 += n1 + n2

    number3 = 0
    for n1 in range(n):
        for n2 in range(n):
            for n3 in range(n):
                number3 += n1 + n2 + n3

    return number1, number2, number3


n1, n2, n3 = calculations(100)
print(f"{n1}, {n2}, {n3}")

# Qual é a Ordem de Complexidade dele? 🤔 : A rigor, ela seria O(n + n² + n³).

# De olho na dica👀: Se os loops estão aninhados você os multiplica, e se
# estão paralelos você os soma.

# Um algoritmo que roda uma busca binária num array de tamanho n para
# cada elemento de um array de tamanho m teria O(m * log n) de complexidade.
