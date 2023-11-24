from functools import cache
from dataclasses import dataclass
from typing import Any

# O cache serve para armazena valores, caso eu procise calcular
# algo que ja esta na memoria, ele me poupa a logica de calcular
# aquele valor, eleminando assim o processamento desnecesario
# tente executar com é sem o cache e veja quantas vezes o Ativou aparece


@cache
def fibonacci(n):
    if n <= 1:
        print('Ativou')
        return n
    else:
        print('Etivou else')
        return fibonacci(n - 1) + fibonacci(n - 2)


# Criando classes de maneiras mais simplificadas

@dataclass
class Pessoa:
    name: str
    last_name: str

    def __getattribute__(self, __name: str) -> Any:
        return __name


joao = Pessoa('joao', 'vasconcelos')
# joao.__getattribute__('jhon')

print(joao)
