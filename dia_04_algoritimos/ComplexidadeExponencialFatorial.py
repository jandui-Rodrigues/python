cidades = ["São Paulo", "Belo Horizonte", "Campina Grande", 'Cajazeiraz']


def caixeiro_viajante(cidades):
    possibilidades = 1
    for fatorial in range(len(cidades)):
        possibilidades *= fatorial + 1

    return possibilidades


print(caixeiro_viajante(cidades))
