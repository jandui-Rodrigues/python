# “Informalmente, um algoritmo é qualquer procedimento computacional bem
# definido que toma algum valor ou conjunto de valores como entrada e produz
# algum valor ou conjunto de valores como saída. Portanto, um algoritmo é uma
# sequência de etapas computacionais que transformam a entrada na saída”
# (CLRS - Introduction to Algorithms)

# Quanto tempo esse código vai demorar em sua execução?
# Isso depende de muitos fatores”. Afinal, o tempo de execução depende da
# máquina, do que está rodando nela, dos recursos etc.
# Não conseguimos dizer isso apenas ao olhar para o código.


def sum_array(numbers):
    sum = 0
    for number in numbers:
        sum += number

    return sum


# Suponha que, para o array abaixo, o tempo de execução seja `n`
sum_array('array_com_dez_mil_numeros')

# Nesse caso, aqui o tempo de execução vai ser `10 * n`, ou `10n`, já que
#  o array é dez vezes maior que o anterior
sum_array('array_com_cem_mil_numeros')

# Já esse é dez mil vezes maior que o primeiro, então esse aqui executa em
#  `100n`
sum_array('array_com_um_milhão_de_numeros')

# É isso que chamamos de complexidade: A taxa de crescimento do tempo de
#  execução de um algoritmo; quanto maior é essa taxa, maior é seu tempo de
#  execução e, portanto, maior sua complexidade.


# A função matemática que representa uma relação linear é f(n) = n e a notação
#  de Ordem de Complexidade para representar a taxa de crescimento do tempo de
#  execução de um algoritmo é dada por O(n), onde o n representa a quantidade
# de operações que o algoritmo vai realizar.
