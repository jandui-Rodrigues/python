from collections import ChainMap

"""
  O ChainMap é uma estrutura de dados que permite que vários mapeamentos sejam
    acessados como um só. Ele recebe como parâmetro um ou mais dicionários e
    retorna um único objeto que contém uma lista desses dicionários.
"""

dict = ChainMap({'a': 1, 'b': 2}, {'c': 3, 'd': 4})

print(dict)
print(dict['a'])
print(dict['c'])
