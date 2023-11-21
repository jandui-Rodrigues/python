import json


def read_json():
    pokemons = open("pokemon.json")
    pokemon = json.load(pokemons)["results"]
    return pokemon


def write_json(content):
    with open('grass_pokemons.json', 'w') as file:
        # transfoma o text em um json
        # write_json = json.dumps(content)
        # file.write(write_json)
        json.dump(content, file)


pokemons = read_json()

grass_type_pokemons = [pokemon
                       for pokemon in pokemons
                       if "Grass" in pokemon["type"]
                       ]
print(len(pokemons))
print(len(grass_type_pokemons))
write_json(grass_type_pokemons)
