# Depoes do /podemos nomear a chamada dos parametros antes disso
# devesse passar os parametroe em ordem posicional


def produtorio(list, /, inicio=1):
    total = inicio or 1
    for item in list:
        total *= item
    return total


print(produtorio([1, 2, 3], inicio=3))
# Retorna um Erro
# print(produtorio(list=[1, 2, 3], inicio=3))


# Apos o (*) os paramentros devem ser passavos sendo nomeados


def name_and_last_name(name, *, last_name):
    return f"{name} { last_name}"


# # Certo
print(name_and_last_name('jandui', last_name='junior'))
# # Errado
# print(name_and_last_name('jandui', 'junior'))
