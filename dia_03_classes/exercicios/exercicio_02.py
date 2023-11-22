from functools import reduce
from collections import Counter
from statistics import median


class Estatistica:

    def __init__(self, list_numbers):
        self.__list_numbers = list_numbers

    def media(self):
        list = self.__list_numbers
        sum = reduce(lambda a, b: a + b, list) / len(list)
        print(sum)

    def moda(self):
        list = self.__list_numbers
        counts = Counter(list)
        moda = max(counts.keys(), key=counts.get)
        print(moda)

    def mediana(self):
        list = self.__list_numbers
        print(median(list))

    # def mediana(self):
    #     list = self.__list_numbers
    #     if len(list) % 2 == 1:
    #         # Lista ímpar
    #         return list[len(list) // 2]
    #     else:
    #         # Lista par
    #         return (list[len(list) // 2] + list[len(list) // 2 - 1]) / 2


list_notas = [5, 4, 6, 5, 6, 7, 7, 7]


estatistica = Estatistica(list_notas)
estatistica.moda()
estatistica.mediana()
estatistica.media()
