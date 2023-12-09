from collections import defaultdict

"""
    O defaultdict é um dicionário que, quando tentamos acessar uma chave que
    não existe, ele cria essa chave e já atribui um valor padrão a ela.
"""


default = defaultdict(list)
default['time'].append('Flamengo')
default['time'].append('Vasco')
default['time'].append('Botafogo')
default['time'].append('Fluminense')

print(default["time"], default['Carros'])
