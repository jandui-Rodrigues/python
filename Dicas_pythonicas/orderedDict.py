from collections import OrderedDict

"""
    O OrderedDict é um dicionário que mantém a ordem de inserção dos elementos.
    Ele é diferente do dicionário comum, que não garante a ordem dos elementos.
"""

dict = OrderedDict()

dict['a'] = 1
dict['b'] = 2
dict['c'] = 3
dict['d'] = 4

print(dict)  # OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
# Caso eu mude a ordem de inserção dos elementos, o OrderedDict não será
# alterado
